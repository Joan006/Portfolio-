import reflex as rx
from portfolio_joan.components.link_button import link_button
import portfolio_joan.styles.styles as styles
from portfolio_joan.styles.styles import Size as Size


def card_with_content(image_url, title_card,title, url, image) -> rx.Component:
    return rx.vstack(
        rx.card(
            rx.aspect_ratio(rx.image(src=image_url, border_radius="2em"),loading="lazy", ratio=16 / 14),
            header=rx.heading(title_card, style=styles.title_card_style),
            footer = link_button(title, url, image),
            style=styles.style_card,
        ),
        is_external=True,
        # centeamos la tarjeta en el espacio 
        display="flex",
        justify_content="center",            
        style=styles.no_hover_style
    )

def proyects_cards() -> rx.Component:
    return rx.responsive_grid(
        card_with_content("imagenes/python_imagen.jpeg", "QR Generator","repository", "file:///Users/mac/Downloads/Joan-Mart%C3%ADnez-Olivares.pdf", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Automation send emails","repository", "https://github.com/Joan006/django_send_emails", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Automation join pdf","repository", "https://github.com/Joan006/automation_join_pdfs", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Compressor images","repository", "https://github.com/Joan006/compressor-images", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Remove Background","repository", "https://github.com/Joan006/remove-background", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Django todo list","repository", "https://github.com/Joan006/django-todo-list", "icons/github.svg"),
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
        card_with_content("imagenes/python_imagen.jpeg", "QR Generator","repository", "https://github.com/Joan006/qr_generator", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Automation send emails","repository", "https://github.com/Joan006/django_send_emails", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Automation join pdf","repository", "https://github.com/Joan006/automation_join_pdfs", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Compressor images","repository", "https://github.com/Joan006/compressor-images", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Remove Background","repository", "https://github.com/Joan006/remove-background", "icons/github.svg"),
        card_with_content("imagenes/python_imagen.jpeg", "Django todo list","repository", "https://github.com/Joan006/django-todo-list", "icons/github.svg"),
        # Comentamos proyectos que podemos no necesitar

        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        #card_with_content("imagenes/python_imagen.jpeg", "Developer tools list","#"),
        template_columns="repeat(2, 1fr)",
        spacing="1em",
        min_child_width="9em",
        margin= "1em",
    )
