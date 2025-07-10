import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_kpi_charts(df):
    sns.set_style("whitegrid")

    # 1. Répartition des notes (Histogramme + courbe KDE)
    st.write("### 📈 Distribution des notes d'examen")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.histplot(df['Exam_Score'], bins=15, kde=True, color='#1f77b4', ax=ax1)
    ax1.set_xlabel("Note", fontsize=12)
    ax1.set_ylabel("Nombre d'étudiants", fontsize=12)
    st.pyplot(fig1)

    # 2. Moyenne des notes par genre (Barre horizontale)
    st.write("### 👥 Moyenne des notes par genre")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    gender_avg = df.groupby("Gender")["Exam_Score"].mean().sort_values()
    sns.barplot(x=gender_avg.values, y=gender_avg.index, palette="coolwarm", ax=ax2)
    ax2.set_xlabel("Note Moyenne")
    st.pyplot(fig2)

    # 3. Moyenne des notes par type d’école (Donut Chart)
    st.write("### 🏫 Moyenne des notes par type d’école")
    school_avg = df.groupby("School_Type")["Exam_Score"].mean()
    fig3, ax3 = plt.subplots()
    wedges, texts, autotexts = ax3.pie(school_avg, labels=school_avg.index, autopct='%1.1f%%',
                                       startangle=90, colors=sns.color_palette("pastel"),
                                       wedgeprops=dict(width=0.4))
    ax3.set(aspect="equal")
    st.pyplot(fig3)

    # 4. Moyenne des notes selon l'accès à internet (Barres groupées)
    st.write("### 🌐 Impact de l’accès à Internet sur la performance")
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(x="Internet_Access", y="Exam_Score", data=df, palette="Set2", ax=ax4)
    ax4.set_ylabel("Note Moyenne")
    st.pyplot(fig4)

    # 5. Moyenne par nombre de sessions de tutorat (Violin plot)
    st.write("### 🎓 Impact du tutorat sur la performance")
    fig5, ax5 = plt.subplots(figsize=(6, 4))
    sns.violinplot(x="Tutoring_Sessions", y="Exam_Score", data=df, palette="Spectral", ax=ax5)
    st.pyplot(fig5)
