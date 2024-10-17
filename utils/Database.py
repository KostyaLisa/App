import sqlite3
import flet as ft


class Database:

    def init_db(self):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()

        # Обновляем таблицу пользователей
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            login TEXT NOT NULL UNIQUE
        )
    ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            description TEXT NOT NULL,
            priority TEXT CHECK( priority IN ('high', 'medium', 'low') ) NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    ''')

        conn.commit()
        conn.close()

    def check_email(login, email):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()

        # Проверяем, есть ли пользователь с таким логином или почтой
        cursor.execute("SELECT * FROM users WHERE login = ? OR email = ?", (login, email))
        user = cursor.fetchone()

        conn.close()
        return user is not None

    # def check_register_user(username, login, email):
    #     if is_login_or_email_taken(login, email):
    #         return False  # Логин или почта уже заняты
    #
    #     conn = sqlite3.connect('tasks.db')
    #     cursor = conn.cursor()
    #
    #     cursor.execute("INSERT INTO users (username, login, email) VALUES (?, ?, ?)", (username, login, email))
    #     conn.commit()
    #     conn.close()

    # return True  # Успешная регистрация

    # def fun(self):
    #     # Инициализация базы данных
    #     self.init_db()
    #
    #     # Элементы интерфейса для регистрации
    #     username_input = ft.TextField(label="Имя пользователя")
    #     login_input = ft.TextField(label="Логин")
    #     email_input = ft.TextField(label="Email")
    #     register_message = ft.Text()
    #
    #     # Элементы интерфейса для задач
    #     task_input = ft.TextField(label="Описание задачи")
    #     priority_dropdown = ft.Dropdown(
    #         label="Приоритет",
    #         options=[
    #             ft.dropdown.Option("high", "Высокий"),
    #             ft.dropdown.Option("medium", "Средний"),
    #             ft.dropdown.Option("low", "Низкий"),
    #         ],
    #     )
    #     tasks_list = ft.Column()
    #
    #     # Обновление списка задач на экране
    #     def update_task_list():
    #         tasks_list.controls.clear()
    #         tasks = get_tasks_sorted(login_input.value)
    #         for task_id, description, priority in tasks:
    #             tasks_list.controls.append(
    #                 ft.Row(
    #                     [
    #                         ft.Text(f"{description} ({priority})"),
    #                         ft.IconButton(
    #                             icon=ft.icons.DELETE,
    #                             on_click=lambda e, task_id=task_id: handle_delete_task(task_id),
    #                         )
    #                     ]
    #                 )
    #             )
    #         page.update()
    #
    #     # Добавление задачи
    #     def handle_add_task(e):
    #         if login_input.value and task_input.value and priority_dropdown.value:
    #             add_task(login_input.value, task_input.value, priority_dropdown.value)
    #             update_task_list()
    #
    #     # Удаление задачи
    #     def handle_delete_task(task_id):
    #         delete_task(task_id)
    #         update_task_list()
    #
    #     # Обработка регистрации
    #     def handle_register(e):
    #         if username_input.value and login_input.value and email_input.value:
    #             if register_user(username_input.value, login_input.value, email_input.value):
    #                 register_message.value = "Регистрация прошла успешно!"
    #                 register_message.color = "green"
    #             else:
    #                 register_message.value = "Логин или почта уже заняты."
    #                 register_message.color = "red"
    #             page.update()
    #
    #     # Интерфейс страницы
    #     page.add(
    #         ft.Column(
    #             [
    #                 ft.Text("Регистрация пользователя"),
    #                 username_input,
    #                 login_input,
    #                 email_input,
    #                 ft.ElevatedButton("Зарегистрироваться", on_click=handle_register),
    #                 register_message,
    #                 ft.Divider(height=20, thickness=2),  # Разделитель между секциями
    #                 ft.Text("Добавить задачу"),
    #                 task_input,
    #                 priority_dropdown,
    #                 ft.ElevatedButton("Добавить задачу", on_click=handle_add_task),
    #                 ft.Text("Список задач"),
    #                 tasks_list,
    #             ]
    #         )
    #     )
