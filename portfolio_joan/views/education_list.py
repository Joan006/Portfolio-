import reflex as rx
from portfolio_joan.components.education_item import education_item
from  portfolio_joan.styles.styles import Size as Size
import portfolio_joan.styles.styles as styles



def education_list() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.heading(
                    "🏫", 
                    size="2xl",
                    margin= "30px",
                    text_align = "center"
                ),
            rx.heading(
                    "My Education",
                    font_size=Size.BIG.value,
                    font_weight="600",
                    text_align= "center",
                    margin = "30px",
                    style=styles.heading_style
                ),
            ),
            education_item(
                "icons/school-check-solid.svg",
                "Centro de Estudios Tegnologicos y Cientificos n.11 - IPN",
                "-> Tecnico en Ingenieria Industrial - 2017-2020"
            ),
            education_item(
                "icons/school-solid.svg",
                "Escuela superior de Computo - IPN ",
                "-> Ing. Sistemas Computacionales - Cursando" 
            ),
            education_item(
                "icons/certificate.svg",
                "Centro de Investigacion en Computacion - IPN",
                "-> Certificado - Python en el ambito cientifico"
            )
        ),
        justify_content= "center",
        width = "100%",
        height=["60vh","50vh","50vh", "50vh", "50vh"],
        margin = "auto"
    )

