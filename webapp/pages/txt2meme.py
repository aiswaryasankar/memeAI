import streamlit as st
from utils import add_logo

add_logo("https://storage.googleapis.com/sdp-memechat/aa785b20cdee8c1e2fcf8d0403f5c97e.jpg", height=150)

def generate(txt):
    
    img = None
    
    # do_something()
    
    return txt, img


st.title("Convert any text to a meme")

with st.form(key='my_form'):
    text_input = st.text_input(key='title1', label='Enter any text and hit "Generate" to get relevant memes', value='', placeholder='Enter some sample text to generate meme and click submit')
    submitted = st.form_submit_button(label='Submit')
    if submitted:
        st.write(generate(text_input))
