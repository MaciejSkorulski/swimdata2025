
import streamlit as st
import pandas as pd
from datetime import datetime

# ------------------------------
# USTAWIENIA POCZĄTKOWE
# ------------------------------

st.set_page_config(page_title="SwimData - Trening", layout="wide")
st.title("📊 Rejestr treningowy – SwimData 2025")

# Domyślna lista zawodników (do edycji)
zawodnicy = [
    "Anna Kowalska", "Piotr Nowak", "Kasia Wiśniewska", "Tomek Zieliński",
    "Ola Dąbrowska", "Michał Wójcik", "Julia Maj", "Bartek Szymański",
    "Natalia Lis", "Kacper Bąk"
]

# ------------------------------
# KROK 1: WYBÓR DATY
# ------------------------------
st.subheader("1. Wybierz dzień treningowy")
selected_date = st.date_input("Data treningu", value=datetime.today())

# ------------------------------
# KROK 2: RODZAJ I GODZINA TRENINGU
# ------------------------------
st.subheader("2. Informacje o treningu")
col1, col2 = st.columns(2)
with col1:
    training_type = st.selectbox("Rodzaj treningu", ["Woda", "Ląd"])
with col2:
    training_time = st.time_input("Godzina treningu")

# ------------------------------
# KROK 3: LISTA ZAWODNIKÓW I DANE
# ------------------------------
st.subheader("3. Wprowadź dane zawodników")

# Przygotowanie tabeli z miejscem do wpisu
data = []
for name in zawodnicy:
    col1, col2, col3, col4 = st.columns([2, 1, 1, 3])
    with col1:
        st.markdown(f"**{name}**")
    with col2:
        presence = st.checkbox("Obecny", key=f"{name}_presence")
    with col3:
        training_ab = st.selectbox("A/B", ["-", "A", "B"], key=f"{name}_ab")
    with col4:
        test_result = st.text_input("Grip test / Uwagi", key=f"{name}_test")

    data.append({
        "Data": selected_date,
        "Godzina": training_time.strftime("%H:%M"),
        "Rodzaj treningu": training_type,
        "Zawodnik": name,
        "Obecność": "✅" if presence else "❌",
        "Trening A/B": training_ab,
        "Wynik testu / Uwagi": test_result
    })

# ------------------------------
# KROK 4: ZAPIS
# ------------------------------
st.subheader("4. Zapisz dane treningu")

if st.button("📥 Zapisz trening"):
    df = pd.DataFrame(data)
    filename = f"trening_{selected_date.strftime('%Y-%m-%d')}.csv"
    df.to_csv(filename, index=False)
    st.success(f"Dane zapisane do pliku: {filename}")
    st.dataframe(df)
