import reflex as rx

def footer() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("Derechos reservados Joandv© 2023"),
            rx.link("Términos de servicio", font_color="rgb(107 107 107)"),
            rx.link("Política de privacidad", font_color="rgb(107 107 107)" ),
            rx.text("Portfolio realizando - Reflex "),
            padding="1em",
            width="full",
            background_color= "rgb(2 11 22)",
            display="grid",
            place_items="center"
        ),

    )

