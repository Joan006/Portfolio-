import reflex as rx

from portfolio_joan.styles.styles import Size as Size
from portfolio_joan.components.social_media import social_media
import portfolio_joan.styles.styles as styles

# hero

def hero() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.avatar(
            name = "Joan Martinez",
            src="me2.jpg", 
            show_border=True,
            size="xl",
            box_shadow = "0 0 9px #f9cd45"
            ),
            rx.hstack( 
            rx.heading(
                    "Hi - I'm Joan Martinez",
                    font_size=Size.TITLE_HERO.value,
                    font_weight="900",
                    style=styles.heading_style
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
            padding_top="13em"
        ),

        rx.vstack(
            rx.link(
                rx.vstack( 
                    rx.text("more about me", font_size=Size.SMALL.value),  
                    rx.icon(tag="arrow_down", box_size=Size.MEDIUM.value, class_name="animate-bounce"),
                ),
                href="#about-me",
                align_items="center",
            ),
            padding_top="15em"
        ),
        style=styles.vstack_hero_style
    )

