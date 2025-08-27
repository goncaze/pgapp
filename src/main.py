import flet as ft
import pg8000


def main(page: ft.Page):

    # Mesma funcionalidade, sem dependências C
    conn = pg8000.connect(
        host="aws-1-sa-east-1.pooler.supabase.com",
        port=6543,
        database="postgres",
        user="postgres.yneqljutudrbiacihmxw",
        password="ORHAz33BTMcSJE27",
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM evento")
    rows = cursor.fetchall()

    coluna = ft.Column()
    for record in rows:
        coluna.controls.append(ft.Text(value=record))
        print(record)

    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            content=coluna,
            expand=True,
        )
    )


ft.app(main)
