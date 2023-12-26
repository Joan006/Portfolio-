import reflex as rx

from portfolio_joan.styles.styles import Size as Size
import  portfolio_joan.styles.styles as styles

def link_button(title:str,url:str, image:str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = image,
                    font_size =Size.LARGE.value,
                    heigth = Size.BIG.value,
                    margin = Size.SMALL.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_body_style),
                    spacing = "1em",
                    align_items="start",
                    margin = Size.ZERO.value,
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )
