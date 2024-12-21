import streamlit as st
import time

passwords = {
    "Eddie & Cora": "123",
    "Ellery & Julia": "456",
    "Luisa": "789"
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
            st.success(f"🎅: Richtig! 🎈")
        else:
            st.snow()
            st.error("🎅: Versuch's nochmal... ⛄")
