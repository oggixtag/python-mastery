#Boucle dynamique pour la saisie et validation des entrées
while True:

    resultat = None

    #Saisie du Nombre A
    try:
        nombre_a = float(input("Entrez le premier nombre : "))
        print(f"premier nombre :{nombre_a}")
    except ValueError:
        print("Veuillez entrer un nombre valide. On recommence.")
        continue

    #Constritution du resultat
    resultat = f"{nombre_a}"

    #saisi de l'operatation
    try:
        operateur = input("Entrez l'operation (+, -, *, /) : ")
        if operateur not in ['+', '-', '*', '/']:
            raise ValueError("Opérateur invalide")
    except ValueError:
        print("Opérateur invalide. Veuillez entrer +, -, * ou /. On recommence.")
        continue

    #Concatenation avec l'operation
    resultat = f"{resultat} {operateur}"

    #Saisie du Nombre B
    try:
        nombre_b = float(input("Entrez le deuxième nombre : "))
        print(f"deuxième nombre :{nombre_b}")
    except ValueError:
        print("Veuillez entrer un nombre valide. On recommence.")
        continue

    #Concatenation de l'operation avec le nombre B
    resultat = f"{resultat} {nombre_b}"

    print(f"Expression à évaluer : {resultat}")

    #bloc de calcul de l'operation
    #séparation de l'action (le calcul) de la réussite (l'affichage)
    try:
        if (operateur == '+'):
            resultat = nombre_a + nombre_b
        elif (operateur == '-'):
            resultat = nombre_a - nombre_b
        elif (operateur == '*'):
            resultat = nombre_a * nombre_b
        elif (operateur == '/'):
            resultat = nombre_a / nombre_b
    #exceptions de la plus spécifique à la plus générale.
    except ZeroDivisionError:
        print("Erreur : Division par zéro. On recommence.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}. On recommence.")
        continue    #pour remonter directement au début de la boucle while
    
    else:
        #resulta operataion
        print(f"Résultat : {resultat}")

        #Demande de refaire une operation
        autre_operation = input("Voulez-vous effectuer une autre opération ? (y/n) : ").lower()
        if autre_operation == 'n':
            print("Au revoir !")
            break





