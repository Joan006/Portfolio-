import reflex as rx

from portfolio_joan.styles.styles import Size as Size
import  portfolio_joan.styles.styles as styles

def image_text_button(image_url: str, button_text: str, text_font_size: str) -> rx.Component:
    return rx.button(
        rx.image(src=image_url, alt="Button Image"),  # Include the image
        rx.text(button_text, font_size=text_font_size),  # Apply font_size prop for text size
        style={"padding": "10px", "border_radius": "5px"}  # Additional styling attributes
    )

def link_button(title:str,url, image:str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
               rx.image(
                    src = image,
                    width = Size.MEDIUM.value,
                    margin = "5px",
                    loading="lazy"
                ),
                rx.vstack(
                rx.text(title, style=styles.button_title_style),
                    spacing = "0em",
                    margin = Size.ZERO.value,

                ),
                justify_content="space-around",
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
        display="flex",
        justify_content= "center",
        background_color = "black",
        border = "1px solid #ffbd44",
        color = "#ffbd44",
        border_radius = "1em",
        _hover={"transform": "scale(1)","box_shadow": "0 0 9px #f9cd45"},
        style=styles.no_hover_style
    )
