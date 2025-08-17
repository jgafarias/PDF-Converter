import flet as ft

def main(page: ft.Page):
    page.title = "Conversor de PDF"
    page.window.width = 500
    page.window.height = 500

    # Função chamada quando o usuário escolhe um arquivo
    def on_file_selected(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            selected_file.value = f"Arquivo selecionado: {file_path}"
        else:
            selected_file.value = "Nenhum arquivo selecionado"
        page.update()

    # Cria o FilePicker e adiciona ao overlay da página
    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)

    # Texto que vai mostrar o arquivo selecionado
    selected_file = ft.Text("Arquivo ()")

    # Botão que abre o FilePicker
    picker_button = ft.IconButton(
        icon=ft.Icons.FOLDER,
        tooltip="Selecionar arquivo",
        on_click=lambda _: file_picker.pick_files()
    )

    # Coloca os widgets dentro de uma coluna
    page.add(ft.Row([selected_file, picker_button]))

ft.app(target=main)
