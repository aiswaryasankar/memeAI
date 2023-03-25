import streamlit as st
st.set_page_config(
    page_title="Text-to-meme | MemeAI",
    page_icon="👋",
)
from streamlit_extras.switch_page_button import switch_page
from annotated_text import annotated_text, annotation

from utils import load_button, add_logo

add_logo("https://storage.googleapis.com/sdp-memechat/aa785b20cdee8c1e2fcf8d0403f5c97e.jpg", height=150)


st.title("Let's create some memes!")
st.write(
        f'<hr style="background-color: #faa; margin-top: 0;'
        ' margin-bottom: 0; height: 3px; border: none; border-radius: 3px;">',
        unsafe_allow_html=True,
    )
annotated_text(annotation("MemeAI", color="#faa", border="1px dashed red"), " uses AI to generate quality", annotation("memes", color="#bbb", border="1px dashed red"), "for you to share with your audience")
#st.text('MemeAI uses AI to generate quality memes for you to share with your audience')
    
col1, col2, col3 = st.columns(3)
with col3:
    load_button('./webapp/styles/buton.css')
    if st.button('txt2meme'):
        switch_page("txt2meme")
with col1:
    load_button('./webapp/styles/buton.css')
    if st.button('search template'):
        switch_page("search_template")
with col2:
    load_button('./webapp/styles/buton.css')
    if st.button('Themed memes'):
        switch_page("theme")
