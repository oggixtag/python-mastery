################# Fonctions de gestion des taches #################
#
# #Fonction d'affichage des taches
def affichage(ma_liste):
    
    if ma_liste:
        # Le code s'exécute si la liste n'est pas vide
        print('Iteration sur la liste des taches..')
        for index, tache in enumerate(ma_liste):
            print(f"Tâche taches [{index}]: {tache['nom']} - Statut: {tache['statut']}")
    else:
        print("La liste des taches est vide.")

################# Programme principal #################
print("Création d'un dictionnaire de statuts possibles pour une tache")
statut_tache = {}
print(type(statut_tache))

#Status par default d'une tache
v_statut_tache_a_faire = 'à faire'
v_statut_tache_en_cours = 'en cours'
v_statut_tache_termine = 'terminé'

#Dictionnaire des statuts possibles d'une tache
statut_tache = {
    'a faire': v_statut_tache_a_faire,
    'en cours': v_statut_tache_en_cours,
    'terminé': v_statut_tache_termine
}


print("Création d'une liste de taches")
taches = []
print(type(taches))


#Boucle principale du programme pour permettre d'ajouter, mettre à jour et supprimer des tâches de manière dynamique
while True:

    #Action à effectuer
    action = input("Que voulez-vous faire ? (ajouter [a], mettre à jour [m], supprimer [s], afficher [r], quitter [q]) : ")

    if action == 'a':

        #taches = [
        #      {"nom": "Acheter du pain", "statut": "à faire"},
        #      {"nom": "Coder le projet", "statut": "en cours"}
        #]

        #On demande à l'utilisateur de saisir une tache
        v_nouvelle_tache = input("Nom de la novelle tâche : ")

        #Ajout de la tache saisié par l'utilisateur
        taches.append({"nom": v_nouvelle_tache, "statut": v_statut_tache_a_faire})

        print("Tache ajoutée avec succès !")

    elif action == 'm':

        print("Affichage des taches avant la mise à jour")
        affichage(taches)

        #Bloc de mise à jour du statut d'une tache
        try:        
            v_index_tache_a_mettre_a_jour = int(input("Index de la tâche à mettre à jour : "))

            print("Affichage des statuts possibles pour une tache:")
            for index, statut in enumerate(statut_tache):
                print(f"Statut [{index}]: {statut}")
            v_nouveau_statut = input("Nouveau statut de la tâche : ") 

            if v_nouveau_statut not in statut_tache.values():
                raise ValueError("Statut invalide. Veuillez choisir parmi les statuts possibles.")
            
            taches[v_index_tache_a_mettre_a_jour]['statut'] = v_nouveau_statut
        except IndexError:
            print("Index de tâche invalide. Veuillez entrer un index valide.")
        except ValueError as e:
            print(f"Erreur : {e}. On recommence.")
            continue #pour remonter directement au début de la boucle while

        print("Tache mise à jour avec succès !")
        affichage(taches)

    elif action == 's':

        print("Affichage des taches avant la mise à jour")
        affichage(taches)
        
        #Suppression 
        try:
            v_index_tache_a_supprimer = int(input("Index de la tâche à supprimer : "))
            del taches[v_index_tache_a_supprimer]
        except IndexError:
            print("Index de tâche invalide. Veuillez entrer un index valide.")
            continue #pour remonter directement au début de la boucle while
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'index de la tâche à supprimer. On recommence.")
            continue #pour remonter directement au début de la boucle while

        print("Tache supprimée avec succès !")
        affichage(taches)

    elif action == 'r':
        affichage(taches)

    elif action == 'q':
        print("Au revoir !")
        break
