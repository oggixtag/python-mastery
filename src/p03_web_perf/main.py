import os
import json
from contact import Contact

# Fonction pour l'affichage du menu
def afficher_menu():
    print("\n--- GESTIONNAIRE DE CONTACTS ---")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Modifier le téléphone d'un contact")
    print("4. Supprimer un contact")
    print("5. Quitter")
    return input("Choisissez une option : ")

# Préparation du chemin du fichier JSON (dossier data à la racine du projet)
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.normpath(os.path.join(base_dir, '..', '..', 'data'))
fichier_contacts = os.path.join(data_dir, 'contacts.json')

# Création du dossier data s'il n'existe pas déjà
os.makedirs(data_dir, exist_ok=True)
  
# Fonction pour sauvegarder les contacts
# Transforme les objets en dictionnaires et les écrit dans le fichier.
def sauvegarder_contacts(repertoire):
    # 1. On transforme les objets en dictionnaires
        #On lit de droite à gauche :
        #for contact in repertoire : "Prends chaque objet un par un dans ma liste."
        #contact.to_dict() : "Applique-lui sa méthode de transformation."
        #[...] : "Range tous les résultats dans une nouvelle liste."
    liste_dicts = [contact.to_dict() for contact in repertoire]

    # 2. On ouvre le fichier et on écrit dedans
    with open (fichier_contacts,"w", encoding="utf-8") as f:
        # indent=4 : Indente le JSON pour le rendre lisible par un humain
        # ensure_ascii=False : Permet d'écrire les accents correctement
        json.dump(liste_dicts, f, indent=4, ensure_ascii=False)
    
# Fonction pour charger les contacts
# Lit le fichier et transforme les dictionnaires en objets Contact.
def charger_contact():
    try:
        with open(fichier_contacts, "r", encoding="utf-8") as f:
            donnees = json.load(f)
            # On reconstruit nos objets grâce au @classmethod
            return [Contact.from_dict(d) for d in donnees]
    except (FileNotFoundError, json.JSONDecodeError):
        # Lors de premier demarrage le fichiet n'héxiste pas
        # Cela permet de demarrer à  vide, puor un experience utilisatur plus fluide
        return []

