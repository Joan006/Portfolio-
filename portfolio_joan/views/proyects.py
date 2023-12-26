import reflex as rx
from portfolio_joan.components.card import card
from portfolio_joan.components.link_button import link_button
import portfolio_joan.styles.styles as styles
def proyects() -> rx.Component:
    return rx.responsive_grid(
        rx.box(
            rx.vstack(
                rx.text("QR Generator", font_size="1.5em"),  # Título del proyecto
                rx.text("script,QR code generator"),  # Descripción del proyecto
                rx.button(
                    "Repository",
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style,
        ),
        rx.box(
            rx.vstack(
                rx.text("Automation send emails", font_size="1.5em"),  # T√≠tulo del proyecto
                rx.text("Script,send emails automation"),  # Descripci√≥n del proyecto
                rx.button(
                    "Repository",
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style
        ),
        rx.box(
            rx.vstack(
                rx.text("Automation join PDFs", font_size="1.5em"),  # T‚àö‚â†tulo del proyecto
                rx.text("Script , that joins PDFs into one"),  # Descripci‚àö‚â•n del proyecto
                rx.button(
                    "Repository",
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style,
        ),
        rx.box(
            rx.vstack(
                rx.text("Compressor images", font_size="1.5em"),  # T‚àö‚â†tulo del proyecto
                rx.text("Script, which compresses images"),  # Descripci‚àö‚â•n del proyecto
                rx.button(
                    "Repository",
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style,
        ),
        rx.box(
         rx.vstack(
                rx.text("Image background remover", font_size="1.5em"),  # T‚Äö√†√∂‚Äö√¢‚Ä†tulo del proyecto
                rx.text("Descripcion del proyecto..."),  # Descripci‚Äö√†√∂‚Äö√¢‚Ä¢n del proyecto
                rx.button(
                    "Repository",
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style,
        ),
        rx.box(
         rx.vstack(
                rx.text("Django - todo list", font_size="1.5em"),  # T‚Äö√†√∂‚Äö√¢‚Ä†tulo del proyecto
                rx.text("App, todo list"),  # Descripci‚Äö√†√∂‚Äö√¢‚Ä¢n del proyecto
                rx.button(
                    "Mas informacion",
                ),
                style=styles.style_card
            ),
            style=styles.div_card_style
        ),
        columns=[3],
        spacing="4",
        height="60vh",
        padding="5vh"
    )

