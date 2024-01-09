import reflex as rx
from portfolio_joan.components.link_button import link_button
import portfolio_joan.styles.styles as styles
from portfolio_joan.styles.styles import Size as Size


def card_with_content(image_url, title, href) -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.aspect_ratio(rx.image(src=image_url, border_radius="2em"), ratio=16 / 14),
            header=rx.heading(title, style=styles.title_card_style),
            footer = link_button("Repository", "", "icons/github.svg"),
            style=styles.style_card,
        ),
        href=href,
        # centeamos la tarjeta en el espacio 
        display="flex",
        justify_content="center",            
        style=styles.no_hover_style
    )

def proyects_cards() -> rx.Component:
    return rx.responsive_grid(
        card_with_content("imagenes/python_imagen.jpeg", "QR Generator","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Automation send emails","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Automation join pdf","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Compressor images","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Remove Background","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Django todo list","#"),
        # Comentamos proyectos que podemos no necesitar

        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        template_columns="repeat(3, 1fr)",
        spacing="1em",
        min_child_width="9em",
        margin= "2em",
    )

def proyects_cards_mobile() -> rx.Component:
    return rx.responsive_grid(
        card_with_content("imagenes/python_imagen.jpeg", "QR Generator","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Automation send emails","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Automation join pdf","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Compressor images","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Remove Background","#"),
        card_with_content("imagenes/python_imagen.jpeg", "Django todo list","#"),
        # Comentamos proyectos que podemos no necesitar

        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        template_columns="repeat(2, 1fr)",
        spacing="1em",
        min_child_width="9em",
        margin= "1em",
    )
