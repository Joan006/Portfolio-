import reflex as rx 
from enum import Enum

from .fonts import Fonts as Fonts

# circulos de fondo de la pagina
dots : dict = {
    "@keyframes dots": {
        "0%": {"background_position": "0 0"},
        "100%": {"background_position": "40px 40px"}
    },
    "animation" : "dots 4s linear infinite alternate-reverse both",
}

# Tamaños 
class Size(Enum):
    ZERO = ["0px !important"]
    SMALL = ["0.5em", "0.6em", "0.7em", "0.8em", "1em"]
    MEDIUM = ["0.8em", "0.9em", "1em", "1.1em", "1.2em"]
    DEFAULT = ["1em", "1.1em", "1.2em", "1.3em", "1.4em"]
    LARGE = ["1.5em", "1.6em", "1.7em", "1.8em", "1.9em"]
    BIG = ["2em", "2.1em", "2.2em", "2.3em", "2.4em"]
    VERY_BIG = ["4em", "4.1em", "4.2em", "4.3em", "4.5em"] 


# Estilos base de la pagina
BASE_STYLE = {
    "font_family": Fonts.DEFAULT.value,
    
    # background
    "_light":{"background" : "radial-gradient(circle, rgba(0,0,0,0.35) 1px, transparent 1px)","background_size" : "25px 25px"},
    "background" : "radial-gradient(circle, rgba(255,255,255,0.09) 1px, transparent 1px)",
    "background_size" : "25px 25px",
    "style":dots,
}

# Estilos de componentes

# componentes de navbar 
hstack_navbar_style= dict(
        font_size=Size.SMALL.value,
        spacing="2em",
        width="100%",
        height="50px",
        padding=["0rem 1rem", "0rem 1rem", "0rem 1rem", "0rem 8rem", "0rem 8rem"],
        position="fixed",
        top="0px",
        z_index="10",

)


