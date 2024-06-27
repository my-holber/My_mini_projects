import json


def check_movie_availability(movie_name, database_file):
    # Lire le contenu du fichier JSON
    try:
        with open("all_anime_details.json", 'r', encoding='utf-8') as f:
            movie_database = json.load(f)
    except FileNotFoundError:
        print(f"Fichier '{database_file}' non trouvé.")
        return
    
    titles = []
    for movie_item in movie_database:
        titles.append(movie_item["Title"])

    # Vérifier si le film est présent dans la base de données
    if movie_name in titles:
        print(f"Le film '{movie_name}' est disponible dans la base de données.")
    else:
        print(f"Le film '{movie_name}' n'est pas disponible dans la base de données.")

# Exemple d'utilisation
def main():
    database_file = "all_anime_details.json"  # Le fichier JSON contenant les titres des films disponibles
    movie_name = input("Entrez le nom du film que vous recherchez : ")
    check_movie_availability(movie_name, database_file)

if __name__ == "__main__":
    main()
