import flet as ft
import time
from pages.login import LoginPage
from utils.Database import Database

from utils.style import *
from utils.Validation import Validation


class SignupPage:

    validators =  Validation()

    def __init__(self):
        # Defining input fields correctly
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
        self.login_input = ft.Container(
            content=ft.TextField(
                label="Login",
                bgcolor=secondaryBqColor,
                border=ft.InputBorder.NONE,
                filled=True,
                color=secondaryFontColor,
            ),
            border_radius=15,
        )
        self.password_input = ft.Container(
            content=ft.TextField(
                label="Password",
                password=True,
                can_reveal_password=True,
                bgcolor=secondaryBqColor,
                border=ft.InputBorder.NONE,
                filled=True,
                color=secondaryFontColor,
            ),
            border_radius=15,
        )
        self.confirm_password_input = ft.Container(
            content=ft.TextField(
                label="Confirm Password",
                password=True,
                can_reveal_password=True,
                bgcolor=secondaryBqColor,
                border=ft.InputBorder.NONE,
                filled=True,
                color=secondaryFontColor,
            ),
            border_radius=15,
        )
        self.error_field= ft.Text('', color='red')

    def view(self, page: ft.Page):
        page.title = "Page Registration"
        page.window.width = defaultWidthWindows
        page.window.height = defaultHeightWindows
        page.window.min_width = 800
        page.window.min_height = 400

        # Load custom fonts
        page.fonts = {"muller-extrabold": "fonts/muller-extrabold.ttf"}



        def signup(e):
            email_value= self.email_input.content.value
            login_value = self.login_input.content.value
            password_value = self.password_input.content.value
            confirm_password_value = self.confirm_password_input.content.value
            # print(email_value,login_value,password_value,confirm_password_value)
            if email_value and login_value and password_value and confirm_password_value:
                db = Database()
                if not self.validators.is_valid_email(email_value):
                    self.email_input.content.bgcolor= inputBqErrorColor
                    self.error_field.value = 'field Email not valid'
                    self.error_field.size = 12
                    self.email_input.update()
                    self.error_field.update()
                    time.sleep(1)
                    self.error_field.size=0
                    self.email_input.content.bgcolor= inputBgColor
                    self.error_field.update()
                    self.email_input.update()
                elif db.check_email(email_value):
                    self.email_input.content.bgcolor = inputBqErrorColor
                    self.error_field.value = 'This email it belongs'
                    self.error_field.size = 12
                    self.email_input.update()
                    self.error_field.update()
                    time.sleep(1)
                    self.error_field.size = 0
                    self.email_input.content.bgcolor = inputBgColor
                    self.error_field.update()
                    self.email_input.update()

                elif not self.validators.is_valid_password(password_value):
                    self.password_input.content.bgcolor = inputBqErrorColor
                    self.error_field.value = 'field Password not valid'
                    self.error_field.size = 12
                    self.password_input.update()
                    self.error_field.update()
                    time.sleep(1)
                    self.error_field.size = 0
                    self.password_input.content.bgcolor = inputBgColor
                    self.error_field.update()
                    self.password_input.update()
                elif password_value != confirm_password_value:
                    self.error_field.value="Passwords do not equal"
                    self.error_field.size = 12
                    self.error_field.update()
                    time.sleep(1)
                    self.error_field.size = 0
                    self.error_field.update()

                else:
                    # Redirect to login page
                    self.error_field.value = "You have Register"

                    self.error_field.size = 12
                    self.error_field.color = ft.colors.GREEN
                    self.error_field.update()
                    time.sleep(4)
                    page.go("/")
            else:
                self.error_field.value = "All fields are required!"
                self.error_field.update()
                time.sleep(1)
                self.error_field.size = 0
                self.error_field.update()

        return ft.View(
            "/",
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        # Left panel
                        ft.Container(
                            expand=2,
                            padding=ft.padding.all(40),
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "Welcome to Registration",
                                        color=defaultFontColor,
                                        size=25,
                                        font_family="prisma-pro-shadow",
                                    ),
                                    self.error_field,
                                    self.email_input,
                                    self.login_input,
                                    self.password_input,
                                    self.confirm_password_input,
                                    ft.Container(
                                        content=ft.Text("Register", color=defaultFontColor),
                                        alignment=ft.alignment.center,
                                        height=40,
                                        bgcolor=hoverBqColor,
                                        on_click=lambda e: signup(e)
                                    ),
                                ]
                            )
                        ),
                        # Right panel with background image
                        ft.Container(
                            expand=3,
                            image_src="images/bg_login.jpg",
                            image_fit=ft.ImageFit.COVER,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(
                                        name=ft.icons.VERIFIED_USER_ROUNDED,
                                        color=hoverBqColor,
                                        size=140,
                                    ),
                                    ft.Text(
                                        "Form Registration",
                                        color=hoverBqColor,
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                        font_family="muller-extrabold",
                                    ),
                                ]
                            ),
                        ),
                    ]
                )
            ],
            bgcolor=defaultBqColor,
            padding=0
        )

