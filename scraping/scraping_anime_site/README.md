### Projet de Scraper d'Animes

Ce projet utilise Python pour scraper des détails sur les animes à partir du site `yummyanime.tv`, stocke les données dans un fichier JSON et fournit des fonctionnalités pour vérifier les doublons et rechercher des titres spécifiques.

#### Scripts Python inclus :

1. **main.py** :
   - Scrapes les détails des animes à partir de `yummyanime.tv`, et les sauvegarde dans un fichier JSON.
   - Utilise `requests` pour les requêtes HTTP et `BeautifulSoup` pour l'analyse HTML.

2. **check_duplicates.py** :
   - Vérifie les doublons dans un fichier JSON contenant une liste de titres d'animes.
   - Affiche les titres en double et leur nombre d'occurrences.

3. **movie_search.py** :
   - Permet de rechercher la disponibilité d'un anime spécifique dans la base de données JSON générée par `main.py`.
   - Demande à l'utilisateur d'entrer le nom de l'anime à rechercher.

#### Utilisation :

1. **Prérequis** :
   - Python 3.x installé.
   - Les packages Python requis (`requests`, `beautifulsoup4`) installés. Vous pouvez les installer via `pip` :

     ```
     pip install requests beautifulsoup4
     ```

2. **Exécution** :

   a. **main.py** :
      - Exécutez `main.py` pour scraper les données d'animes. Entrez le nombre de pages à scraper lorsque vous y êtes invité.

     ```
     python main.py
     ```

   b. **check_duplicates.py** :
      - Après avoir exécuté `main.py` et généré `all_anime_details.json`, exécutez `check_duplicates.py` pour vérifier les doublons.

     ```
     python check_duplicates.py
     ```

   c. **movie_search.py** :
      - Pour rechercher un anime spécifique dans `all_anime_details.json`, exécutez `movie_search.py` et suivez les instructions pour entrer le nom de l'anime recherché.

     ```
     python movie_search.py
     ```

#### Structure du fichier JSON :

- Le fichier `all_anime_details.json` contient une liste d'objets JSON, chaque objet représentant un anime avec des détails comme le titre, le lien et des détails supplémentaires.

#### Notes :

- Assurez-vous que tous les fichiers (`main.py`, `check_duplicates.py`, `movie_search.py`) et le fichier `all_anime_details.json` sont dans le même répertoire pour un fonctionnement correct des scripts.
