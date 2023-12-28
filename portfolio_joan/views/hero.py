import reflex as rx

from portfolio_joan.styles.styles import Size as Size
from portfolio_joan.components.social_media import social_media
import portfolio_joan.styles.styles as styles

# hero

def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack( 
            rx.heading(
                    "Hi - I'm Joan Martinez",
                    font_size=Size.TITLE_HERO.value,
                    font_weight="900",
                    _dark={
                        "background": "linear-gradient(to right, #e1e1e1, #f9cd45)",
                        "background_clip": "text",
                    },
                ),
                rx.heading(
                    "👋", 
                    size="2xl", 
                    style=styles.style_hand, 
                ),
            ),
            rx.text("Apps to contact me", font_size=Size.LARGE.value), 
            social_media(),
            align_items="center",
            padding_top="15em"
        ),

        rx.vstack(
            rx.link(
                rx.vstack( 
                    rx.text("more about me", font_size=Size.SMALL.value),  
                    rx.icon(tag="arrow_down", box_size=Size.MEDIUM.value, class_name="animate-bounce"),
                    style=styles.no_hover_style,
                ),
                href="#about-me",
                align_items="center",
            ),
            padding_top="15em"
        ),
        style=styles.vstack_hero_style
    )

