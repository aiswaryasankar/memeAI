import pynecone as pc

def front_page_button(txt, descr, ref):
    return pc.box(
        pc.link(
            pc.box(
                pc.vstack(
                    pc.icon(tag="arrow_down"),
                    pc.text(txt, font_size="0.75em", color="black"),
                    pc.text(
                        descr, font_size="0.4em", color="black", text_align="center"
                    ),
                ),
                height="200px",
                width="400px",
                border_radius="20px",
                border_width="thin",
                border_color="lightblue",
                padding=5,
            ),
            href=ref,
            color="rgb(107,99,246)",
        ),
    )


def front_page_buttons():
    return pc.button_group(
        front_page_button(
            "Text-to-meme",
            "Generate AI memes by simply typing a sentence and let AI automatically choose the template and write a caption.",
            "/txt2meme",
        ),
        front_page_button(
            "Themed memes",
            "Generate AI memes for popular themes like startup, prodcut management and crypto by choosing a meme template and uploading a image of your own.",
            "/txt2meme",
        ),
        front_page_button(
            "Search",
            "Not sure which meme template to use? Just describe the emotion you're looking for and we'll get you the right template.",
            "/txt2meme",
        ),
    )
