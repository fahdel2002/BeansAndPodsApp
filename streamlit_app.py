import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titre de l'application
st.title("Analyse des Données - Beans and Pods")

# Barre latérale pour charger le fichier CSV
st.sidebar.header("Chargement du dataset")
uploaded_file = st.sidebar.file_uploader("Choisissez un fichier CSV", type=["csv"])

# Charger les données
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("Fichier chargé avec succès !")
    
    # Aperçu des données
    if st.checkbox("Afficher un aperçu des données"):
        st.write(data.head())
    
    # Statistiques descriptives
    if st.checkbox("Afficher les statistiques descriptives"):
        st.write(data.describe())
    
    # Sélection des colonnes pour la visualisation
    columns = data.columns.tolist()
    selected_columns = st.multiselect("Choisissez des colonnes pour la visualisation", columns)
    
    if selected_columns:
        st.subheader("Visualisation des données")
        
        # Pairplot
        st.write("**Pairplot des colonnes sélectionnées**")
        fig = sns.pairplot(data[selected_columns])
        st.pyplot(fig)
        
        # Histogrammes
        for col in selected_columns:
            st.write(f"**Histogramme pour {col}**")
            fig, ax = plt.subplots()
            data[col].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
            st.pyplot(fig)
else:
    st.info("Veuillez charger un fichier pour commencer l'analyse.")
