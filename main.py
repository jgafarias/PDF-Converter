import flet as ft

def main(page: ft.Page):
    page.title = "Conversor de PDF"
    page.window.width = 500
    page.window.height = 300

    # Função chamada quando o usuário escolhe um arquivo
    def on_file_selected(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            selected_file.value = f"{file_path}"
        else:
            selected_file.value = "Nenhum arquivo selecionado"
        page.update()

    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)

    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)


    def generate_pdf(e):
        page.open(ft.SnackBar(ft.Text("PDF gerado com sucesso!", weight=ft.FontWeight.BOLD), bgcolor=ft.Colors.GREEN))

    title = ft.Text(
        "Conversor PDF",
        size=30,
        weight=ft.FontWeight.BOLD, 
        text_align=ft.MainAxisAlignment.CENTER 
    )
    
    def texto(text_view: str):
        return ft.Text(text_view, size=15, color=ft.Colors.with_opacity(0.3, ft.Colors.WHITE))
    
    save_btn = ft.ElevatedButton(
        "GERAR",
        height=50,
        width=110,
        icon=ft.Icons.PICTURE_AS_PDF_OUTLINED,
        on_click=generate_pdf,
        bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.RED),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            overlay_color=ft.Colors.RED,
            text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK,
            )
        )
    )
    
    # Texto que vai mostrar o arquivo selecionado
    selected_file = ft.TextField(hint_text="Nenhum arquivo selecionado")

    # Botão que abre o FilePicker
    picker_button = ft.IconButton(
        icon=ft.Icons.FOLDER,
        tooltip="Selecionar arquivo",
        on_click=lambda _: file_picker.pick_files()
    )

    # Coloca os widgets dentro de uma coluna
    page.add(ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,       # eixo principal (vertical)
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            title,
            ft.Divider(),
            texto("Selecione o arquivo para converter"),
            ft.Row([selected_file, picker_button], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=10),
            save_btn,
        ],
    ))

ft.app(target=main)
