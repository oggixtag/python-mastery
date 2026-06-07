import os
import time
import urllib.request
from urllib.error import URLError, HTTPError
import pandas as pd
from datetime import datetime

class WebAnalyzer:
    def __init__(self):
        # Définition du chemin du fichier CSV dans le dossier data commun
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.normpath(os.path.join(base_dir, '..', '..', 'data'))
        self.csv_file = os.path.join(self.data_dir, 'web_perf_metrics.csv')
        
        # S'assurer que le dossier data existe
        os.makedirs(self.data_dir, exist_ok=True)

    def analyser_site(self, url: str) -> dict:
        """Envoie une requête HTTP, calcule les métriques et les retourne sous forme de dictionnaire."""
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            temps_debut = time.perf_counter()
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Performance Analyzer)'})
            
            with urllib.request.urlopen(req, timeout=10) as response:
                html_content = response.read()
                temps_total = time.perf_counter() - temps_debut
                
                statut = response.status
                poids_ko = len(html_content) / 1024
                erreur = "Aucune"

        except HTTPError as e:
            statut, temps_total, poids_ko, erreur = e.code, 0.0, 0.0, f"HTTP Error: {e.reason}"
        except URLError as e:
            statut, temps_total, poids_ko, erreur = 0, 0.0, 0.0, f"Network Error: {e.reason}"
        except Exception as e:
            statut, temps_total, poids_ko, erreur = 0, 0.0, 0.0, str(e)

        donnees = {
            "Date": horodatage,
            "URL": url,
            "Statut_HTTP": statut,
            "Temps_Reponse_Sec": round(temps_total, 3),
            "Poids_HTML_Ko": round(poids_ko, 2),
            "Erreurs": erreur
        }
        
        self._sauvegarder_csv(donnees)
        return donnees

    def _sauvegarder_csv(self, donnees: dict):
        """Ajoute une nouvelle ligne de métriques au fichier CSV à l'aide de Pandas."""
        df_nouvel_enregistrement = pd.DataFrame([donnees])
        
        # Si le fichier n'existe pas, on le crée avec les entêtes. Sinon, on ajoute à la suite (append).
        if not os.path.exists(self.csv_file):
            df_nouvel_enregistrement.to_csv(self.csv_file, index=False, encoding="utf-8")
        else:
            df_nouvel_enregistrement.to_csv(self.csv_file, mode='a', header=False, index=False, encoding="utf-8")

    def generer_rapport_statistique(self) -> str:
        """Utilise Pandas pour charger le CSV et calculer des statistiques globales."""
        if not os.path.exists(self.csv_file):
            return "Aucune donnée disponible. Lancez d'abord une analyse."

        # Lecture du dataset avec Pandas
        df = pd.read_csv(self.csv_file)
        total_analyses = len(df)

        if total_analyses == 0:
            return "Le fichiet est vide."
        
        # 1. Calcul du taux de réussite global
        #        
        # Filtrage des requêtes réussies pour ne pas fausser les moyennes de temps
        df_succes = df[df["Statut_HTTP"] == 200]
        #print(df_succes)  # Debug: Affiche les données filtrées pour les succès

        if df_succes.empty:
            return "Aucune analyse réussie (Statut 200) enregistrée pour générer des statistiques."

        #créé le sous-tableau df_succes pour calculer le temps moyen et le poids moyen uniquement sur les requêtes réussies (Statut 200).
        nb_succes = len(df_succes)
        taux_reussite = (nb_succes / total_analyses) * 100

        # 2. Analyse groupée par URL (Groupby)
        #print("\n--- ANALYSE DÉTAILLÉE PAR SITE (GROUPBY) ---")

        # On regroupe par URL et on applique nos trois fonctions d'agrégation
        df_sites = df_succes.groupby("URL")["Temps_Reponse_Sec"].agg(["mean", "count", "max"])
        
        # On renomme les colonnes pour un affichage propre
        df_sites.columns = ["Vitesse_Moyenne_Sec", "Nombre_Tests", "Temps_Max_Sec"]
        
        # On affiche le tableau trié du plus rapide au plus lent
        #print(df_sites.sort_values(by="Vitesse_Moyenne_Sec").round(3))

        # 3. Affichage allert site lent
        df_lents = df_succes[df_succes["Temps_Reponse_Sec"] > 2.0]
        if df_lents.empty:
            print("Il n'y a pas des sites lents")
        else:
            #print(df_lents[["URL","Temps_Reponse_Sec"]].to_string(index=False))
            df_site_lents = df_lents[["URL","Temps_Reponse_Sec"]].to_string(index=False)
        
        temps_moyen = df_succes["Temps_Reponse_Sec"].mean()
        poids_moyen = df_succes["Poids_HTML_Ko"].mean()
        site_plus_rapide = df_succes.loc[df_succes["Temps_Reponse_Sec"].idxmin()]["URL"]
        temps_min = df_succes["Temps_Reponse_Sec"].min()

        rapport = (
            f"\n --- RAPPORT DE PERFORMANCE (PANDAS) ---"
            f"\n Nombre total de requêtes enregistrées          : {total_analyses}"
            f"\n Taux de réussite des requêtes                  : {taux_reussite:.1f}%"
            f"\n Temps de réponse moyen (Status 200)            : {temps_moyen:.3f} secondes"
            f"\n Poids moyen du code HTML téléchargé            : {poids_moyen:.2f} Ko"
            f"\n Site le plus rapide testé                      : {site_plus_rapide} ({temps_min:.3f}s)"
            f"\n -- Tableau du plus rapide au plus lent (GROUPBY)"
            f"\n {df_sites.sort_values(by="Vitesse_Moyenne_Sec").round(3)}"
            f"\n -- Affichage allert site lent"
            f"\n {df_site_lents}"
              
        )
        return rapport