import streamlit as st
import pandas as pd
import os

# Percorsi dei file CSV
FILE_CLASSIFICA = "classifica.csv"
FILE_STORICO = "storico_giornate.csv"
FILE_SCONTRI = "scontri_diretti.csv"


# Funzione per caricare la classifica
def carica_classifica():
    if os.path.exists(FILE_CLASSIFICA):
        df = pd.read_csv(FILE_CLASSIFICA, index_col=0)
        return df
    return None


# Funzione per caricare lo storico giornate
def carica_storico():
    if os.path.exists(FILE_STORICO):
        return pd.read_csv(FILE_STORICO)
    return None


# Funzione per caricare gli scontri diretti
def carica_scontri():
    if os.path.exists(FILE_SCONTRI):
        return pd.read_csv(FILE_SCONTRI, index_col=0)
    return None


# Titolo dell'app
st.title("⚽ Fantacalcio Battle Royale")

# 📌 Mostra Classifica Ordinata
st.subheader("🏆 Classifica Attuale")
df_classifica = carica_classifica()

if df_classifica is not None:
    # Ordina per punti_scontri e poi punti_totali
    df_classifica = df_classifica.sort_values(by=["punti_scontri", "punti_totali"], ascending=[False, False])

    # Resetta l'indice per una visualizzazione più pulita
    df_classifica = df_classifica.reset_index()
    df_classifica.index = df_classifica.index + 1
    # Mostra la classifica
    st.dataframe(df_classifica)
else:
    st.warning("⚠️ Nessuna classifica trovata. Carica il file 'classifica.csv'.")

# 📌 Mostra Storico Giornate
st.subheader("📅 Storico Giornate")
df_storico = carica_storico()

if df_storico is not None:
    st.dataframe(df_storico)
else:
    st.warning("⚠️ Nessun storico trovato. Carica il file 'storico_giornate.csv'.")

# 📌 Mostra Scontri Diretti
st.subheader("⚔️ Scontri Diretti")
df_scontri = carica_scontri()

if df_scontri is not None:
    st.dataframe(df_scontri)
else:
    st.warning("⚠️ Nessun file di scontri diretti trovato. Carica 'scontri_diretti.csv'.")

