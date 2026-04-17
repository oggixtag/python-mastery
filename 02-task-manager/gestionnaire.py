################# Importation librairie #################
import json
import os

################# Fonctions de gestion des taches #################

# Fonction d'affichage des taches
def affichage(ma_liste):
    
    if ma_liste:
        # Le code s'exécute si la liste n'est pas vide
        print('Iteration sur la liste des taches..')
        for index, tache in enumerate(ma_liste):
            print(f"Tâche [{index}]: {tache['nom']} - Statut: {tache['statut']}")
    else:
        print("La liste des taches est vide.")

# Fonction de sauvegarde des taches dans un fichier JSON
def sauvegarder(ma_liste, chemin_fichier):
    with open(chemin_fichier, 'w', encoding='utf-8') as fichier:
        # indent=4 rend le fichier JSON lisible par un humain en ajoutant des espaces et des sauts de ligne. 
        # ensure_ascii=False permet de conserver les caractères non ASCII (comme les accents) dans le fichier JSON au lieu de les échapper avec des séquences d'échappement Unicode.
        json.dump(ma_liste, fichier,indent=4, ensure_ascii=False)

#Fonction de recherche d'une tache dans la liste des taches
def recherche(ma_liste, nom_tache):
    resultat = []
    nom_tache = nom_tache.lower()
    for tache in ma_liste:
        if nom_tache in tache['nom'].lower():
            resultat.append(tache)
    return resultat

################# Programme principal #################

#On prépare le chemin du fichier JSON (dossier data a la racine du projet)
base_dir = os.path.dirname(__file__)
data_dir = os.path.normpath(os.path.join(base_dir, 'data'))
#print(f"Chemin du dossier data : {data_dir}")
fichier_taches = os.path.join(data_dir, 'taches.json')
#Création du dossier data s'il n'existe pas déjà
os.makedirs(data_dir, exist_ok=True)

#On vérifie si le fichier JSON existe déjà
if os.path.exists(fichier_taches):
    with open(fichier_taches, 'r', encoding='utf-8') as fichier:
        taches = json.load(fichier)
else:
    #Si le fichier n'existe pas, on commence par un liste vide
    print("Création d'une liste de taches")
    taches = []
    print(type(taches))

print("Création d'un dictionnaire de statuts possibles pour une tache")
#statut_tache = {}
#print(type(statut_tache))

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
print(type(statut_tache))


#Boucle principale du programme pour permettre d'ajouter, mettre à jour et supprimer des tâches de manière dynamique
while True:

    #Action à effectuer
    action = input("Que voulez-vous faire ? (ajouter [a], mettre à jour [m], supprimer [s], afficher [f], quitter [q], rechercher [r]) : ")

    if action == 'r':
        #On demande à l'utilisateur la tache à rechercher
        v_tache_a_rechercher = input("Nom de la tâche à rechercher : ")
        resultat_recherche = recherche(taches, v_tache_a_rechercher)
        if resultat_recherche:
            print("Résultats de la recherche :")
            affichage(resultat_recherche)
        else:
            print(f"🔍 Aucun résultat pour '{v_tache_a_rechercher}'.")

    elif action == 'a':

        #On demande à l'utilisateur de saisir une tache
        v_nouvelle_tache = input("Nom de la novelle tâche : ")
 
        #Sauvegarde de la tache saisie et insertion dans la liste des taches dans le fichier json
        nouvelle_tache = {"nom": v_nouvelle_tache, "statut": v_statut_tache_a_faire}
        taches.append(nouvelle_tache)
        sauvegarder(taches, fichier_taches)

        print("Tache ajoutée avec succès !")

    elif action == 'm':

        if not taches:
            print("La liste des taches est vide. Aucune tache à mettre à jour.")
            continue #pour remonter directement au début de la boucle while

        print("Affichage des taches avant la mise à jour")
        affichage(taches)

        #Bloc de mise à jour du statut d'une tache
        try:
            #On demande à l'utilisateur de saisir l'index de la tache à mettre à jour
            v_index_tache_a_mettre_a_jour = int(input("Index de la tâche à mettre à jour : "))

            print("Affichage des statuts possibles pour une tache:")
            for index, statut in enumerate(statut_tache):
                print(f"Statut [{index}]: {statut}")
            v_nouveau_statut = input("Nouveau statut de la tâche : ") 

            if v_nouveau_statut not in statut_tache.values():
                raise ValueError("Statut invalide. Veuillez choisir parmi les statuts possibles.")
            
            taches[v_index_tache_a_mettre_a_jour]['statut'] = v_nouveau_statut
            sauvegarder(taches, fichier_taches)
        except IndexError:
            print("Index de tâche invalide. Veuillez entrer un index valide.")
        except ValueError as e:
            print(f"Erreur : {e}. On recommence.")
            continue #pour remonter directement au début de la boucle while

        print("Tache mise à jour avec succès !")
        affichage(taches)

    elif action == 's':

        if not taches:
            print("La liste des taches est vide. Aucune tache à mettre à supprimer.")
            continue #pour remonter directement au début de la boucle while

        print("Affichage des taches avant la mise à jour")
        affichage(taches)
        
        #Suppression 
        try:
            #On demande à l'utilisateur de saisir l'index de la tache à supprimer
            v_index_tache_a_supprimer = int(input("Index de la tâche à supprimer : "))

            del taches[v_index_tache_a_supprimer]
            sauvegarder(taches, fichier_taches)
        except IndexError:
            print("Index de tâche invalide. Veuillez entrer un index valide.")
            continue #pour remonter directement au début de la boucle while
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'index de la tâche à supprimer. On recommence.")
            continue #pour remonter directement au début de la boucle while

        print("Tache supprimée avec succès !")
        affichage(taches)

    elif action == 'f':
        affichage(taches)

    elif action == 'q':
        print("Au revoir !")
        break
