################# Importation librairie #################
from analyzer import WebAnalyzer

################# Fonctions #################
def afficher_menu():
    print("\n--- WEB PERF ANALYZER (DATA EDITION) ---")
    print("1. Analyser une nouvelle URL")
    print("2. Générer le rapport statistique (Pandas)")
    print("3. Quitter")
    return input("Choisissez une option : ").strip()

################# Programme principal #################
def main():
    analyzer = WebAnalyzer()

    while True:
        choix = afficher_menu()

        match choix:
            case "1":
                url = input("\nEntrez l'URL à analyser (ex: https://example.com) : ").strip()
                if not url.startswith(("http://", "https://")):
                    print("Erreur : L'URL doit commencer par http:// ou https://")
                    continue
                
                print(f"Analyse et enregistrement CSV en cours pour : {url}...")
                res = analyzer.analyser_site(url)
                
                if res["Statut_HTTP"] == 200:
                    print(f"Succès ! Temps : {res['Temps_Reponse_Sec']}s | Taille : {res['Poids_HTML_Ko']} Ko")
                else:
                    print(f"Échec du test (Statut {res['Statut_HTTP']}). Erreur enregistrée : {res['Erreurs']}")

            case "2":
                print(analyzer.generer_rapport_statistique())

            case "3":
                print("Fermeture de l'analyseur de données. Au revoir !")
                break

            case _:
                print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()