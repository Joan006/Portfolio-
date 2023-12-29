from platform import win32_ver
import reflex as rx 
from portfolio_joan.components.proyects import proyects
from portfolio_joan.styles.styles import Size
import portfolio_joan.styles.styles as styles

def about_me() -> rx.Component:
    return rx.responsive_grid(
        rx.grid_item(       
            rx.hstack(
                rx.heading(
                    "I am a junior software programmer",
                    font_size=Size.BIG.value,
                    font_weight="600",
                    margin_start = "2em",
                    style=styles.heading_style,
                ), 
                
                width="100%",

            ),
            col_span=2,  
        ),
        rx.grid_item(
            rx.box(
                proyects(),  
                height="100%",
            ),
        ),
        rx.grid_item(
                rx.box(
                    rx.heading(
                        "My projects carried out",
                        font_size=Size.TITLE_HERO.value,
                        font_weight="900",
                        style=styles.heading_style,
                        margin_start = "2em"

                    ),
                
                height="100%",
            ),
        ),        columns=[1, 2],  
        spacing="1em",
        height="100%",
        template_columns="repeat(2, 1fr)",
        style={
            "background-image": "url('room4.jpg')",
            "background-position": "center",
            "background-repeat": "no-repeat",
            "background-size": "cover",  # Esto asegura que la imagen cubra todo el contenedor
        },
    )                   
