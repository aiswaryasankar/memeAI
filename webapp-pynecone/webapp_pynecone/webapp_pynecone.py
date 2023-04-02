"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from webapp_pynecone.side_menu import sidebar
from webapp_pynecone.buttons import front_page_buttons
from webapp_pynecone.pages.text2meme import txt2meme, State

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def index():
    return pc.center(
        pc.vstack(
            pc.heading("Let's create some memes!", font_size="2em"),
            pc.text(
                "memeAI uses AI to generate quality memes for you to share with your audience",
                font_size="0.5em",
            ),
            front_page_buttons(),
            spacing="1.5em",
            font_size="2em",
        ),
        sidebar(),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(txt2meme, route="/txt2meme")
app.compile()
