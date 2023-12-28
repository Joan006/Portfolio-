import reflex as rx

config = rx.Config(
    app_name="portfolio_joan",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)
