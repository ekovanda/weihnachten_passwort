import streamlit as st
import time

solutions = {
    "📷": "Miraduro da Beira da Quinta",
    "🎁": "Schlüssel",
    "💍": "AIR",
    "👶": "1/7",
    "👑": "Qxf7#",
    "📆": "237"

}

passcode = {
    "Eddie & Cora": 123456,
    "Ellery & Julia": 234567,
    "Luisa": 345678
}

st.title("🎅🎄 Ho ho ho! 🎄🎅")

with st.form("my_form"):
    
    # Wo wurde unser Begrüßungsvideo für Alma gedreht?
    video = st.text_input(label="📷", help="Tipp: Der Ort hat >4.5 ⭐ bei über 2000 Bewertungen.")
    
    # Was haben Luisa und ich von der Standesbeamtin geschenkt bekommen?
    geschenk = st.text_input(label="🎁")
    
    # Was ist die Intersection unserer Hochzeitslocations?
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    intersection = st.pills(label="💍", options=letters, selection_mode="multi", help="1 Wort pro Location")
    intersection = "".join(sorted(intersection))

    # Wie viel Gramm wog 1 Millimeter Alma zur Gebur
    options = ["1/10", "1/9", "1/8", "1/7", "1/6", "1/5", "1/4", "1/2", "1/1"]
    alma = st.select_slider(label="👶", options=options) 

    # Was nun?
    chess = st.text_input(label="👑", help="5 Zeichen")

    # Wie lange sind Ellery & Julia verheiratet?
    hochzeit = st.slider(label="📆", min_value=0, max_value=365, help="2.")

    person = st.radio(label="Wer bist du?", options=["Eddie & Cora", "Ellery & Julia", "Luisa"])

    submitted = st.form_submit_button("Prüfen")
    if submitted:
        with st.spinner('Der Weihnachtsmann prüft die Antworten...'):
            time.sleep(5)

        answers = [video, geschenk, intersection, alma, chess, hochzeit]
        correct = 0
        for idx, icon in enumerate(solutions.keys()):
            if solutions[icon] == answers[idx]:
                st.success(f"{icon}: Richtig!")
                correct += 1
            else:
                st.error(f"{icon}: Versucht es nochmal")

        if correct == 6:
            st.warning("🎅🎅🎅 Alles geschafft 🎅🎅🎅")
            st.warning(f"Dein Code ist: **{passcode[person]}**")
            st.snow()