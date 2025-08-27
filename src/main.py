import flet as ft
import pg8000


def main(page: ft.Page):

    # Mesma funcionalidade, sem dependências C
    conn = pg8000.connect(
        host="localhost",
        port=5432,
        database="calendario_db",
        user="postgres",
        password="root10",
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM evento")
    rows = cursor.fetchall()

    for record in rows:
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
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
