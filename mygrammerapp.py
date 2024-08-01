import flet as ft
from correctinggrammer import StandardEnglish

def main(page: ft.Page):
    page.title = "Correct My Grammar"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.window.width = 700
    page.window.height = 600


    logo = ft.Image(src=f"assets/logo.jpg", width=300)
    user_input = ft.TextField(
        hint_text="Enter any sentence...",
        border_radius=30,
        expand=True,
        multiline=True,
        width=600,
        height=300
    )
    outputText = ft.Text(
        "Your response will be generated here....",
        text_align="start",
        width=600,
        no_wrap=False,
        
    )

    def result(e):
        answer = StandardEnglish(str(user_input.value)).convert()
        outputText.value = answer
        page.update()
 
    outputContainer = ft.Container(
        content=outputText,
        margin=20,
        padding=20,
        bgcolor="#f2f2f2",
        border_radius=30,
        width=600
    )
    

    page.add(
       
            logo,
            user_input,
            ft.ElevatedButton("Submit", on_click=result),
            outputContainer,
            ft.Image(src=f"assets/children_happy.jpg", width=500)
        
    )

ft.app(target=main, assets_dir="assets")
