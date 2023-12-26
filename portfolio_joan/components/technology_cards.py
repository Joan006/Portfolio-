import reflex as rx
from reflex.components import flex

from portfolio_joan.styles.styles import Size as Size

# tegnologias 
class TecnologiasState(rx.State):
    tecnologias: list[dict] = [
        {"nombre": "Python", "color": "#3776AB"},
        {"nombre": "JavaScript", "color": "#F7DF1E"},
    ]

def tarjeta_tecnologia(tecnologia: dict):
    return rx.box(
        rx.text(tecnologia["nombre"], color="#ffffff"),
        bg=tecnologia["color"],
        padding="10px",
        margin="5px",
        border_radius="md"
    )

def techonology_cards():
    return rx.vstack(
        rx.heading("Mis Tecnolog’as", size="lg", align="center"),
        rx.responsive_grid(
            rx.foreach(TecnologiasState.tecnologias, tarjeta_tecnologia),
            columns=[2, 3, 4],
        )
    )
