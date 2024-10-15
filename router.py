# import flet as ft
# import path
# from pages.login import LoginPage
# from pages.signup import SignupPage
#
#
# class Routing:
#     pass
#
#
# class Router:
#     def __int__(self, page: ft.Page):
#         self.page = page
#         self.app_router = [
#             path(url="/", clear = True, view = LoginPage().view),
#             path(url="/signup", clear=True, view=SignupPage().view),
#
#         ],
#         Routing(
#             page = self.page,
#             app_router = self.app_router,
#         )
#
#         self.page.go(self.page.route)

import flet as ft
from pages.login import LoginPage
from pages.signup import SignupPage

class Router:
    def __init__(self, page: ft.Page):
        self.page = page

        # Route change handler
        def route_change(route):
            self.page.views.clear()

            # Define the routing logic based on the URL
            if route == "/signup":
                self.page.views.append(SignupPage().view(self.page))
            else:
                self.page.views.append(LoginPage().view(self.page))

            self.page.update()

        # Pop view handler (for navigating back)
        def view_pop(view):
            self.page.views.pop()
            self.page.update()

        # Assign route and pop handlers
        self.page.on_route_change = route_change
        self.page.on_view_pop = view_pop

        # Navigate to the current route
        self.page.go(self.page.route)
