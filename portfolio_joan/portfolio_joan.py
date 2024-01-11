"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx


import portfolio_joan.styles.styles as styles
from portfolio_joan.components.navbar import navbar
from portfolio_joan.views.hero import hero
from portfolio_joan.views.about_me import projects_zone
from portfolio_joan.views.info_me import info_me
from portfolio_joan.views.education_list import education_list
from portfolio_joan.views.footer import footer


filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    """The app state."""

    pass



def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        education_list(),
        #info_me(),
        projects_zone(),
        info_me(),
        #education_list(),
        footer()
)
 


# Add state and page to the app.
app = rx.App(style=styles.BASE_STYLE)
app.add_page(index, title="JoanDv || Portfolio", image="/favicon.ico")
