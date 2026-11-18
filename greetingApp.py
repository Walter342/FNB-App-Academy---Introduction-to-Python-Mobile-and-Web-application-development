import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"

    name_field = ft.TextField(label="Enter your name", width=300)
    greeting_text = ft.Text(size=20)

    def greet_click(e):
        greeting_text.value = f"Hello, {name_field.value}!"
        page.update()

    greet_button = ft.Button("Greet Me", on_click=greet_click)

    page.add(
        ft.Column(
            [
                name_field,
                greet_button,
                greeting_text,
            ]
        )
    )


ft.run(main)