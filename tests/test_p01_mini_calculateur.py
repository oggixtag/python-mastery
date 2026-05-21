import pytest
from src.p01_mini_calculateur.calculateur import ajouter
from src.p01_mini_calculateur.calculateur import diviser
from src.p01_mini_calculateur.calculateur import soustraire
from src.p01_mini_calculateur.calculateur import multiplier

def test_ajouter_nombre_positif():
    assert ajouter(2, 2) == 4 

def test_ajouter_nombre_non_numerique_gere_err():
    with pytest.raises(TypeError):
        assert ajouter("2", 2) == 4 

def test_diviser_nombre_positif():
    assert diviser(4, 2) == 2

def test_diviser_nombre_par_zero_gere_err():
    with pytest.raises(ValueError):
        assert diviser(10, 0) == 4 

def test_soustraire_nombres_positifs():
    assert soustraire(10, 4) == 6

def test_multiplier_avec_decimaux():
    # Tester la multiplication avec un nombre décimal (float)
    assert multiplier(2.5, 2) == 5.0

def test_ajouter_decimaux_evite_bug_arrondi():
    # En Python, 0.1 + 0.2 vaut parfois 0.30000000000000004
    # pytest.approx permet de gérer proprement les arrondis des floats
    assert ajouter(0.1, 0.2) == pytest.approx(0.3)