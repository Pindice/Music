import streamlit as st

from modules.model import predict, genre_mapping
from modules.preprocessing import audio_to_csv
from modules.components import dataframe_toggler, user_feedback

# TODO Rename things
# TODO Check librosa printed warnings


# Streamlit app ------------------------------------------------------------------------
st.title("Prédiction genre musical")

# File upload
uploaded_file = st.file_uploader(
    "Télécharger un fichier audio", type=["wav"]
)  # TODO Add mp3 !?


if uploaded_file is not None:
    # Perform audio processing
    dfs = audio_to_csv(uploaded_file)

    # Afficher les inputs preprocessed
    dataframe_toggler(dfs)

    # Predictions
    predicted_class = predict(dfs)

    # Feedback utilisateur
    classe = user_feedback(genre_mapping)

    # Nouvel entrainement (sytématique)
