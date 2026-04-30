from contact import Contact

# 1. Création du répertoire (notre base de données temporaire)
repertoire = []



#lancement du programme dans ce bloc
def main():

    # 2. Instanciation de quelques contacts
    try:
        # 3. Ajout à la liste
        repertoire.append(Contact("Jean", "Dupont", "123456789", "[EMAIL_ADDRESS]"))
        repertoire.append(Contact("Marie", "Martin", "987654321", "[EMAIL_ADDRESS]"))
        repertoire.append(Contact("Pierre", "Durand", "123456789", "[EMAIL_ADDRESS]"))
        repertoire.append(Contact("Jeanne", "Dubois", "987654321", "[EMAIL_ADDRESS]"))
        repertoire.append(Contact("Paul", "Martin", "123456789", "[EMAIL_ADDRESS]"))
 
        try:
            repertoire.append(Contact("Marc", "", "123456789", "marc@email.com"))
        except ValueError as e:
            print(f"Erreur de saisie (Marc) : {e}")

        # 4. Affichage de tous les contacts
        print("\n--- LISTE DES CONTACTS ---")
        for contact in repertoire:
            contact.afficher_fiche()

    except Exception as e:
        print(f"Erreur : {e}")
    
    finally:
        print("Fin du programme")

if __name__ == "__main__":
    main()
