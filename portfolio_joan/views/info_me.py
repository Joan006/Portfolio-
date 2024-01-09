import reflex as rx
from portfolio_joan.styles.styles import Size as Size
import portfolio_joan.styles.styles as styles


def info_me():
    return rx.center(
        rx.vstack(
            rx.heading(
                "About me", font_size=Size.VERY_BIG.value, style=styles.heading_style
            ),
            rx.text(
                """I am a passionate developer with experience in web technologies such as HTML, CSS, and JavaScript. Additionally, I have strong skills in Python, using it for Django web development and automation. I excel in tackling complex challenges and finding innovative solutions. My constant motivation to learn and my ability to work in a team come together to create exceptional user experiences. I am always looking to apply my skills to enhance the digital world.""",
                font_size=Size.SMALL.value
            ),
            padding="2em",
            width="80%",
            border_radius="1em",
            margin="auto",
            style=styles.container_infome_style,
        ),
        width="100%",
        height=["80vh","50vh","50vh", "50vh", "50vh"],
        display="flex",
        align_items="center",
        justify_content="center",
        padding="1em"
    )           