# Lancement du programme dans ce bloc
def main():

    # ÉTAPE A : Charger les données 
    repertoire = charger_contact()
    
    while True:
        # Etape B: Affichage du menu et récupération du choix...
        choix = afficher_menu()
        
        match choix:
            case "1":
                # AJOUTER UN CONTACT
                nom = input("Nom : ")
                prenom = input("Prénom : ")
                tel = input("Téléphone : ")
                email = input("Email : ")
                try:
                    # On crée l'objet (instanciation)
                    nouveau = Contact(nom, prenom, tel, email)
                    repertoire.append(nouveau)
                    
                    #Sauvergarde le contact dans json 
                    sauvegarder_contacts(repertoire)

                    print(f" {nom} {prenom} a été ajouté au répertoire.")
                except ValueError as e:
                    print(f" Erreur : {e}")

            case "2":
                # AFFICHER TOUS LES CONTACTS
                if not repertoire:
                    print("Le fichet est vide.")
                else:
                    print(f"\n Liste des contacts ({len(repertoire)}) :")
                    for contact in repertoire:
                        # On appelle la méthode de l'objet
                        contact.afficher_fiche()

            case "3":
                # MODIFIER UN TÉLÉPHONE
                
                # Recherche contact
                nom_recherche = input("Entrez le nom du contact: ")

                # Recherche de doublon sur la base du contact saisi
                #
                # Le nom de l'élément que tu gardes (au début) doit être exactement le même que celui que tu examines (après le for).
                # contacts_trouves = [	                    => On prépare une nouvelle boîte (une liste) pour ranger nos résultats.
                # contact_in_repertoire	                    => C'est l'élément final que l'on décide de "garder" et de mettre dans la boîte.
                # for contact_in_repertoire in repertoire   => On dit à Python : "Prends chaque contact un par un dans le répertoire complet".
                # if ... == ...	                            => On ne laisse passer le contact que si son nom correspond à la recherche.
                
                contacts_trouves = [
                    contact_in_repertoire 
                    for contact_in_repertoire in repertoire 
                    if contact_in_repertoire.nom.lower() == nom_recherche.lower()
                ]

                if not contacts_trouves:
                    print(f"Aucun contact trouvé au nom de '{nom_recherche}'.")

                else:
                    contact_cible = None

                    # 1. Gestion des doublons (Plusieurs occurrences trouvées)
                    if len(contacts_trouves) > 1:
                        print(f"\n {len(contacts_trouves)} contacts trouvés pour '{nom_recherche}' :")
                        
                        # Affichage des contacts trouvés avec un index 
                        for i, contact_in_repertoire in enumerate(contacts_trouves, start=1):
                            print(f"{i}. {contact_in_repertoire.nom} {contact_in_repertoire.prenom} - {contact_in_repertoire._telephone} ({contact_in_repertoire.email})")
                        
                        try:
                            choix = int(input("\n Entrez le numéro du contact à modifier : "))
                            if 1 <= choix <= len(contacts_trouves):
                                # On récupère l'objet cible via l'index choisi par l'utilisateur
                                contact_cible = contacts_trouves[choix - 1]
                            else:
                                print("Choix invalide. L'opération est annulée.")
                        except ValueError:
                            print("Erreur : Veuillez entrer un nombre entier valide.")

                    # 2. Cas idéal (Une seule occurrence trouvée)
                    else:
                        contact_cible = contacts_trouves[0]

                    # 3. Exécution de la modification si un contact a été validé
                    if contact_cible:
                        print(f"\n Modification de : {contact_cible.nom} {contact_cible.prenom} (Actuel : {contact_cible.get_telephone()})")
                        nouveau_tel = input("Entrez le nouveau numéro de téléphone : ").strip()
                        
                        if nouveau_tel:
                            # On utilise la méthode de l'objet pour mettre à jour la donnée
                            contact_cible.set_telephone(nouveau_tel)

                            #Sauvergarde le contact modifié dans json 
                            sauvegarder_contacts(repertoire)

                            print(f" Le numéro de {contact_cible.nom} a été mis à jour avec succès.")
                        else:
                            print(" Modification annulée : le numéro ne peut pas être vide.")

            case "4":

                # SUPPRESSION D'UN CONTACT
                
                # Recherche contact
                nom_recherche = input("Entrez le nom du contact: ")

                # Recherche de doublon sur la base du contact saisi
                #
                # Le nom de l'élément que tu gardes (au début) doit être exactement le même que celui que tu examines (après le for).
                # contacts_trouves = [	                    => On prépare une nouvelle boîte (une liste) pour ranger nos résultats.
                # contact_in_repertoire	                    => C'est l'élément final que l'on décide de "garder" et de mettre dans la boîte.
                # for contact_in_repertoire in repertoire   => On dit à Python : "Prends chaque contact un par un dans le répertoire complet".
                # if ... == ...	                            => On ne laisse passer le contact que si son nom correspond à la recherche.
                
                contacts_trouves = [
                    contact_in_repertoire 
                    for contact_in_repertoire in repertoire 
                    if contact_in_repertoire.nom.lower() == nom_recherche.lower()
                ]

                if not contacts_trouves:
                    print(f"Aucun contact trouvé au nom de '{nom_recherche}'.")

                else:
                    contact_cible = None

                    # 1. Gestion des doublons (Plusieurs occurrences trouvées)
                    if len(contacts_trouves) > 1:
                        print(f"\n {len(contacts_trouves)} contacts trouvés pour '{nom_recherche}' :")
                        
                        # Affichage des contacts trouvés avec un index 
                        for i, contact_in_repertoire in enumerate(contacts_trouves, start=1):
                            print(f"{i}. {contact_in_repertoire.nom} {contact_in_repertoire.prenom} - {contact_in_repertoire.get_telephone()} ({contact_in_repertoire.email})")
                        
                        try:
                            choix = int(input("\n Entrez le numéro du contact à supprimer : "))
                            if 1 <= choix <= len(contacts_trouves):
                                # On récupère l'objet cible via l'index choisi par l'utilisateur
                                contact_cible = contacts_trouves[choix - 1]
                            else:
                                print("Choix invalide. L'opération est annulée.")
                        except ValueError:
                            print("Erreur : Veuillez entrer un nombre entier valide.")

                    # 2. Cas idéal (Une seule occurrence trouvée)
                    else:
                        contact_cible = contacts_trouves[0]

                    # 3. Exécution de la modification si un contact a été validé
                    if contact_cible:                        

                        print(f"\nAttention : Vous allez supprimer {contact_cible.nom} ({contact_cible.get_telephone()}).")
                        confirmation = input("Êtes-vous sûr ? (o/n) : ").strip().lower()

                        if confirmation == 'o':
                            # Suppression de la mémoire vive
                            repertoire.remove(contact_cible)
                            
                            # Synchronisation sur le disque dur
                            sauvegarder_contacts(repertoire)
                            print(f"{contact_cible.nom} a été supprimé du répertoire.")
                        else:
                            print("Suppression annulée.")

            case "5":
                print("Au revoir !")
                break

            case _:
                print("L'option n'est pas valide, essaye encore ..")

if __name__ == "__main__":
    main()