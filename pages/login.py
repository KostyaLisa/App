import flet as ft
from utils.style import *



class LoginPage:


    email_input = ft.Container(
        content= ft.TextField(label="Email",
                              bgcolor=secondaryBqColor,
                              border=ft.InputBorder.NONE,
                              filled=True,
                              color=secondaryFontColor,
                              ),
        border_radius=15
    )

    def view(self,page: ft.Page):
        page.title = "Page authorization"
        page.window.width = defaultWidthWindows
        page.window.height = defaultHeightWindows
        page.window.min_width = 800
        page.window.min_height = 400

        return ft.View(
            "/",
            controls=[
                # ft.Text("Login"),
                # ft.ElevatedButton("Page Registration", on_click=lambda e: page.go("/signup")),

                # NEXT Step

                # self.email_input

            #     next step
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                            expand=2,
                            padding =ft.padding.all(40),
                            content = ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
        )
                        )
                    ]
                )
            ]
        )

