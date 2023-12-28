from platform import win32_ver
import reflex as rx 
from portfolio_joan.components.proyects import proyects

def about_me() -> rx.Component:
    return rx.responsive_grid(
        rx.grid_item(
            rx.hstack(
                rx.text("hola"),
                # Add components inside this hstack to populate your top horizontal grid.
                width="100%",

            ),
            col_span=2,  # This will make the top grid item span across two columns on larger screens.
        ),
        rx.grid_item(
            rx.box(
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
        template_columns="repeat(2, 1fr)"  # Ensure there are two template columns defined for larger screens.
    )                   
