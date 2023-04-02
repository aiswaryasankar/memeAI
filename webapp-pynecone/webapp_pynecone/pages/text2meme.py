import pynecone as pc
from webapp_pynecone.side_menu import sidebar
from webapp_pynecone.endpoint import return_meme
import asyncio


class State(pc.State):
    """The app state."""

    text: str = "Convert any text to a meme or GIF..."
    image = "https://app.supermeme.ai/static/empty-placeholder.png"
    images: list[str] = []
    flag = False
    show_progress = False

    def set_text(self, text):
        self.text = text

    def default_image_toggle(self):
        self.flag = True

    def toggle_progress(self):
        self.show_progress = not self.show_progress

    async def on_submit(self):
        print(self.text)
        self.images = []
        images = await return_meme(self.text)
        await asyncio.sleep(4)
        self.images.extend(images)
        print(self.images)


def display_image(image):
    return pc.box(
        pc.image(
            src=image,
            height="500px",
            width="auto",
        ),
        height="auto",
        width="auto",
        border_radius="20px",
        border_width="thin",
        border_color="lightblue",
        padding=5,
    )


def txt2meme() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading(
                "Convert any text to a meme or GIF...",
                color_scheme="green",
                font_size="1.5em",
            ),
            pc.text(
                'Enter any text (tweet, blog post intro, etc.) and hit "Generate" to get relevant.',
                font_size=".5em",
            ),
            pc.vstack(
                pc.hstack(
                    pc.input(on_change=State.set_text, size="lg", width="600px"),
                    pc.button(
                        "Generate",
                        on_click=[
                            State.toggle_progress,
                            State.on_submit,
                            State.toggle_progress,
                            State.default_image_toggle,
                        ],
                    ),
                ),
                pc.cond(
                    State.flag,
                    pc.cond(
                        State.show_progress,
                        pc.circular_progress(is_indeterminate=True),
                        pc.responsive_grid(
                            pc.foreach(State.images, display_image),
                            columns=[2],
                            spacing="4",
                            width="1000px",
                        ),
                    ),
                    pc.image(
                        src="https://app.supermeme.ai/static/empty-placeholder.png",
                        height="500px",
                        width="auto",
                    ),
                ),
            ),
            spacing="1.5em",
            font_size="2em",
            height="auto",
            width="auto",
        ),
        sidebar(),
        padding_top="10%",
    )
