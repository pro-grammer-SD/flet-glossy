import flet as ft

from flet_glossy import FletGlossyContainer

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletGlossyContainer(
                    tooltip="My new FletGlossy Control tooltip",
                    value = "My new FletGlossy Flet Control", 
                ),),

    )

ft.app(main)
