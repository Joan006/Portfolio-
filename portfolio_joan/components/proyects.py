import reflex as rx
from portfolio_joan.components.link_button import link_button
import portfolio_joan.styles.styles as styles
from portfolio_joan.styles.styles import Size as Size

def proyects() -> rx.Component:
    return rx.responsive_grid(
        rx.box(
            rx.vstack(
                rx.image(
                    src="imagenes/python_imagen.jpeg",
                    font_size=Size.BIG.value,
                    height="5em",
                    border_radius="2em"
                        
                ),
                rx.text("QR Generator", style=styles.title_card_style
                ),  
                rx.text("Script,QR code generator",font_size=Size.VERY_SMALL.value),  
                link_button(
                    "Repository",
                    " ",
                    "icons/github.svg"
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style,
        ),
        rx.box(
            rx.vstack(
                rx.image(
                    src="imagenes/python_imagen.jpeg",
                    font_size=Size.BIG.value,
                    height="5em",
                    border_radius="2em",
                        
                ),
                rx.text("Automation send emails", style=styles.title_card_style 
                ),  
                rx.text("Script,send emails automation",font_size=Size.VERY_SMALL.value),  
                link_button(
                    "Repository",
                    " ",
                    "icons/github.svg"
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style
        ),
        rx.box(
            rx.vstack(
                rx.image(
                    src="imagenes/python_imagen.jpeg",
                    font_size=Size.BIG.value,
                    height="5em",
                    border_radius="2em",
                        
                ),
                rx.text("Automation join PDFs", style=styles.title_card_style
                ),  
                rx.text("Script , that joins PDFs into one",font_size=Size.VERY_SMALL.value), 
                link_button(
                    "Repository",
                    " ",
                    "icons/github.svg"
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style,
        ),
        rx.box(
            rx.vstack(
                rx.image(
                    src="imagenes/python_imagen.jpeg",
                    font_size=Size.BIG.value,
                    height="5em",
                    border_radius="2em",
                        
                ),
                rx.text("Compressor images", style=styles.title_card_style
                ),  
                rx.text("Script, which compresses images",font_size=Size.VERY_SMALL.value),  
                link_button(
                    "Repository",
                    " ",
                    "icons/github.svg"
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style,
        ),
        rx.box(
         rx.vstack(
                rx.image(
                    src="imagenes/python_imagen.jpeg",
                    font_size=Size.BIG.value,
                    height="5em",
                    border_radius="2em",
                        
                ),
                rx.text("Background remover", style=styles.title_card_style
                ),
                rx.text("Descripcion del proyecto...",font_size=Size.VERY_SMALL.value),  
                link_button(
                    "Repository",
                    " ",
                    "icons/github.svg"
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style,
        ),
        rx.box(
         rx.vstack(
                rx.image(
                    src="imagenes/python_imagen.jpeg",
                    font_size=Size.BIG.value,
                    height="5em",
                    border_radius="2em",
                        
                ),
                rx.text("Django - todo list", style=styles.title_card_style
                ),  
                rx.text("App, todo list", font_size=Size.VERY_SMALL.value),  
                link_button(
                    "Repository",
                    " ",
                    "icons/github.svg"
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style
        ),
        columns=[1, 2, 3],
        min_child_width="10.5em",
        height="80vh",
        padding=["0rem 1rem", "0rem 1rem", "0rem 1rem", "0rem 2rem", "0rem 2rem"]
    )

