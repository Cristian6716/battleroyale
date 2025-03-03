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
        return pd.read_csv(FILE_CLASSIFICA, index_col=0)
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
    df_classifica = df_classifica.sort_values(by=["punti_scontri", "punti_totali"], ascending=[False, False])
    df_classifica = df_classifica.reset_index()
    df_classifica.index = df_classifica.index + 1
    st.dataframe(df_classifica)
else:
    st.warning("⚠️ Nessuna classifica trovata. Carica il file 'classifica.csv'.")

# 📌 Mostra Scontri Diretti con menu a tendina
st.subheader("⚔️ Scontri Diretti")
df_scontri = carica_scontri()

if df_scontri is not None:
    squadre = list(df_scontri.index)  # Lista delle squadre
    squadra_scelta = st.selectbox("Seleziona una squadra", squadre)

    # Filtriamo solo la riga della squadra selezionata
    risultati_squadra = df_scontri.loc[squadra_scelta].dropna()

    # Convertiamo la serie in DataFrame per una visualizzazione più chiara
    df_risultati = pd.DataFrame({"Avversario": risultati_squadra.index, "Esito": risultati_squadra.values})

    # Mostriamo solo i risultati della squadra selezionata
    st.dataframe(df_risultati)
else:
    st.warning("⚠️ Nessun file di scontri diretti trovato. Carica 'scontri_diretti.csv'.")

# 📌 Mostra Storico Giornate
st.subheader("📅 Storico Giornate")
df_storico = carica_storico()

if df_storico is not None:
    st.dataframe(df_storico)
else:
    st.warning("⚠️ Nessun storico trovato. Carica il file 'storico_giornate.csv'.")
