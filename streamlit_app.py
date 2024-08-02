
import streamlit as st
import random
import string
st.title('Generator hasel ')
if st.button('Generuj'):
    def generate_password(length=16):
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = ''.join(random.choice(characters) for _ in range(length))
    return password
    print(generate_password())
