import reflex as rx 
from portfolio_joan.styles.styles import Size as Size

def social_media():
    return rx.breadcrumb(
        rx.breadcrumb_item(
            rx.link(
                rx.image(
                    src="icons/github.svg",
                    width=Size.MEDIUM.value,
                    style={"transition": "transform 0.2s ease-in-out", "cursor": "pointer"},
                    _hover={"transform": "scale(1.2)" }
                ),
                href="https://github.com/tu-usuario",
                is_external=True
            )
        ),
        rx.breadcrumb_item(
            rx.link(
                rx.image(
                    src="icons/instagram.svg",
                    width=Size.MEDIUM.value,
                    style={"transition": "transform 0.2s ease-in-out", "cursor": "pointer"},
                    _hover={"transform": "scale(1.2)"}
                ),
                href="https://linkedin.com/in/tu-usuario",
                is_external=True
            )
        ),
        rx.breadcrumb_item(
            rx.link(
                rx.image(
                    src="icons/linkedin.svg",
                    width=Size.MEDIUM.value,
                    style={"transition": "transform 0.2s ease-in-out", "cursor": "pointer"},
                    _hover={"transform": "scale(1.2)"}
                ),
                href="https://twitter.com/tu-usuario",
                is_external=True
            )
        ),
        separator=" ",  # Puedes cambiar el separador a tu preferencia
        color="rgb(107,99,246)"  # Puedes ajustar el color segun tu diseño
    )
