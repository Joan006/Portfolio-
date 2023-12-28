import reflex as rx
from reflex.event import background

from portfolio_joan.styles.styles import Size as Size
import  portfolio_joan.styles.styles as styles

def link_button(title:str,url:str, image:str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = image,
                    width = Size.MEDIUM.value,
                    margin = Size.VERY_SMALL.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    spacing = "0em",
                    align_items="start",
                    margin = Size.ZERO.value,
                )
            ),
            padding = "0px"
        ),
        href=url,
        is_external=True,
        width="100%",
        display="flex",
        justify_content= "",
        background_color = "#9b7703",
        border_radius = "1em",

    )
