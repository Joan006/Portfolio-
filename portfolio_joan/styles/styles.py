import reflex as rx
from enum import Enum

from reflex.event import background


from .fonts import Fonts as Fonts


# Tamaños
class Size(Enum):
    ZERO = ["0px !important"]
    VERY_SMALL = ["0.5em", "0.5em", "0.6em", "0.6em", "0.6em"]
    SMALL = ["0.7em", "0.7em", "0.8em", "0.8em", "0.85em"]
    MEDIUM = ["0.8em", "0.9em", "1em", "1.1em", "1.2em"]
    DEFAULT = ["1em", "1.1em", "1.2em", "1.3em", "1.4em"]
    LARGE = ["1.3em", "1.5em", "1.7em", "1.8em", "1.9em"]
    BIG = ["1.5em", "1.7em", "2.2em", "2.3em", "2.4em"]
    TITLE_HERO = ["1.5em", "1.7em", "3em", "3.6em", "4em"]
    VERY_BIG = ["2em", "2.7em", "2.8em", "3em", "3.5em"]


# Estilo -> backgroun 
background_style = { 
    "_light": {
        "background": "radial-gradient(circle, rgba(255,255,255,0.35) 1.3px, transparent 1px)",
        "background_size": "20px 20px",
    },
    "background": "radial-gradient(circle, rgba(255,255,255,0.09) 1.3px, rgba(0,0,0,1) 1px)",
    "background_size": "20px 20px",
    "@keyframes dots": {
        "0%": {"background_position": "0 0"},
        "100%": {"background_position": "40px 40px"},
    },
    "animation": "dots 4s linear infinite alternate-reverse both",
}


# Estilos base de la pagina
BASE_STYLE = {
    "font_family": Fonts.DEFAULT.value,
    "button" : {
        "background":"none !important"
    },
    # background
    **background_style,
    
}


# ESTILOS COMPONENTES PAGINA 

# No -> _hover
no_hover_style = {
    ":hover": {
        "text_decoration": "none",  
        "color": "inherit", 
    }
}

# Estilo -> navbar
hstack_navbar_style = dict(
    font_size=Size.MEDIUM.value,
    text_shadow="2px 2px 4px #000000",
    spacing="2em",
    width="100%",
    height="50px",
    padding=["0rem 1rem", "0rem 1rem", "0rem 1rem", "0rem 8rem", "0rem 8rem"],
    position="fixed",
    top="0px",
    z_index="10",
    opacity="0.5",

)


# Estilo -> Hero
vstack_hero_style = dict(
    display="flex",
    flex_direction="column",
    justify_content="center",
    height="100vh",
    margin="auto",
    padding=["0rem 1rem", "0rem 1rem", "0rem 1rem", "0rem 8rem", "0rem 8rem"],
    backgroundAsize="cover",
)

heading_style = {
    "background": "linear-gradient(to right, #e1e1e1, #f9cd45)",
    "background_clip": "text",
}

# Estilo -> avatar   
avatar_style = {
    "border": "0px solid transparent", "border_image": "linear-gradient(to right, #e1e1e1, #f9cd45) 1"
}


# Estilo -> animacion hand
style_hand = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(45deg)"},
        "100%": {"transform": "rotate(-15deg)"},
    },
    "animation": "wave 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite alternate-reverse both",
}

# Card - style
button_title_style = dict ( 
    font_size = Size.VERY_SMALL.value,
)

style_card = dict (
    background = "#000c16",
    padding="1em",
    border_radius="2em", 
    box_shadow = "0 0 8px #2777bb",
    width="9em",
    margin="1em",
    height="17em"
)

div_card_style = dict (
    display = "flex",
    justify_content = "center", 
    aligns_items = "center",
) 

title_card_style = dict (
font_size=Size.SMALL.value,  font_weight="900",
    _dark={"background": "linear-gradient(to right, #e1e1e1, #f9cd45)","background_clip": "text",}
)

# contaiter -> info_me
container_infome_style = dict (
    background_color = "black",
    border_radius="2em", 
    box_shadow = "0 0 8px #2777bb"
)
