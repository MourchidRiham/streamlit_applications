Voici un fichier **`README.md`** complet et bien structuré que tu peux copier/coller dans ton projet :

---

````markdown
# 📊 Tableau de Bord des Performances Étudiantes

## 🎯 Présentation du Projet

Ce projet a pour objectif de créer une application web interactive développée avec **Streamlit** permettant d'analyser les **facteurs de performance des étudiants** à partir d’un fichier CSV. L'application utilise **DuckDB** pour le stockage et les requêtes SQL, et propose des **visualisations dynamiques** pour mieux comprendre les données.

Ce tableau de bord permet aux utilisateurs d’explorer les données selon différents critères (genre, type d'école, niveau, etc.) et de visualiser quatre indicateurs clés de performance (KPI).

---
Voici une **suggestion claire de la structure du projet** que tu peux inclure à la fin de ton `README.md`, sous forme de section intitulée **Structure du projet** :

---

```markdown
## 🗂️ Structure du Projet

```

student-performance-dashboard/
│
├── app.py                            # Fichier principal Streamlit (application)
│
├── requirements.txt                  # Dépendances du projet
│
├── README.md                         # Documentation du projet
│
├── data/
│   └── StudentPerformanceFactors.csv # Fichier de données (exemple de CSV)
│
├── utils/
│   ├── duckdb\_utils.py               # Fonctions de chargement et requêtes DuckDB
│   └── visualizations.py             # Fonctions de visualisation des KPI
│
└── venv/                             # Environnement virtuel Python (à ne pas versionner)

```

---

📝 **Remarques :**
- Le dossier `data/` contient tes fichiers CSV à analyser.
- Le dossier `utils/` contient les scripts Python séparés pour organiser la logique métier.
- `app.py` est le point d’entrée de l’application Streamlit.


## ⚙️ Instructions d’installation et d’exécution

### 1. Cloner le dépôt

```bash
git clone https://github.com/MourchidRiham/streamlit_applications.git
cd streamlit_applications
````

### 2. Créer et activer un environnement virtuel

Windows :

```bash
python -m venv venv
.\venv\Scripts\activate
```

Mac/Linux :

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l’application

```bash
streamlit run app.py
```

---

## 🧠 Fonctionnalités

* 📂 Téléversement d’un fichier CSV contenant les performances étudiantes.
* 🧹 Nettoyage automatique des données (valeurs manquantes, doublons, renommage de colonnes).
* 📊 Visualisations interactives : histogrammes, barres, diagrammes en anneau, violin plots.
* 📈 Calcul de 4 KPI principaux :

  * Note moyenne
  * Taux de réussite
  * Taux d’échec
  * Nombre total d’étudiants
* 🎛️ Filtres dynamiques par :

  * Genre
  * Niveau scolaire
  * Sujet
  * Type d’école
  * Accès à Internet
  * Niveau d’éducation des parents
  * Sessions de tutorat
  * Niveau de motivation

---

## 👥 Répartition des tâches

| Membre             | Tâches principales                                                                  |
| ------------------ | ----------------------------------------------------------------------------------- |
| **MOURCHID Riham** | 🔧 Développement backend : intégration DuckDB, nettoyage, logique de filtrage       |
| **EL HAFA Hajar**  | 🎨 Développement frontend : interface Streamlit, visualisations, style et ergonomie |

---

## 🛠️ Difficultés rencontrées

* ⚠️ **Problèmes d’importation** au départ : structure de projet mal organisée (`duckdb_utils`, `visualizations`).
* 🔍 **Colonnes non standardisées** dans le CSV : noms avec espaces, case incohérente, doublons.
* 💡 **Compréhension des outils** (DuckDB, Streamlit CLI, PowerShell) pour déploiement local et GitHub.
* 🐛 Bugs intermittents liés à des erreurs de typage dans les colonnes et des fichiers manquants.
* 🔐 Problèmes avec GitHub CLI : ajout manuel du chemin d’accès système, gestion du push initial.

---

## ✅ Résultat

L'application est désormais **fonctionnelle**, **stable** et **intuitive**, offrant une expérience fluide pour l’analyse des performances scolaires sur base de données CSV.

---

*Projet réalisé dans le cadre de notre formation — 2025.*
*© MOURCHID Riham & EL HAFA Hajar*
