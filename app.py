import streamlit as st

from gtts import gTTS
import pdfplumber
all_text = ' '
st.title("Convert all your E-books to Audio Books just like that!")
book = st.file_uploader("Please upload your pdf")
uploaded = st.checkbox("Is pdf uploaded?")
if uploaded == 1:
    with pdfplumber.open(book) as pdf:
        for text in pdf.pages:
            single_page_text = text.extract_text()
            all_text = all_text + '\n' + str(single_page_text)
    if all_text != "":
        tts = gTTS(all_text)
        tts.save('all_text.mp3')
        audio_file = open('all_text.mp3','rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav', start_time=0)
