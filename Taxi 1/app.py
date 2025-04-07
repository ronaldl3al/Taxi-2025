# main.py

import flet as ft
from view.login import LoginPage
from view.menu import MenuPage

import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)

def main(page: ft.Page):
    
    def route_change(route):
        page.views.clear()  # Limpiar las vistas actuales

        
        if page.route == "/login":
            page.views.append(LoginPage(page))
        elif page.route == "/menu":
            page.views.append(MenuPage(page))
        """elif page.route == "/socios":
            page.views.append(SociosPage(page))
        elif page.route == "/vehiculos":
            page.views.append(VehiculosPage(page))
        elif page.route == "/avances":
            page.views.append(AvancesPage(page))
        elif page.route == "/sanciones":
            page.views.append(SancionesPage(page))
        elif page.route == "/finanzas":
            page.views.append(FinanzasPage(page))"""

        page.update()  

   
    page.on_route_change = route_change

   
    page.go("/login")

# app de escritorio
#ft.app(target=main)

# aplicación web

ft.app(target=main, view=ft.WEB_BROWSER)
