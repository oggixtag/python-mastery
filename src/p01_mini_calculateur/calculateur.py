################# Fonctions de gestion des taches #################
def ajouter(a: int | float , b: int | float) -> int | float :
    return a + b

# Python renvoie presque toujours un nombre décimal (float), même si on divise 10 par 2
def diviser(a: int | float , b: int | float) -> float :
    if b == 0:
        raise ValueError("le deuxième nombre ne peux pas être égale à 0")
    else:
        return a / b

def soustraire(a: int | float , b: int | float) -> int | float :
    return a - b

def multiplier(a: int | float , b: int | float) -> float :
    return a * b