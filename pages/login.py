import flet as ft

from utils.style import *


class LoginPage:
    def __init__(self):
        self.email_input = ft.Container(
            content=ft.TextField(
                label="Email",
                bgcolor=secondaryBqColor,
                border=ft.InputBorder.NONE,
                filled=True,
                color=secondaryFontColor,
            ),
            border_radius=15,
        )
        self.password_input = ft.Container(
            content=ft.TextField(
                label="Enter Password",
                password=True,
                can_reveal_password=True,
                bgcolor=secondaryBqColor,
                border=ft.InputBorder.NONE,
                filled=True,
                color=secondaryFontColor,
            ),
            border_radius=15,  # Removed trailing comma here
        )


    def view(self, page: ft.Page):
        # Page setup
        page.title = "Page Authorization"
        page.window.width = defaultWidthWindows
        page.window.height = defaultHeightWindows
        page.window.min_width = 800
        page.window.min_height = 400

        # Define fonts
        page.fonts = {
            "muller-extrabold": "fonts/muller-extrabold.ttf",
            "prisma-pro-shadow": "fonts/prisma-pro-shadow.ttf",
        }
        signup_link = ft.Container(
            content=ft.Text("Create Account", color=defaultFontColor),
            on_click=lambda e: page.go('/signup'),  # Removed trailing comma here
        )
        ft.ElevatedButton("Войти", on_click=lambda _: page.go("/signup"))
        ft.ElevatedButton("Регистрация", on_click=lambda _: page.go("/signup"))

        # Layout
        return ft.View(
            '/',
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        # Left Panel
                        ft.Container(
                            expand=2,
                            padding=ft.padding.all(40),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "Welcome",
                                        color=defaultFontColor,
                                        size=25,
                                        font_family="prisma-pro-shadow",
                                    ),
                                    self.email_input,
                                    self.password_input,
                                    ft.Container(
                                        content=ft.Text("Authorization", color=defaultFontColor),
                                        alignment=ft.alignment.center,
                                        height=40,
                                        bgcolor=hoverBqColor,
                                    ),
                                    signup_link,  # Sign-up link to the sign-up page
                                ],
                            ),
                        ),
                        # Right Panel
                        ft.Container(
                            expand=3,
                            image_src="images/bg_login.jpg",
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(
                                        name=ft.icons.SCREEN_LOCK_PORTRAIT_ROUNDED,
                                        color=hoverBqColor,
                                        size=140,
                                    ),
                                    ft.Text(
                                        "Authorization",
                                        color=hoverBqColor,
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                        font_family="muller-extrabold",
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ],
            bgcolor=defaultBqColor,
            padding=0,
        )
