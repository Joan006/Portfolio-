"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx

import portfolio_joan.styles.styles as styles
from portfolio_joan.components.navbar import navbar


filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    """The app state."""

    pass



def index() -> rx.Component:
    return rx.box(
        navbar(),
   )



# Add state and page to the app.
app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)
app.compile()
