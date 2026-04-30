from contact import Contact

def afficher_menu():
    print("\n--- GESTIONNAIRE DE CONTACTS ---")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Modifier le téléphone d'un contact")
    print("4. Quitter")
    return input("Choisissez une option : ")

#lancement du programme dans ce bloc
def main():

    # 1. Création du répertoire (notre base de données temporaire)
    repertoire = []
    
    while True:
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
                    print(f" {nom} {prenom} a été ajouté au répertoire.")
                except ValueError as e:
                    print(f" Erreur : {e}")

            case "2":
                # AFFICHER TOUS LES CONTACTS
                if not repertoire:
                    print("Le répertoire est vide.")
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

                            print(f" Le numéro de {contact_cible.nom} a été mis à jour avec succès.")
                        else:
                            print(" Modification annulée : le numéro ne peut pas être vide.")

            case "4":
                print("Au revoir !")
                break

            case _:
                print("L'option n'est pas valide, essaye encore ..")

if __name__ == "__main__":
    main()