import flet as ft
import ctypes
from storage.data.generator import Generation

ICON_PATH = "assets\\password_icon.ico"

class PasswordGeneratorUI(ft.Container):
    def __init__(self):
        super().__init__(
            padding=20,
            bgcolor="#121212",
            border_radius=15,
            alignment=ft.alignment.center
        )
        
        self.password_field = ft.TextField(
            value="Ваш пароль",
            read_only=True,
            text_align=ft.TextAlign.CENTER,
            bgcolor="#1E1E1E",
            color="white",
            border_radius=10
        )

        
        self.slider = ft.Slider(
            min=4, max=32, value=12, divisions=7,
            label="{value}",
            active_color="#BB86FC",
            inactive_color="#3A3A3A"
        )

        
        self.include_numbers = ft.Checkbox(label="Числа", value=True, active_color="#BB86FC")
        self.include_letters = ft.Checkbox(label="Буквы", value=True, active_color="#BB86FC")
        self.include_symbols = ft.Checkbox(label="Спецсимволы", value=False, active_color="#BB86FC")

        generate_button = ft.ElevatedButton(
            text="Сгенерировать",
            bgcolor="#BB86FC",
            color="white",
            on_click = self.generate_password
            
        )

        
        self.content = ft.Column(
            [
                ft.Text("Генератор паролей", size=20, weight=ft.FontWeight.BOLD, color="white"),
                self.password_field,
                ft.Text("Длина пароля", color="gray"),
                self.slider,
                ft.Text("Выберите символы:", color="gray"),
                self.include_numbers,
                self.include_letters,
                self.include_symbols,
                generate_button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    


    def generate_password(self, event):
        self.password_field.color = "white"
        try:
            
            length = int(self.slider.value)
            use_numbers = self.include_numbers.value
            use_letters = self.include_letters.value
            use_symbols = self.include_symbols.value

            new_password = Generation(length, use_numbers, use_letters, use_symbols)

            self.password_field.value = new_password
            self.update()

        except ValueError:
            self.password_field.value = "(numbers, letters, symbols) must be True"
            self.password_field.color = "red"
            self.update()

        
        


def main(page: ft.Page):
    page.title = "Генератор паролей"
    page.window.icon = "password_icon.ico"
    page.bgcolor = "#181818"
    page.window.width = 500
    page.window.height = 600

    page.window.resizable = (False, False)
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(PasswordGeneratorUI())

ft.app(target = main)
