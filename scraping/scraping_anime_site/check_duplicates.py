import json

def check_duplicates(json_file):
    """
    Vérifie les doublons dans un fichier JSON contenant une liste de titres.

    Args:
    json_file (str): Le chemin du fichier JSON à vérifier.

    Returns:
    list: Une liste des titres dupliqués, s'il y en a.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            titles = json.load(f)
        
        # Utiliser un dictionnaire pour compter les occurrences de chaque titre
        title_counts = {}
        for title in titles:
            if title in list(title_counts.keys()):
                title_counts[title] += 1
            else:
                print(title)
                title_counts[title] = 1
        
        # Filtrer les titres ayant plus d'une occurrence
        duplicates = [title for title, count in title_counts.items() if count > 1]

        if duplicates:
            print("Des doublons ont été trouvés dans le fichier JSON:")
            for dup in duplicates:
                print(f'Titre: "{dup}", Nombre de répétitions: {title_counts[dup]}')
        else:
            print("Aucun doublon trouvé dans le fichier JSON.")
        
        return duplicates

    except FileNotFoundError:
        print(f"Le fichier {json_file} n'a pas été trouvé.")
        return []
    except json.JSONDecodeError:
        print(f"Le fichier {json_file} ne contient pas un JSON valide.")
        return []

# Exemple d'utilisation
if __name__ == "__main__":
    json_file = "all_anime_details.json"
    check_duplicates(json_file)