#Création de la liste avec un dictionnaire
taches = {}
print(type(taches))

#Status par default d'une tache
v_statut_tache_a_faire = 'à faire'
v_statut_tache_en_cours = 'en cours'
v_statut_tache_termine = 'terminé'

#Liste des statuts possibles d'une tache
statut_tache = [v_statut_tache_a_faire, v_statut_tache_en_cours, v_statut_tache_termine]

print("Iteration sur le statuts possibles d'une tache..")
for index, statut in enumerate(statut_tache):
    print(f"Statut [{index}]: {statut}")

#if taches.items() == {}:
#    print("Aucune tâche n'est enregistrée.")

taches = [
    {"nom": "Acheter du pain", "statut": "à faire"},
    {"nom": "Coder le projet", "statut": "en cours"}
]

print('Iteration sur la liste des taches..')
for index, tache in enumerate(taches):
    print(f"Tâche taches [{index}]: {tache['nom']} - Statut: {tache['statut']}")
    #sinon print(tache['nom'])

#Boucle principale du programme pour permettre d'ajouter, mettre à jour et supprimer des tâches de manière dynamique
while True:

    #Action à effectuer
    action = input("Que voulez-vous faire ? (ajouter, mettre à jour, supprimer, afficher, quitter) : ")

    if action == 'ajouter':
        #On demande à l'utilisateur de saisir une tache
        v_nouvelle_tache = input("Nom de la novelle tâche : ")

        #Ajout de la tache saisié par l'utilisateur
        taches.append({"nom": v_nouvelle_tache, "statut": v_statut_tache_a_faire})

    elif action == 'mettre à jour':
        #Affichage des statuts possibles pour la tache à mettre à jour
        print("Statuts possibles :")
        for index, statut in enumerate(statut_tache):
            print(f"Statut [{index}]: {statut}")
        v_nouveau_statut = input("Nouveau statut de la tâche : ")

        try:
            if v_nouveau_statut not in statut_tache:
                raise ValueError("Statut invalide. Veuillez choisir parmi les statuts possibles.")
        except ValueError as e:
            print(f"Erreur : {e}. On recommence.")
            continue    #pour remonter directement au début de la boucle while

        for index, tache in enumerate(taches):
            print(f"Tâche taches [{index}]: {tache['nom']} - Statut: {tache['statut']}")

        #Mise à jour du statut d'une tache
        v_index_tache_a_mettre_a_jour = int(input("Index de la tâche à mettre à jour : "))

        taches[v_index_tache_a_mettre_a_jour]['statut'] = v_nouveau_statut

    elif action == 'supprimer':
        #Suppression d'une tache
        v_index_tache_a_supprimer = int(input("Index de la tâche à supprimer : "))
        del taches[v_index_tache_a_supprimer]

        for index, tache in enumerate(taches):
            print(f"Tâche taches [{index}]: {tache['nom']} - Statut: {tache['statut']}")

    elif action == 'afficher':
        for index, tache in enumerate(taches):
            print(f"Tâche taches [{index}]: {tache['nom']} - Statut: {tache['statut']}")

    elif action == 'quitter':
        print("Au revoir !")
        break