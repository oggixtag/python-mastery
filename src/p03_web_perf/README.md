# 📊 Web Perf Analyzer (Data Edition) - Projet 03

Ce module fait partie du dépôt `python-mastery`. C'est une application axée sur la **Data (manipulation de fichiers CSV et analyse statistique avec Pandas)**. Elle permet de mesurer les performances de chargement de pages web, d'historiser les résultats et de générer des rapports détaillés.

## 🎯 Objectifs du Projet

* **Collecte de données** : Envoyer des requêtes HTTP pour mesurer le temps de réponse et le poids HTML de différentes URL.
* **Persistance (CSV)** : Stocker chaque analyse dans un fichier de données centralisé.
* **Analyse de données (Pandas)** : Utiliser la puissance de la bibliothèque Pandas pour calculer des moyennes globales, regrouper les données par site (`groupby`) et filtrer les anomalies (alertes de lenteur).

---

## 📁 Structure du Projet

```text
python-mastery/
├── data/
│   └── web_perf_metrics.csv       # Base de données CSV générée automatiquement
├── src/
│   └── p03_web_perf/
│       ├── __init__.py            # Initialisation du package
│       ├── analyzer.py            # Logique d'analyse et calculs Pandas
│       ├── main.py                # Interface utilisateur en console
│       └── README.md              # Documentation du projet (ce fichier)
├── tests/
│   └── p03_web_perf/
│       ├── __init__.py            # Package de tests pour le projet 03
│       └── test_analyzer.py       # Tests unitaires de l'analyseur
└── requirements.txt               # Dépendances du projet (Pandas, Numpy, etc.)
```
---

## 🛠️ Installer les dépendances

Le projet s'exécute dans un environnement virtuel Python isolé `(venv)` pour garantir la stabilité des dépendances (notamment Pandas).

1. **Activer l'environnement virtuel** :
   ```powershell
   # Sur Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   
   ```

   ```bash
   # Sur Linux/Mac (Bash)
   source venv/bin/activate
   ```

---

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Utilisation
Une fois l'environnement activé, lancez l'application principale depuis la racine du dépôt :

```bash
python src/p03_web_perf/main.py
```

---

## 📋 Fonctionnalités du Menu

1. **Analyser une nouvelle URL** : Saisissez une adresse complète (ex: https://www.python.org). Le script calcule ses métriques, détecte les éventuelles erreurs HTTP ou réseau, et ajoute une nouvelle ligne dans le dataset en temps réel.

2. **Générer le rapport statistique (Pandas)** : Analyse le fichier CSV complet pour afficher :

   - Le taux de réussite global des requêtes (pourcentage de codes HTTP 200).
   - Un tableau croisé et trié par site (groupby) incluant la vitesse moyenne, le nombre total de tests et le temps de réponse maximum enregistré pour chaque domaine.
   - Une section d'alertes critiques qui isole automatiquement les requêtes trop lentes ayant dépassé le seuil d'exigence fixé à 2.0 secondes.

3. **Quitter** : Ferme proprement l'analyseur de données.

---

## 📊 Métriques Enregistrées (Dataset)

À chaque analyse, le moteur exporte les données vers le fichier data/web_perf_metrics.csv sous les colonnes suivantes :

- Date : Horodatage précis de la requête (AAAA-MM-JJ HH:MM:SS).
- URL : L'adresse absolue du site web testé.
- Statut_HTTP : Le code de retour du serveur (ex: 200 pour un succès, 404 pour introuvable, 0 pour une erreur réseau).
- Temps_Reponse_Sec : Le temps total d'exécution de la requête en secondes (arrondi à 3 décimales).
- Poids_HTML_Ko : La taille du code source de la page téléchargée en kilo-octets.
- Erreurs : Message descriptif de l'anomalie en cas d'échec (ou "Aucune" si succès).

---

## ✅ Tests

Les tests du projet 03 sont déjà présents dans `tests/p03_web_perf/` et couvrent l'initialisation de l'analyseur ainsi que le calcul des indicateurs principaux à partir d'un CSV de test.

Commande de validation utilisée :

```bash
pytest .\tests\p03_web_perf\test_analyzer.py
```

Résultat observé : `2 passed`.
