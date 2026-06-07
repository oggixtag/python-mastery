## P07 - Gestionnaire de contacts (CLI)

Ce module est une application console pour gerer un repertoire de contacts. L'utilisateur peut ajouter, lister, modifier et supprimer des contacts. Les donnees sont sauvegardees en JSON dans un dossier data a la racine du projet pour conserver l'etat entre les executions.

### Fonctionnalites

- Ajouter un contact (nom, prenom, telephone, email)
- Afficher tous les contacts
- Modifier le telephone d'un contact (gestion des doublons par nom)
- Supprimer un contact (confirmation avant suppression)
- Persistance des donnees en JSON

### Structure du module

```text
python-mastery/
├── src/
│   └── p07_crm_contacts/
│       ├── contact.py
│       └── main.py
└── tests/
    └── p07_crm_contacts/
        ├── __init__.py
        └── test_contact.py       # Le fichier de tests que nous allons créer
```

### Utilisation

1) Lancer le programme via main.py
2) Suivre le menu interactif
3) Les contacts sont stockes dans data/contacts.json

### Notes techniques

- Le fichier JSON est cree automatiquement si besoin
- En cas de fichier absent ou invalide, le programme demarre avec un repertoire vide
