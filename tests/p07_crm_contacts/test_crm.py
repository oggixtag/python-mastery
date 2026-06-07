import pytest
from src.p07_crm_contacts.contact import Contact

def test_initialisation_contact_valide():
    """Vérifie qu'un contact est correctement créé lorsque toutes les données sont valides."""
    # --- ARRANGE ---
    nom = "Dupont"
    prenom = "Jean"
    telephone = "0601020304"
    email = "jean.dupont@email.com"

    # --- ACT ---
    contact = Contact(nom, prenom, telephone, email)

    # --- ASSERT ---
    assert contact.nom == nom
    assert contact.prenom == prenom
    assert contact.email == email
    assert contact.get_telephone() == telephone

def test_initialisation_contact_sans_nom_leve_erreur():
    """Vérifie qu'une erreur est levée si le nom est manquant."""
    # --- ARRANGE ---
    nom_invalide = ""
    
    # --- ACT & ASSERT ---
    # On indique à pytest qu'on s'attend à ce que le bloc de code lève une ValueError
    with pytest.raises(ValueError) as exc_info:
        Contact(nom_invalide, "Jean", "0601020304", "jean.dupont@email.com")
        
    # On peut même vérifier le message d'erreur exact
    assert str(exc_info.value) == "Le nom est obligatoire"

def test_serialisation_et_deserialisation_contact():
    """Vérifie qu'un contact peut être converti en dictionnaire et reconstruit à l'identique."""
    # --- ARRANGE ---
    # 1. On crée un contact initial
    contact_origine = Contact("Dupont", "Jean", "0601020304", "jean.dupont@email.com")

    # --- ACT ---
    # 2. On le transforme en dictionnaire (Sérialisation)
    dictionnaire_contact = contact_origine.to_dict()
    
    # 3. On recrée un nouveau contact à partir de ce dictionnaire (Désérialisation)
    contact_restaure = Contact.from_dict(dictionnaire_contact)

    # --- ASSERT ---
    # On vérifie que les données du contact restauré sont strictement identiques à l'original
    assert contact_restaure.nom == contact_origine.nom
    assert contact_restaure.prenom == contact_origine.prenom
    assert contact_restaure.get_telephone() == contact_origine.get_telephone()
    assert contact_restaure.email == contact_origine.email