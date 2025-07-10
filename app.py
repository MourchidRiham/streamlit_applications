import streamlit as st
import pandas as pd
import duckdb
from utils.duckdb_utils import load_data_into_duckdb, query_kpis
from utils.visualizations import plot_kpi_charts

# Configuration de la page
st.set_page_config(page_title="Tableau de Bord des Performances Étudiantes", layout="wide")
st.title("📊 Tableau de Bord des Performances Étudiantes")

# Téléversement du fichier CSV
uploaded_file = st.file_uploader("📂 Téléversez votre fichier CSV", type="csv")

if uploaded_file:
    # Lecture du fichier CSV
    df = pd.read_csv(uploaded_file)

    # Affichage des colonnes disponibles pour vérification
    st.write("✅ Colonnes disponibles :", df.columns.tolist())

    # Connexion à DuckDB en mémoire
    conn = duckdb.connect(database=':memory:')
    load_data_into_duckdb(conn, df)

    # Filtres dynamiques disponibles dans la barre latérale
    st.sidebar.header("🎯 Filtres")

    gender_options = df['Gender'].unique().tolist()
    gender_filter = st.sidebar.multiselect("Genre", options=gender_options, default=gender_options)

    school_options = df['School_Type'].unique().tolist()
    school_filter = st.sidebar.multiselect("Type d'école", options=school_options, default=school_options)

    internet_options = df['Internet_Access'].unique().tolist()
    internet_filter = st.sidebar.multiselect("Accès à Internet", options=internet_options, default=internet_options)

    # Application des filtres sur les données
    filtered_df = df[
        (df['Gender'].isin(gender_filter)) &
        (df['School_Type'].isin(school_filter)) &
        (df['Internet_Access'].isin(internet_filter))
    ]

    # Réenregistrement des données filtrées dans DuckDB
    conn.unregister('student_data')  # On annule l'ancien registre s'il existe
    conn.register('student_data', filtered_df)

    # Requête des indicateurs clés de performance (KPI)
    kpi_results = query_kpis(conn)

    # Affichage des KPI dans 4 colonnes
    st.subheader("📈 Indicateurs Clés de Performance (KPI)")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Note Moyenne", f"{kpi_results['average_grade']:.2f}")
    col2.metric("Taux de Réussite (%)", f"{kpi_results['pass_rate']:.2f}%")
    col3.metric("Taux d'Échec (%)", f"{kpi_results['fail_rate']:.2f}%")
    col4.metric("Nombre d'Étudiants", f"{kpi_results['total_students']}")

    # Affichage des visualisations
    st.subheader("📊 Visualisations")
    plot_kpi_charts(filtered_df)

else:
    st.info("🔄 Veuillez téléverser un fichier CSV pour commencer.")
