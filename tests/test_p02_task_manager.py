from src.p02_task_manager.main import sauvegarde
from src.p02_task_manager.main import charger_fichier
import json
import pytest

# Fonction de sauvegarde des taches dans un fichier JSON
def test_sauvegarde(fichier_test_vide):
    # --- ARRANGE (Préparer) ---
    # On prépare une liste avec une tâche concrète
    taches_a_sauver = [{"nom": "Test Unitaire", "statut": "à faire"}]

    # --- ACT (Agir) ---
    # C'est ici qu'on appelle ta fonction sauvegarde(src\p02_task_manager\main.py)
    # le deuxième paramètre est la fonction conftest
    sauvegarde(taches_a_sauver, fichier_test_vide)

    # --- ASSERT (Vérifier) ---
    # On vérifiera ici si le fichier contient bien nos données
    with open(fichier_test_vide, 'r', encoding='utf-8') as fichier:
        donnees_lues = json.load(fichier) 
    
    # On vérifie si les données lues correspondent aux données sauvegardées
    assert donnees_lues == taches_a_sauver, "Les données lues ne correspondent pas aux données sauvegardées"

# Fonction pour vérifier l'absence du fichier , dans ce contexte le fichier est vide
def test_chargement_fichier_absent(tmp_path):
    # Arrange
    fichier_absent = tmp_path / "taches_virtuelles.json"
    
    # Act
    taches_chargees = charger_fichier(fichier_absent)

    # Assert
    assert taches_chargees == [], "Le fichier devrait être vide car il n'existe pas."

# Fonction pour vérifier le fichier corrompu 
def test_fichier_corrompues(tmp_path):
    # Arrange
    fichier_corrompu = tmp_path / "taches_virtuelles.json"
    fichier_corrompu.write_text("Bonjour")

    # Act
    with pytest.raises(json.JSONDecodeError):
        charger_fichier(fichier_corrompu)

    # Assert

# Fonction pour vérifier l'ajout d'une tache
def test_ajout_tache(fichier_avec_donnees):
    # Arrange
    taches = charger_fichier(fichier_avec_donnees)

    # Act
    nouvelle_tache = {"nom": "Test ajout d'une tache", "statut": "à faire"}
    taches.append(nouvelle_tache)
    sauvegarde(taches, fichier_avec_donnees)

    # Assert
    taches_finales = charger_fichier(fichier_avec_donnees)
    assert nouvelle_tache in taches_finales