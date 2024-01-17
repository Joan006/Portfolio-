import reflex as rx
from portfolio_joan.styles.styles import Size as Size        
import portfolio_joan.styles.styles as styles
from portfolio_joan.components.link_button import link_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.hstack(
                rx.icon(tag="email", color="white"),
                rx.text("martinez.olivares.006@gmail.com", font_size=Size.SMALL.value, color = "#f8c133"),
            ),
            width="70%",
            margin="auto",
        ),
        rx.box(
            rx.hstack(
                link_button(
                    "Developer Tools",
                    "https://developers.reflex.run/",
                    "favicon.ico"
                ),
            ),
            width="8em",
            margin="auto",
        ),
        style=styles.hstack_navbar_style
        )
