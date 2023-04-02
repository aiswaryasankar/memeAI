import pynecone as pc


def sidebar():
    return pc.box(
        pc.vstack(
            pc.link(
                pc.image(
                    src="https://storage.googleapis.com/sdp-memechat/aa785b20cdee8c1e2fcf8d0403f5c97e.jpg",
                ),
                href="/",
            ),
            pc.link(
                pc.box(
                    "Text-to-meme",
                    bg="lightgreen",
                    border_radius="md",
                    text_align="left",
                ),
                href="/txt2meme",
            ),
            pc.link(
                pc.box(
                    "Themed memes",
                    bg="yellow",
                    border_radius="md",
                    text_align="left",
                ),
                href="/txt2meme",
            ),
            pc.link(
                pc.box(
                    "Search templates",
                    bg="lightblue",
                    border_radius="md",
                    text_align="left",
                ),
                href="/txt2meme",
            ),
            width="250px",
            padding_x="2em",
            padding_y="1em",
        ),
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        z_index="500",
    )
