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
                    _hover={"transform": "scale(1.2)", "box_shadow": "0 0 13px #3b2a8c", "border_radius": "10px"}
                ),
                href="https://github.com/Joan006",
                is_external=True
            )
        ),
        rx.breadcrumb_item(
            rx.link(
                rx.image(
                    src="icons/cv.svg",
                    width=Size.MEDIUM.value,
                    style={"transition": "transform 0.2s ease-in-out", "cursor": "pointer"},
                    _hover={"transform": "scale(1.2)","box_shadow": "0 0 9px #E4405F"}
                ),
                href="https://profile.indeed.com/p/joanm-l4pwc6l",
                is_external=True
            )
        ),
        rx.breadcrumb_item(
            rx.link(
                rx.image(
                    src="icons/linkedin.svg",
                    width=Size.MEDIUM.value,
                    style={"transition": "transform 0.2s ease-in-out", "cursor": "pointer"},
                    _hover={"transform": "scale(1.2)","box_shadow": "0 0 9px #0077B5"}
                ),
                href="https://www.linkedin.com/in/mart%C3%ADnez-olivares-joan-538a3b287/",
                is_external=True
            )
        ),
        separator=" ",  # Puedes cambiar el separador a tu preferencia
        color="rgb(107,99,246)"  # Puedes ajustar el color segun tu diseño
    )
