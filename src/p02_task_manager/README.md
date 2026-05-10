## 📝 Description
Ce script Python permet de gérer un cycle de vie complet de tâches (CRUD). Contrairement au premier projet, les données ne sont plus volatiles : elles sont sauvegardées et chargées automatiquement depuis un fichier JSON, permettant de conserver sa liste d'une session à l'autre.

## ✨ Fonctionnalités
- Gestion Complète (CRUD) :
	- Ajouter : Création de nouvelles tâches avec un statut initial "à faire".
	- Afficher : Visualisation claire de la liste avec indexation.
	- Mettre à jour : Modification dynamique du statut avec validation des entrées.
	- Supprimer : Retrait sécurisé de tâches par leur index.
- Recherche Intelligente : Moteur de recherche insensible à la casse permettant de retrouver des tâches par des mots-clés partiels.
- Persistance des Données : Sauvegarde automatique dans un fichier taches.json structuré avec indentation pour une meilleure lisibilité.
- Robustesse & Sécurité :
	- Gestion rigoureuse des erreurs d'index (IndexError) et de type (ValueError).
	- Vérification systématique de l'existence des dossiers et fichiers via le module os.
	- Encodage en UTF-8 pour le support intégral des caractères accentués.

## 🚀 Installation et Utilisation
- Cloner le dépôt :

```bash
git clone https://github.com/oggixtag/python-mastery.git
```

- Accéder au dossier :

```bash
cd 02-task-manager
```

- Lancer l'application :

```bash
python gestionnaire.py
```

## 🛠️ Concepts Techniques Appliqués
- Structures de données : Listes de dictionnaires.
- Modularité : Utilisation de fonctions (def) pour l'affichage, la sauvegarde et la recherche.
- Gestion des fichiers : Utilisation des modules json et os pour la persistance.
- Logique de programmation : Boucles while, conditions if/elif/else, et gestion d'exceptions try/except.

## 📂 Structure du projet
- gestionnaire.py : Logique principale de l'application.
- data/ : Dossier généré automatiquement pour le stockage.
- taches.json : Fichier de sauvegarde des données.
- README.md : Documentation du projet.

## 👤 Auteur

**Andrea Moriggi** - *Développeur Web & Web Mobile*
- **LinkedIn** : [Profil LinkedIn](https://www.linkedin.com/in/andrea-moriggi-65b73935/)
- **Portfolio / GitHub** : https://github.com/oggixtag

---

Projet réalisé pour valider les compétences en manipulation de fichiers et persistance de données en Python.