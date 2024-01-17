import reflex as rx
from portfolio_joan.styles.styles import Size as Size
import portfolio_joan.styles.styles as styles
from portfolio_joan.components.skill_item import skill_item


def my_skills() -> rx.Component:
    return rx.vstack(
        rx.desktop_only(
            rx.box(
                rx.hstack(
                    rx.image(
                        src="skills/head.png", loading="lazy", width=Size.BIG.value
                    ),
                    rx.heading(
                        "My skills",
                        font_size=Size.VERY_BIG.value,
                        font_weight="600",
                        text_align="center",
                        margin="30px",
                        style=styles.heading_style,
                    ),
                    justify_content="center",
                    margin= "20px"
                ),
                rx.hstack(
                    rx.heading(
                        "Backend / Automations",
                        font_size=Size.MEDIUM.value,
                        font_weight="600",
                        margin="8px",
                        style=styles.heading_style,
                    ),
                    rx.icon(
                        tag="arrow_forward",
                        color="white",
                        font_size=Size.MEDIUM.value,
                    ),
                    skill_item("skills/python.png", "Python"),
                    skill_item("skills/django.png", "Django"),
                    skill_item("skills/numpy.png", "Numpy"),
                    skill_item("skills/reflex.png", "Reflex"),
                    width="100%",
                    margin="1em",
                ),
                rx.hstack(
                    rx.heading(
                        "Web Development",
                        font_size=Size.MEDIUM.value,
                        font_weight="600",
                        margin="8px",
                        style=styles.heading_style,
                    ),
                    rx.icon(
                        tag="arrow_forward",
                        color="white",
                        font_size=Size.MEDIUM.value,
                    ),
                    skill_item("skills/javascript.png", "Javascript"),
                    skill_item("skills/html.png", "Html"),
                    skill_item("skills/css.png", "Css"),
                    width="100%",
                    margin="1em",
                ),
                rx.hstack(
                    rx.heading(
                        "Other Languages",
                        font_size=Size.MEDIUM.value,
                        font_weight="600",
                        margin="8px",
                        style=styles.heading_style,
                    ),
                    rx.icon(
                        tag="arrow_forward",
                        color="white",
                        font_size=Size.MEDIUM.value,
                    ),
                    skill_item("skills/c_sharp.png", "C#"),
                    skill_item("skills/git.png", "Git"),
                    width="100%",
                    margin="1em",
                ),
            ),
            width="100%",
            align_items="flex_end",
            height=["60vh", "60vh", "60vh", "60vh", "60vh"],
            margin="auto",
            style={
                "backdrop_filter": "blur(2px)",
                "background-image": "url('imagenes/human_desktop.jpg')",
                "background-position": "center",
                "background-attachment": "fixed",
                "background-size": "cover",
                "padding": "1em",
            },
        ),
    )

def my_skills_mobile() -> rx.Component:
    return rx.vstack(
        rx.mobile_and_tablet(
            rx.box(
                rx.hstack(
                    rx.image(
                        src="skills/head.png", loading="lazy", width=Size.BIG.value
                    ),
                    rx.heading(
                        "My skills",
                        font_size=Size.VERY_BIG.value,
                        font_weight="600",
                        text_align="center",
                        margin="30px",
                        style=styles.heading_style,
                    ),
                    justify_content="center",
                    margin="20px"
                ),
                rx.hstack(
                    rx.heading(
                        "Backend / Automations",
                        font_size=Size.MEDIUM.value,
                        font_weight="600",
                        style=styles.heading_style,
                    ),
                    rx.icon(
                        tag="arrow_forward",
                        font_size=Size.MEDIUM.value,
                    ),
                    skill_item("skills/python.png", "Python"),
                    skill_item("skills/django.png", "Django"),
                    skill_item("skills/numpy.png", "Numpy"),
                    skill_item("skills/reflex.png", "Reflex"),
                    width="100%",
                ),
                rx.hstack(
                    rx.heading(
                        "Web Development",
                        font_size=Size.MEDIUM.value,
                        font_weight="600",
                        style=styles.heading_style,
                    ),
                    rx.icon(
                        tag="arrow_forward",
                        font_size=Size.MEDIUM.value,
                    ),
                    skill_item("skills/javascript.png", "Javascript"),
                    skill_item("skills/html.png", "Html"),
                    skill_item("skills/css.png", "Css"),
                    width="100%",
                ),
                rx.hstack(
                    rx.heading(
                        "Other Languages",
                        font_size=Size.MEDIUM.value,
                        font_weight="600",
                        style=styles.heading_style,
                    ),
                    rx.icon(
                        tag="arrow_forward",
                        font_size=Size.MEDIUM.value,
                    ),
                    skill_item("skills/c_sharp.png", "C#"),
                    skill_item("skills/git.png", "Git"),
                    width="100%",
                ),
            ),
            width="100%",
            align_items="flex_end",
            height=["60vh", "60vh", "60vh", "60vh", "60vh"],
            margin="auto",
            style={
                "backdrop_filter": "blur(2px)",
                "background-image": "url('imagenes/mobile.jpg')",
                "background-position": "center",
                #"background-attachment": "fixed",
                "background-size": "cover",
                "background-repeat": "no-repeat",
                "padding": "1em",
            },
        ),
    )
