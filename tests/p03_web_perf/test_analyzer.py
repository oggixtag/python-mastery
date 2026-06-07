import pytest
import pandas as pd
from src.p03_web_perf.analyzer import WebAnalyzer

"""L'objectif de ce test : je veux vérifier que lorsque je crée une instance de ma classe WebPerfAnalyzer, elle configure correctement le chemin vers le fichier CSV où seront stockées les données."""
def test_initialisation_chemin_csv():
    """Vérifie que l'analyseur pointe bien sur le bon fichier CSV par défaut."""
    # 1. On instancie de la classe
    analyzer = WebAnalyzer()

    # 2. On vérifier que le chemin du fichier soit correct
    assert analyzer.csv_file.endswith("web_perf_metrics.csv")

@pytest.fixture
def faux_fichet_csv(tmp_path):
    """Génère un fichet de test"""
    test_csv = tmp_path / "faux_metrique.csv"
    
    """Ajout the données"""
    donnees = {
        "Date": ["2026-06-06 10:00:00","2026-06-06 10:05:00","2026-06-06 10:10:00"],
        "URL": ["https://python.org", "https://free-work.com", "https://error-site.com"],
        "Statut_HTTP": ["200","200","500"],
        "Temps_Reponse_Sec": [0.123, 2.456, 0.789],
        "Poids_HTML_Ko": [50.5, 75.2, 100.0],
        "Erreurs": ["Aucune", "Aucune", "HTTP Error: Bad Request"]
    }

    """Création du DataFrame"""
    df = pd.DataFrame(donnees)

    """Enregistrement du DataFrame dans un fichier CSV"""
    df.to_csv(test_csv, index=False, encoding="utf-8")

    return str(test_csv)

"""L'objectif du test : prendre en compte les faux metrique"""
def test_faux_metrique(faux_fichet_csv):
    
    # --- ARRANGE : Définir les données que l'on veut sauvegarder. ---
    # 1. on instancie l'analysateur
    analyser = WebAnalyzer
    # 2. on inject les faux metrique
    analyser.csv_file = faux_fichet_csv

    # --- ACT :  On exécute l'action à tester. ---
    # 3. on charge le DataFrame
    df = pd.read_csv(analyser.csv_file)
    df_succes = df[df["Statut_HTTP"] == 200]
    # 4. règles métier
    total_analysed = len(df)
    total_succes = len(df_succes)
    taux_reussite = (total_succes / total_analysed) * 100
    df_lentes = df_succes[df_succes["Temps_Reponse_Sec"] > 2.0]

    # --- ASSERT : On effectue toutes les vérifications ---
    # 1. Vérification du volume global
    assert total_analysed == 3
    # 2. Vérification du taux de réussite calculé
    assert round(taux_reussite, 2) == 66.67
    # 3. Vérification du filtrage des alertes de lenteur
    assert len(df_lentes) == 1
    assert df_lentes.iloc[0]["URL"] == "https://free-work.com"
