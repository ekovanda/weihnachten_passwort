import streamlit as st
import time

solutions = {
    "🌄": "Miraduro da Beira da Quinta",
    "🎁": "Schlüssel",
    "💍": "AIR",
    "👶": "1/7",
    "👑": "👸F7",
    "📷": True

}

passcode = {
    "Eddie & Cora": 123456,
    "Ellery & Julia": 234567,
    "Luisa": 345678
}

st.title("🎅 Ho Ho Ho! 🎅")

with st.form("my_form"):
    
    # Wo wurde unser Begrüßungsvideo für Alma gedreht?
    video = st.text_input(label="🌄", help="Tipp: Der Ort hat >4.5 ⭐ bei über 2000 Bewertungen.")
    st.divider()
    
    # Was haben Luisa und ich von der Standesbeamtin geschenkt bekommen?
    geschenk = st.text_input(label="🎁")
    st.divider()
    
    # Was ist die Intersection unserer Hochzeitslocations?
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    intersection = st.pills(label="💍", options=letters, selection_mode="multi", help="1 Wort pro Location")
    intersection = "".join(sorted(intersection))
    st.divider()

    # Wie viel Gramm wog 1 Millimeter Alma zur Gebur
    options = ["1/10", "1/9", "1/8", "1/7", "1/6", "1/5", "1/4", "1/2", "1/1"]
    alma = st.select_slider(label="👶", options=options)
    st.divider()

    # Was nun?
    chess1 = st.segmented_control(label="🤴", options=["🐴", "👨‍🌾", "🏃‍♂️", "👸", "🏰"])
    chess2 = st.segmented_control(label="🤴", options=["A", "B", "C", "D", "E", "F", "G", "H"], label_visibility="hidden")
    chess3 = st.segmented_control(label="🤴", options=["1", "2", "3", "4", "5", "6", "7", "8"], label_visibility="hidden")
    chess = (chess1 or "") + (chess2 or "") + (chess3 or "")
    st.divider()

    # Wie lange sind Ellery & Julia verheiratet?
    foto = st.checkbox(label="📷")
    st.divider()

    person = st.radio(label="Wer bist du?", options=["Eddie & Cora", "Ellery & Julia", "Luisa"])

    submitted = st.form_submit_button("Prüfen")
    if submitted:
        with st.spinner('Der Weihnachtsmann prüft die Antworten...'):
            time.sleep(5)

        answers = [video, geschenk, intersection, alma, chess, foto]
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