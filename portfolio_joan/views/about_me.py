from platform import win32_ver
import reflex as rx 
from portfolio_joan.components.proyects import proyects
from portfolio_joan.styles.styles import Size

def about_me() -> rx.Component:
    return rx.responsive_grid(
        rx.grid_item(
            rx.hstack(
                rx.heading(
                    "I am a junior software programmer",
                    font_size=Size.BIG.value,
                    font_weight="600",
                    style={
                        "background": "linear-gradient(to right, #e1e1e1, #f9cd45)",
                        "background_clip": "text",
                    },
                    margin_start = "3em"
                ), 
                # Add components inside this hstack to populate your top horizontal grid.
                width="100%",

            ),
            col_span=2,  # This will make the top grid item span across two columns on larger screens.
        ),
        rx.grid_item(
                rx.box(
                    rx.heading(
                        "My projects carried out",
                        font_size=Size.TITLE_HERO.value,
                        font_weight="900",
                        style={
                            "background": "linear-gradient(to right, #e1e1e1, #f9cd45)",
                            "background_clip": "text",
                        },
                        margin_start = "2em"

                    ),
                # Presumably, this is the content of your first column.
                height="100%",
            ),
        ),
        rx.grid_item(
            rx.box(
                proyects(),  # This function call should return a component for the second column.
                height="100%",
            ),
        ),
        columns=[1, 2],  # 1 column on small screens, 2 columns on larger screens.
        spacing="1em",
        height="100%",
        template_columns="repeat(2, 1fr)",# Ensure there are two template columns defined for larger screens.
        style={
            "background-image": "url('room.jpg')",
            "background-position": "center",
            "background-repeat": "no-repeat",
            "background-attachment": "fixed",  # Esto asegura que la imagen se mantenga est‡tica
            "background-size": "cover",  # Esto asegura que la imagen cubra todo el contenedor
        },
    )                   
