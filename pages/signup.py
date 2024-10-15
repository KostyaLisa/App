import flet as ft



class SignupPage:

    def view(self, page: ft.Page):
        page.title = "Page registration"

        return ft.View(
            "/",
            controls=[
                ft.Text("Registration"),
                ft.ElevatedButton("Page authorization", on_click=lambda e: page.go("/login")),

            ]
        )

