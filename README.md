
# 🚀 Python Mastery : Le Cursus 105touches

> **"L'art du digital, touche après touche."** Ce repository retrace ma montée en compétence sur l'écosystème Python à travers 7 projets structurants, allant des bases de l'algorithmique à l'automatisation industrielle.

-----

## 📊 Ma Progression

| Étape | Projet | Focus Technique | Statut |
| :--- | :--- | :--- | :--- |
| 1 | **Mini-Calculateur** | Logique & Exceptions | ✅ Terminé |
| 2 | **Task Manager JSON** | Structures de données | ✅ Terminé |
| 3 | **Web Perf Analyzer** | Data (CSV/Pandas) | ✅ Terminé |
| 4 | **Headless CMS API** | Flask & REST | 🔄 En cours |
| 5 | **Auto-Reporting Pro** | Automatisation & APIs | ⏳ À venir |
| 6 | **Dashboard Stratégique** | Architecture & Tests | ⏳ À venir |
| 7 | **CRM Contacts** | Gestion de base de données | 🔄 En cours |

-----

## 🛠️ Détail des Projets

### [01-mini-calculateur](./src/p01_mini_calculateur)

Application console robuste gérant les opérations arithmétiques et la validation des entrées.

  * **Objectif :** Maîtrise des conditions, boucles et gestion d'erreurs (`try/except`).

### [02-task-manager](./src/p02_task_manager)

Outil de gestion de tâches avec persistance des données.

  * **Objectif :** Manipulation de dictionnaires complexes et sérialisation JSON.

### [03-web-perf-analyzer](./src/p03_web_perf)

Analyseur de logs et de données SEO pour l'optimisation stratégique.

  * **Objectif :** Nettoyage de données (Cleaning) et calculs statistiques.

### [04-headless-cms-api](./src/p04_headless_cms_api)

API REST permettant de gérer des services et des contenus web.

  * **Objectif :** Architecture Web, routes HTTP et logique CRUD.

### [05-auto-reporting](./src/p05_auto_reporting)

Générateur automatisé de rapports PDF/Excel croisant plusieurs sources de données.

  * **Objectif :** Intégration de bibliothèques tierces et automatisation métier.

### [06-strategic-dashboard](./src/p06_strategic_dashboard)

Projet "Portfolio" unifiant les briques précédentes dans une architecture modulaire.

  * **Objectif :** Tests unitaires (`pytest`), documentation technique et qualité de code professionnelle.

### [07-crm-contacts](./src/p07_crm_contacts)

Application console de gestion de contacts avec ajout, modification, suppression et persistance JSON.

  * **Objectif :** Consolider la programmation orientée objet, la sérialisation JSON et la gestion d'un état local réutilisable.

-----

## 🧪 Tests

Le dépôt contient des tests unitaires pour le projet 03 dans [tests/p03_web_perf](tests/p03_web_perf). Ils valident l'initialisation de l'analyseur et le calcul des indicateurs à partir d'un CSV de test.

Commande de vérification utilisée :

```bash
pytest .\tests\p03_web_perf\test_analyzer.py
```

Résultat observé : `2 passed`.

-----

## ⚙️ Installation & Utilisation

Pour explorer l'un des projets, clonez le dépôt et créez un environnement virtuel :

```bash
# Clonage du repository
git clone https://github.com/votre-compte/python-mastery.git

# Accès au dossier
cd python-mastery

# Création de l'environnement virtuel
python -m venv venv

# Activation (Windows)
.\venv\Scripts\activate

# Activation (macOS/Linux)
source venv/bin/activate
```

Chaque sous-dossier contient son propre fichier `requirements.txt` pour installer les dépendances spécifiques.

-----

## 👨‍💻 À propos

**Andrea MORIGGI** - Développeur Web & Mobile  
*Expertise en digitalisation, automation et performance stratégique.* [LinkedIn](https://www.linkedin.com/in/andrea-moriggi-65b73935/?locale=fr_FR) | [Portfolio](https://www.google.com/search?q=votre-lien)

-----
## 📜 Licence

Ce dépôt est distribué sous licence MIT. Voir le fichier [LICENSE](LICENSE).