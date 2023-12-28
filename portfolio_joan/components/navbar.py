import reflex as rx
from portfolio_joan.styles.styles import Size as Size        
import portfolio_joan.styles.styles as styles


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.hstack(
                rx.icon(tag="email", _dark={"color": "rgba(255, 255, 255, 0.5)"}),
                rx.text("martinez.olivares.006@gmail.com", font_size=Size.SMALL.value),
            ),
            width="25%",
            margin="auto",
        ),
        rx.box(
            rx.hstack(
                rx.button(
                    rx.icon(tag="moon"),
                    on_click=rx.toggle_color_mode,
                    font_size=Size.SMALL.value,
                    size="xs"
                ),
            ),
            width="25%",
            margin="auto",
        ),
        style=styles.hstack_navbar_style
        )
