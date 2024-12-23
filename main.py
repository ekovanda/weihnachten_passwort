import streamlit as st
import time

passwords = {
    "Eddie & Cora": "Kugeln",
    "Ellery & Julia": "Advent",
    "Luisa": "Schnee"
}

st.title("🎅🎄 Ho ho ho! 🎄🎅")

with st.form("my_form"):
    #st.markdown("## Wer bist du")
    person = st.selectbox(label="Wer bist du?", options=["Eddie & Cora", "Ellery & Julia", "Luisa"])
    password = st.text_input(label="Passwort")

    submitted = st.form_submit_button("Prüfen")

    if submitted:
        with st.spinner('Der 🎅 prüft das Passwort...'):
            time.sleep(5)

        if passwords[person] == password:
            st.balloons()
            st.success(f"🎅: Richtig! Merke dir den Zahlencode 🎈")
        else:
            st.snow()
            st.error("🎅: Versuch's nochmal... ⛄")
