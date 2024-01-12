import reflex as rx 
import portfolio_joan.styles.styles as styles 
from portfolio_joan.styles.styles import Size as Size


def skill_item(src_image:str, title_skill:str ) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=src_image,          
            loading="lazy"
        ),
        rx.text(
            title_skill,
            font_size= Size.SMALL.value,
            style=styles.text_component,
        ),
        width="8vh",
        height = "12vh",
        margin=Size.MEDIUM.value,
    )


