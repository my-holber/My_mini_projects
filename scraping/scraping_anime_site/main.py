import requests
from bs4 import BeautifulSoup
import json

# Définir l'en-tête avec le User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# Initialiser une liste pour stocker les données de tous les animes
cache_anime_titles = []
all_anime_data = []

# Définir le nombre de pages à scraper
num_pages = int(input("[+] -> "))

for page in range(1, num_pages + 1):
    try:
        # URL cible pour chaque page
        url = f"https://yummyanime.tv/series/page/{page}/"
        
        # Envoyer la requête
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Analyse HTML en utilisant BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Trouver tous les éléments avec la classe "movie-item"
        movie_items = soup.find_all("div", {"class": "movie-item"})
        print("page = ", page)
        i = 0
        
        for movie_item in movie_items:
            try:
                # Extraire le titre de chaque élément
                title_div = movie_item.find("div", {"class": "movie-item__title"})
                title = title_div.text.strip() if title_div else "Titre inconnu"
                
                i += 1
                print(f"page {page} : items = {i}")
                
                if title in cache_anime_titles:
                    # Anime déjà traité
                    continue
                
                cache_anime_titles.append(title)
                
                # Extraire le lien de chaque élément
                link_tag = movie_item.find("a", href=True)
                link = link_tag['href'] if link_tag else "#"
                
                # URL de la page de détail
                url_db = f"https://yummyanime.tv{link}"
                
                # Envoyer la requête pour la page de détail
                response_db = requests.get(url_db, headers=headers)
                response_db.raise_for_status()
                
                # Analyse HTML de la page de détail
                soup_url_db = BeautifulSoup(response_db.content, "html.parser")
                
                # Trouver la liste non ordonnée avec la classe "inner-page__list"
                inner_page_list = soup_url_db.find('ul', {'class': 'inner-page__list'})
                
                # Initialiser un dictionnaire pour stocker les données
                anime_data = {
                    "Title": title,
                    "Link": url_db,
                    "Details": {}
                }
                
                # Ajouter les informations trouvées dans le dictionnaire
                if inner_page_list:
                    items = inner_page_list.find_all('li')
                    for item in items:
                        label_span = item.find('span')
                        label = label_span.text.strip() if label_span else "Label inconnu"
                        value = item.text.replace(label, '').strip()
                        anime_data["Details"][label] = value
                
                # Ajouter les données de l'anime à la liste principale
                all_anime_data.append(anime_data)
                
            except Exception as e:
                print(f"Erreur lors du traitement de l'anime {title}: {e}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête pour la page {page}: {e}")

# Sauvegarder les données dans un fichier JSON
try:
    with open('all_anime_details.json', 'w', encoding='utf-8') as f:
        json.dump(all_anime_data, f, ensure_ascii=False, indent=4)
    print("Toutes les données ont été sauvegardées dans le fichier 'all_anime_details.json'")
except Exception as e:
    print(f"Erreur lors de la sauvegarde des données: {e}")