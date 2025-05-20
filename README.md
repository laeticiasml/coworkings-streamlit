Coworkings en Île-de-France, projet de Laeticia
I.	Objectif de cette application 

Objectif principal : Trouver un espace de coworking à Paris facilement
Le besoin peut venir par exemple d’une personne souhaitant trouver un espace de coworking à Paris ou en Île-de-France  donc j’ai créé une carte interactive qui affiche tous les coworkings de la région. 
L’objectif de mon application était de :
•	Trouver automatiquement (grâce au scraping) tous les espaces de coworking listés sur un site 
•	Trier et nettoyer les informations pour qu’elles soient claires et bien structurées et sans doublons ni vides. 
•	Ajouter les coordonnées GPS (latitude et longitude) pour pouvoir les afficher sur une carte.
•	Créer une application web simple avec Streamlit pour :
o	Visualiser les coworkings une carte
o	Voir combien il y en a par ville (grâce à un graphique)
o	Rechercher par ville (liste déroulante) 

II.	Présentation des étapes réalisées

1.	Le scraper (le script qui récupère les données)
J’a travaillé sur Google Colab et j'ai commencé le projet en créant un script Python avec les bibliothèques requests et pyquery. Ce script va sur le site officiel leportagesalarial.com/coworking, 
Ce lien permet de récupérer tous les liens vers les pages d'espaces de coworking Ensuite, je filtre uniquement ceux situés en Île-de-France  après en visitant chaque page il va trouver les informations suivantes et les récupérer : le nom de l’espace, l’adresse, le code postal, la ville, le téléphone, le site web et l’accès métro.
Toutes les données vont être stockées dans un fichier que j’ai renommé coworkings_idf.csv et que j’ai enregistré également en local. 


2.	Nettoyage des données et géocodage (latitude, longitude)
Une fois le fichier CSV récupéré, j’ai fait un nettoyage des données :
•	J’ai supprimé les lignes vides et les doublons.
•	J’ai nettoyé les textes (mise en minuscules, suppression d'accents, ponctuations, etc.).
•	J’ai corrigé les codes postaux mal formatés (comme 75 011 devenu 75011).
Ensuite, j’ai utilisé la bibliothèque geopy que j’ai installé d’ailleurs pour trouver les coordonnées GPS (latitude et longitude) de chaque coworking.
les nouvelles infos récupérées ont été enregistrées dans un fichier final que j’ai nommé coworkings_idf_clean.csv.
 

3.	Passage à VS Code avec Streamlit
•	Création de l'environnement virtuel
•	Activation (sous Windows pour ma part) : .\env\Scripts\Activate.ps1
•	Installation des librairies : pip install streamlit folium streamlit-folium pandas pyquery  et puis j’ai créé un fichier requirements.txt pour faciliter la chose et quand quelqu’un voudra lancer le projet, il pourra juste écrire dans le terminal : pip install -r requirements.txt
•	Lancement de l'application : streamlit run projet.py

4.	Application Streamlit interactive
J’ai ensuite créé une application Streamlit dans un fichier projet.py.
Elle contient plusieurs fonctionnalités :
•	Un titre et une interface claire (Coworkings en Île-de-France, projet de Laeticia)
•	Une carte interactive avec folium qui affiche tous les coworkings localisés grâce à leurs coordonnées. Pour l’affichage de la carte J’utilise folium.Map() pour centrer sur Paris
•	Une visualisation graphique : un diagramme en bâtons qui montre le nombre d’espaces par ville.
df["Ville"].value_counts() pour compter combien il y a d'espaces par ville st.bar_chart() pour afficher un histogramme
•	Barre de recherche : qui permet taper le nom de la ville pour voir uniquement les espaces de coworking de cette ville affichés sur la carte et dans le graphique.
 
Remarques 
•	Le fichier principal est projet.py
•	Le fichier coworkings_idf_clean.csv est dans un même dossier appelé mon_projet-steamlit
•	L’application se lance avec : streamlit run projet.py

