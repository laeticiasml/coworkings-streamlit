 # Importation de la bibliothèque Streamlit
import streamlit as st
 # Ajouter un titre à votre application
st.title('Mon application Streamlit')
 # Ajouter du texte à votre application
st.write('Bienvenue dans cette application Streamlit.')

x = st.slider('Sélectionnez une valeur')
st.write(x, 'carré est', x*x)

import streamlit as st
import pandas as pd #pour lire et utiliser le fichier CSV.
import folium # pour créer la carte 
from streamlit_folium import st_folium #pour afficher la carte Folium dans l'application Streamlit.

# le titre de mon application 
st.title("📍 Coworkings en Île-de-France, projet de Laeticia")

# Charger les données et ouvrir le fichier CSV pour utiliser les données comme adresse, noms...
df = pd.read_csv("coworkings_idf_clean.csv")

# je vais utilisé cela pour créer une carte centrée sur Paris
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# cette boucle pour lire chaque ligne du tableau 
for _, row in df.iterrows():
    popup_text = f"""
    <b>{row['Nom'].title()}</b><br>
    📍 {row['Adresse'].title()}<br>
    🏙️ {row['Ville'].title()}
    """
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=folium.Popup(popup_text, max_width=300),
        icon=folium.Icon(color="blue", icon="briefcase", prefix="fa")
    ).add_to(m)

# Afficher la carte dans l'application
st.subheader("🗺️ Carte des espaces de coworking")
st_data = st_folium(m, width=700, height=500)

# Creation d'un graphique simple / diagramme en bâtons
st.subheader("📊 Nombre d'espaces par ville")
nb_villes = df["Ville"].value_counts()
st.bar_chart(nb_villes)


# Créer une barre de recherche pour taper le nom d'un coworking
nom_recherche = st.text_input("🔍 Tape le nom (ou une partie) d'un coworking :")

# Si l'utilisateur tape quelque chose, on filtre les résultats
if nom_recherche:
    df = df[df["Nom"].str.contains(nom_recherche, case=False, na=False)]