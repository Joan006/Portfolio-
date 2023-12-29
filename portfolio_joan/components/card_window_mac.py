import reflex as rx
import portfolio_joan.styles.styles as styles
from portfolio_joan.styles.styles import Size as Size
# Define style dictionaries for each class
card_style = {
    "width": "70em",
    "margin": "0em auto",
    "background_color": "#011522",
    "border_radius": "8px",
    "z_index": "1",
}

tools_style = {
    "display": "flex",
    "align_items": "center",
    "padding": "0px",
}

circle_style = {
    "padding": "0 4px",
}

box_style = {
    "display": "inline-block",
    "align_items": "center",
    "width": "10px",
    "height": "10px",
    "padding": "1px",
    "border_radius": "50%",
}

red_style = {"background_color": "#ff605c"}
yellow_style = {"background_color": "#ffbd44"}
green_style = {"background_color": "#00ca4e"}

# Create the Reflex components with the styles applied
def card_window_mac(title:str, description:str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.span(style={**box_style, **red_style}),
                style=circle_style,
            ),
            rx.box(
                rx.span(style={**box_style, **yellow_style}),
                style=circle_style,
            ),
            rx.box(
                rx.span(style={**box_style, **green_style}),
                style=circle_style,
            ),
            style=tools_style,
        ),        
        rx.box(
            rx.vstack(
            rx.text(title, font_size=Size.BIG.value, font_weight="600", style=styles.heading_style),
            rx.text(description, font_size=Size.VERY_SMALL.value),
            margin="10px",
        ),
        style=card_style
        ),
        style=card_style,
    )
