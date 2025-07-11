import streamlit as st
import pandas as pd
import duckdb
from utils.duckdb_utils import load_data_into_duckdb, query_kpis
from utils.visualizations import plot_kpi_charts

# Configuration de la page
st.set_page_config(page_title="Tableau de Bord des Performances Étudiantes", layout="wide")
st.title("📊 Tableau de Bord des Performances Étudiantes")

# Téléversement du fichier CSV
uploaded_file = st.file_uploader("📂 Téléversez un fichier CSV contenant les performances étudiantes", type=["csv"])

if uploaded_file:
    # Lecture des données
    df = pd.read_csv(uploaded_file)

    # Nettoyage des noms de colonnes
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Suppression des doublons
    initial_shape = df.shape
    df.drop_duplicates(inplace=True)
    if initial_shape[0] - df.shape[0] > 0:
        st.info(f"🔍 {initial_shape[0] - df.shape[0]} doublon(s) supprimé(s)")

    # Traitement des valeurs manquantes
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    if not missing_values.empty:
        st.warning("⚠️ Valeurs manquantes détectées :")
        st.write(missing_values)
        for col in missing_values.index:
            if df[col].dtype in ['float64', 'int64']:
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
        st.success("✅ Valeurs manquantes traitées automatiquement.")
    else:
        st.success("✅ Aucune valeur manquante détectée.")

    # Aperçu des données
    st.write("### 🧾 Aperçu des données nettoyées", df.head())

    # Connexion DuckDB
    conn = duckdb.connect(database=':memory:')
    load_data_into_duckdb(conn, df)

    # Filtres dynamiques
    st.sidebar.header("🎯 Filtres dynamiques")
    filters = {}
    filter_columns = [
        'Gender',
        'Educational_Stage',
        'Topic',
        'School_Type',
        'Internet_Access',
        'Parental_Education_Level',
        'Tutoring_Sessions',
        'Motivation_Level'
    ]

    for col in filter_columns:
        if col in df.columns:
            options = df[col].dropna().unique().tolist()
            selected = st.sidebar.multiselect(f"Filtrer par {col}", options=options, default=options)
            filters[col] = selected

    # Application des filtres
    filtered_df = df.copy()
    for col, selected in filters.items():
        filtered_df = filtered_df[filtered_df[col].isin(selected)]

    # Mise à jour de DuckDB avec les données filtrées
    conn.unregister('student_data')
    conn.register('student_data', filtered_df)

    # KPI
    kpis = query_kpis(conn)

    # Affichage des KPI
    st.subheader("📈 Indicateurs Clés de Performance (KPI)")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Note Moyenne", f"{kpis['average_grade']:.2f}")
    col2.metric("Taux de Réussite", f"{kpis['pass_rate']:.2f}%")
    col3.metric("Taux d'Échec", f"{kpis['fail_rate']:.2f}%")
    col4.metric("Étudiants Total", f"{kpis['total_students']}")

    # Visualisations interactives
    st.subheader("📊 Visualisations Interactives")
    plot_kpi_charts(filtered_df)

else:
    st.info("📥 Veuillez téléverser un fichier CSV pour commencer.")
