import reflex as rx
import portfolio_joan.styles.styles as styles
from portfolio_joan.styles.styles import Size as Size



def education_item(src_icon: str, name_school: str, description: str) -> rx.Component:
    return rx.vstack(
        rx.unordered_list(
            rx.list_item(
                name_school,
                rx.hstack(
                    rx.image(src=src_icon, margin=Size.MEDIUM.value),
                    rx.text(description, color = "#f8c133",)
                ),
                font_size = Size.SMALL.value,
               font_weight="700"
            )
        ),
        width="100%",
        #font_size=Size.SMALL.value
    )           
