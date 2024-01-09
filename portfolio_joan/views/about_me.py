import reflex as rx
from reflex.constants import style
from portfolio_joan.components.proyects import proyects_cards, proyects_cards_mobile
from portfolio_joan.styles.styles import Size
import portfolio_joan.styles.styles as styles


def projects_zone() -> rx.Component:
    # divs - verticales definidos , con su contenido
    vertical_div_1 = rx.box(
        rx.tablet_and_desktop(proyects_cards(), width="100%", height="100%"),
        rx.mobile_only(proyects_cards_mobile(), width="100%", height="100%", style={"backdrop-filter":"blur(1px)"}),
    )
    vertical_div_2 = rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.heading(
                    "My projects carried out",
                    font_size=Size.TITLE_HERO.value,
                    font_weight="900",
                    style=styles.heading_style_blur,
                    margin_start="2em",
                ),
                width="40%",
                height="100%",
            )
        )
    )

    # div -horizontal del projects_zone
    horizontal_div = rx.box(
        rx.hstack(
            rx.heading(
                "Projects carried out with Python",
                font_size=Size.BIG.value,
                font_weight="600",
                margin_start="2em",
                style=styles.heading_style_blur,
            ),
        ),
        width="100%",
        height="50p%",
    )

    # Combine the vertical divs into a flex container
    vertical_container = rx.flex(
        vertical_div_1,
        vertical_div_2,
        direction="col",
        width="100%",
        grow="1",
    )

    # return -  de la funcion con los estilos de el fondo del about_me
    return rx.vstack(
        rx.mobile_and_tablet(
            rx.vstack(
                horizontal_div,
                vertical_container,
                spacing="1em",
                style={
                    "background-image": "url('imagenes/room_mobile.jpg')",
                    "background-position": "center",
                    "background-size": "cover",
                    "background-attachment": "fixed",
                    "padding": "1em",  
                },
            )
        ),
        rx.desktop_only(
            horizontal_div,
            vertical_container,
            spacing="1em",
            style={
                "background-image": "url('imagenes/room_desktop2.jpg')",
                "background-position": "center",
                "background-attachment": "fixed",
                "background-size": "cover",
                "padding": "1em",  # Esto asegura que la imagen cubra todo el contenedor
            },
        ),
    )



