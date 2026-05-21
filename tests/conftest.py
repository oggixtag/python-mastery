import pytest
import json

@pytest.fixture
def fichier_test_vide(tmp_path):
    # tmp_path est fourni automatiquement par pytest (c'est un dossier temporaire unique pour le test)
    fichier = tmp_path / "test_taches.json"
    
    # On initialise le fichier avec une liste vide
    with open(fichier, 'w', encoding='utf-8') as f:
        json.dump([], f)
        
    return str(fichier) # Retourne le chemin du fichier temporaire

@pytest.fixture
def fichier_avec_donnees(tmp_path):
    # 1. On définit le chemin du fichier dans un dossier temporaire
    dossier_data = tmp_path / "data"
    dossier_data.mkdir()
    fichier = dossier_data / "taches_test.json"
    
    # 2. On prépare la liste que tu as choisie
    donnees_initiales = [
        {"nom": "Acheter du pain", "statut": "à faire"},
        {"nom": "Devoir", "statut": "en cours"},
        {"nom": "courses", "statut": "terminé"}
    ]
    
    # 3. On écrit ces données dans le fichier
    with open(fichier, 'w', encoding='utf-8') as f:
        json.dump(donnees_initiales, f, indent=4, ensure_ascii=False)
        
    # 4. On donne le chemin (en texte) au test qui en aura besoin
    return str(fichier)