import tkinter as tk        # Импорт библиотеки tkinter
from tkinter import ttk     # Из библиотеки tkinter достаём ttk
import sqlite3              # Импорт  библиотеки sqlite3


class Main(tk.Frame):
    def __init__(self, root):                               # Конструктор класса
        super().__init__(root)                              # Передаём все методы, все функции, все свойства класса tk
        self.init_main()                                    # Вызываем метод init_main
        self.db = db                                        # Объявляем переменную в классе
        self.view_records()                                 # Вызываем метод view_records

    def init_main(self):                                    # Метод со всеми графическими элементами(поля,кнопки)

                                                            #Frame = виджет для группировки и организации других виджетов в окне приложения
        toolbar = tk.Frame(bg="#d7d8e0", bd=2)              # Установили цвет фона рамки и ширину рамки
        toolbar.pack(side=tk.TOP, fill=tk.X)                # Размещаем в окне


        self.add_img = tk.PhotoImage(file="./img/add.png")  # Загрузили изображение кнопки добавление в переменнную
        # Создали кнопку
        # 1 - привязали к панели инструментов
        # 2- установили цвет фона
        # 3- установили размер рамки
        # 4- установили иконку
        # 5- вызываем функцию,которая сработает при нажатии этой кнопки
        btn_open_dialog = tk.Button(
            toolbar, bg="#d7d8e0", bd=0, image=self.add_img, command=self.open_dialog
        )
        btn_open_dialog.pack(side=tk.LEFT)                  # Размещение кнопку в окне, указывавая гду она(кнопка) будет находиться

        # Создаём таблицу с колонками:"ID", "name", "tel", "email". Указываем высоту и скрываем пустую(нулевую) колонку
        self.tree = ttk.Treeview(
            self, columns=("ID", "name", "tel", "email","salary"), height=45, show="headings"
        )

        self.tree.column("ID", width=30, anchor=tk.CENTER)          # В колонке таблицы указываем имя, ширину и выравнивание( в данном случае по центру)
        self.tree.column("name", width=300, anchor=tk.CENTER)       # В колонке таблицы указываем имя, ширину и выравнивание( в данном случае по центру)
        self.tree.column("tel", width=150, anchor=tk.CENTER)        # В колонке таблицы указываем имя, ширину и выравнивание( в данном случае по центру)
        self.tree.column("email", width=150, anchor=tk.CENTER)      # В колонке таблицы указываем имя, ширину и выравнивание( в данном случае по центру)
        self.tree.column("salary", width=90, anchor=tk.CENTER)      # В колонке таблицы указываем имя, ширину и выравнивание( в данном случае по центру)

        self.tree.heading("ID", text="ID")                          # Устанавливаем текст заголовка( название колонки, новое название колонки)
        self.tree.heading("name", text="ФИО")                       # Устанавливаем текст заголовка( название колонки, новое название колонки)
        self.tree.heading("tel", text="Телефон")                    # Устанавливаем текст заголовка( название колонки, новое название колонки)
        self.tree.heading("email", text="E-mail")                   # Устанавливаем текст заголовка( название колонки, новое название колонки)
        self.tree.heading("salary", text="Зарплата")                # Устанавливаем текст заголовка( название колонки, новое название колонки)

        self.tree.pack(side=tk.LEFT)                                # Размещение таблицы в окне


        self.update_img = tk.PhotoImage(file="./img/update.png")    # Загрузили изображение кнопки обновления в переменнную
        # Создали кнопку
        # 1- привязали к панели инструментов
        # 2- установили цвет фона
        # 3- установили размер рамки
        # 4- установили иконку
        # 5- вызываем функцию,которая сработает при нажатии этой кнопки
        btn_edit_dialog = tk.Button(
            toolbar,
            bg="#d7d8e0",
            bd=0,
            image=self.update_img,
            command=self.open_update_dialog,
        )
        btn_edit_dialog.pack(side=tk.LEFT)                          # Размещение кнопку в окне, указывавая гду она(кнопка) будет находиться


        self.delete_img = tk.PhotoImage(file="./img/delete.png")    # Загрузили изображение кнопки обновления в переменнную
        # Создали кнопку
        # 1 - привязали к панели инструментов
        # 2- установили цвет фона
        # 3- установили размер рамки
        # 4- установили иконку
        # 5- вызываем функцию,которая сработает при нажатии этой кнопки
        btn_delete = tk.Button(
            toolbar,
            bg="#d7d8e0",
            bd=0,
            image=self.delete_img,
            command=self.delete_records,
        )
        btn_delete.pack(side=tk.LEFT)                               # Размещение кнопку в окне, указывавая гду она(кнопка) будет находиться


        self.search_img = tk.PhotoImage(file="./img/search.png")    # Загрузили изображение кнопки обновления в переменнную
        # Создали кнопку
        # 1 - привязали к панели инструментов
        # 2- установили цвет фона
        # 3- установили размер рамки
        # 4- установили иконку
        # 5- вызываем функцию,которая сработает при нажатии этой кнопки
        btn_search = tk.Button(
            toolbar,
            bg="#d7d8e0",
            bd=0,
            image=self.search_img,
            command=self.open_search_dialog,
        )
        btn_search.pack(side=tk.LEFT)                                                   # Размещение кнопку в окне, указывавая гду она(кнопка) будет находиться

    def open_dialog(self):                                                              # Метод open_dialog
        Child()                                                                         # Вызвали класс, отвечающий за добавление данных в ьазу данных

    def records(self, name, tel, email,salary ):
        self.db.insert_data(name, tel, email,salary )                                   #Вызвали функцию добавления данных в базу данных
        self.view_records()                                                             #Вызвали функцию обновления данных и вывода данных на окно

    def view_records(self):
        self.db.cursor.execute("SELECT * FROM Employees")                               #Запрос: Выбираем все данные из таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]                         #Старые данные удаляем
        [self.tree.insert("", "end", values=row) for row in self.db.cursor.fetchall()]  #Вписываем новые данные в бд

    def open_update_dialog(self):
        Update()                                                                        # Вызываем класс

    def update_records(self, name, tel, email, salary):
        self.db.cursor.execute(                                                         # Запрос на обновление
            """UPDATE Employees SET name=?, tel=?, email=?, salary=? WHERE id=?""",

            # Передаём аргуметы на места "?"(первую выделенную строку, берём значение первого столбца)
            (name, tel, email,salary, self.tree.set(self.tree.selection()[0], "#1")),
        )
        self.db.conn.commit()                                                           # Сохраняем запрос
        self.view_records()                                                             # Вызываем функцию класса

    def delete_records(self):
        for selection_items in self.tree.selection():
            self.db.cursor.execute(                                                     # Запрос на удаление строки с таким-то id
                "DELETE FROM Employees WHERE id=?", (self.tree.set(selection_items, "#1"))     # Передаём аргумет на место "?"
            )
        self.db.conn.commit()                                                           # Сохраняем запрос
        self.view_records()                                                             # Вызываем функцию класса

    def open_search_dialog(self):
        Search()                                                                        # Вызываем класс

    def search_records(self, name):
        name = "%" + name + "%"                                                         # Доюавляем к строчке знаки процента
        self.db.cursor.execute("SELECT * FROM Employees WHERE name LIKE ?", (name,))    # Сюда передаем кортеж (name), а не просто name

        [self.tree.delete(i) for i in self.tree.get_children()]                         # Старые данные удаляем
        [self.tree.insert("", "end", values=row) for row in self.db.cursor.fetchall()]  # Вписываем новые данные в бд


class Child(tk.Toplevel):                                   # Дочерний класс
    def __init__(self):                                     # Конструктор класса
        super().__init__(root)                              # Передаём все методы, все функции, все свойства класса tk
        self.init_child()                                   # Вызов метода init_child
        self.view = app

    def init_child(self):
        self.title("Добавить сотрудника")                   # Указали название заголовка
        self.geometry("400x220")                            # Установили размер экземпляра Tk
        self.resizable(False, False)                        # Установили ограничения изменеия размеров окна

        self.grab_set()                                     # Захватываем весь пользовательский ввод
        self.focus_set()                                    # Устанавливаем фокус на  нужном виджете, когда основное окно находится в фокусе.

        label_name = tk.Label(self, text="ФИО:")            #Создание формы для ФИО
        label_name.place(x=50, y=50)                        #Указали координаты формы ФИО
        label_select = tk.Label(self, text="Телефон:")      #Создание формы для Телефона
        label_select.place(x=50, y=80)                      #Указали координаты формы Телефон
        label_sum = tk.Label(self, text="E-mail:")          #Создание формы для E-mail
        label_sum.place(x=50, y=110)                        #Указали координаты формы E-mail

        label_salary = tk.Label(self, text="Зарплата:")          #Создание формы для E-mail
        label_salary.place(x=50, y=140)                        #Указали координаты формы E-mail


        self.entry_name = ttk.Entry(self)                   #Создали поле для ввода формы ФИО
        self.entry_name.place(x=200, y=50)                  #Указади координаты поля для ввода формы ФИО
        self.entry_email = ttk.Entry(self)                  #Создали поле для ввода формы  E-mail
        self.entry_email.place(x=200, y=80)                 #Указали координаты поля для ввода формы E-mail
        self.entry_tel = ttk.Entry(self)                    #Создали поле для ввода формы Телефон
        self.entry_tel.place(x=200, y=110)                  #Указали координаты поля для ввода формы Телефон

        self.entry_salary = ttk.Entry(self)                    #Создали поле для ввода формы Телефон
        self.entry_salary.place(x=200, y=140)                  #Указали координаты поля для ввода формы Телефон

        #Создали кнопку закрытия дочернего класса. Указали тект на кнопке и команду, которая выполниться пр нажатии этой кнопки
        # self.destroy - закрытие нынешнего окна
        #Указали её расположение(координаты)
        self.btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        self.btn_cancel.place(x=220, y=170)

        #Создали кнопку для добавления текста и указали её расположение(координаты)
        self.btn_ok = ttk.Button(self, text="Добавить")
        self.btn_ok.place(x=300, y=170)

        #Отслеживаем событие, при котором сработает кнопка ДОБАВИТЬ.
        #Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию records и передаём ей информацию из полей: name, email,tel
        self.btn_ok.bind(
            "<Button-1>",
            lambda event: self.view.records(
                self.entry_name.get(), self.entry_email.get(), self.entry_tel.get(), self.entry_salary.get()
            ),
        )


class Update(Child):
    def __init__(self):                                             # Конструктор класса
        super().__init__()                                          # Передаём все методы, все функции, все свойства класса tk
        self.init_edit()                                            # Вызываем метод init_edit
        self.view = app                                             # Объявляем переменную в классе
        self.db = db                                                # Объявляем переменную в класе
        self.default_data()                                         # Вызываем метод default_data

    #Метод редактирования данных в бд
    def init_edit(self):
        self.title("Редактирование данных сотрудника")               #Указали название заголовка
        btn_edit = ttk.Button(self, text="Редактировать")            #Создали кнопку и укзали текст на ней
        btn_edit.place(x=205, y=170)                                 #Указали координаты кнопки

        #Отслеживаем событие, при котором сработает кнопка ИЗМЕНИТЬ.
        #Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию update_records
        #и передаём ей информацию из полей: name, email,tel
        btn_edit.bind(
            "<Button-1>",
            lambda event: self.view.update_records(
                self.entry_name.get(), self.entry_email.get(), self.entry_tel.get(), self.entry_salary.get()
            ),
        )

        #Отслеживаем событие, при котором сработает кнопка .
        #Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию destroy к самой кнопке
        # add='+'  - соединяем две функции bind этой кнопки
        btn_edit.bind(
            "<Button-1>",
            lambda event: self.destroy(), add="+"
        )

        self.btn_ok.destroy()                                               #Закрываем кнопку btn_ok

    def default_data(self):
        self.db.cursor.execute(                                             # Запрос на выбор всех полей с таким-то id
            "SELECT * FROM Employees WHERE id=?",
            self.view.tree.set(self.view.tree.selection()[0], "#1"),        #Выбираем id выделенной строки
        )
        row = self.db.cursor.fetchone()                         # Получаем первую запись
        self.entry_name.insert(0, row[1])                       # Передаём значение в поле из этой записи
        self.entry_email.insert(0, row[2])                      # Передаём значение в поле из этой записи
        self.entry_tel.insert(0, row[3])                        # Передаём значение в поле из этой записи
        self.entry_salary.insert(0,row[4])



class Search(tk.Toplevel):
    def __init__(self):                                         # Конструктор класса
        super().__init__()                                      # Передаём все методы, все функции, все свойства класса tk
        self.init_search()                                      # Вызываем метод init_search
        self.view = app                                         # Объявили переменную в классе

    def init_search(self):
        self.title("Поиск сотрудника")                          #Указали название заголовка
        self.geometry("300x100")                                # Установили размер экземпляра Tk
        self.resizable(False, False)                            # Установили ограничения изменеия размеров окна

        label_search = tk.Label(self, text="Имя:")              #Создание формы для поиска ФИО
        label_search.place(x=50, y=20)                          #Указали координаты формы для поиска по ФИО

        self.entry_search = ttk.Entry(self)                     #Создали поле для ввода формы поиска по  ФИО
        self.entry_search.place(x=100, y=20, width=150)         #Указали координаты поля для ввода формы поиска по  ФИО

        # Создали кнопку, указали текст на ней и функцию, которая вызовется по нажатию на ней. Указали координаты кнопки
        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        # Создали кнопку, указали текст на ней. Указали координаты кнопки
        search_btn = ttk.Button(self, text="Найти")
        search_btn.place(x=105, y=50)

        #Отслеживаем событие, при котором сработает кнопка ПОИСК.
        #Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию search_records
        # И передаём ей информацию из поля entry_search
        search_btn.bind(
            "<Button-1>",
            lambda event: self.view.search_records(self.entry_search.get()),
        )
        #Отслеживаем событие, при котором сработает кнопка .
        #Нажимая левой кнопкой мыши по этой кнопке мы вызываем функцию destroy к самой кнопке
        search_btn.bind("<Button-1>", lambda event: self.destroy(), add="+")



class DB:
    def __init__(self):                                                                 # Конструктор класса
        self.conn = sqlite3.connect("db.db")                                            # Создание соединения с базой данных(имя бд)
        self.cursor = self.conn.cursor()                                                # Вызываем курсор бд
        self.cursor.execute(                                                            # Запрос на создание бд
            '''
            CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            tel TEXT NOT NULL,
            email TEXT NOT NULL,
            salary INTEGER
            )
            '''
        )
        self.conn.commit()                                                                                  # Сохраняем запрос
        self.data()

    # Метод для добавленияя изначальных данных в бд
    def data(self):
        insert_into = 'INSERT INTO Employees (name, tel, email, salary) VALUES (?, ?, ?, ?)'


        user_data=('Tom', '+19887983255', 'tom@gmail.com','120')
        user_data1=('Johan', '+79887123455', 'johan@gmail.com','120')
        user_data2=('James', '+19887776655', 'james@yandex.com','120')
        user_data3=('Henry', '+79885425954', 'henry@gmail.com','120')
        user_data4=('Owen', '+89212347232', 'owen@yandex.com','120')
        self.cursor.execute(insert_into,user_data )
        self.cursor.execute(insert_into,user_data1 )
        self.cursor.execute(insert_into,user_data2 )
        self.cursor.execute(insert_into,user_data3 )
        self.cursor.execute(insert_into,user_data4 )

        self.conn.commit()                                                                                          # Сохраняем запрос


    def insert_data(self, name, tel, email, salary):                                                                # Метод для добавленияя наших данных в таблицу
        self.cursor.execute(                                                                                        # Запрос на создание бд
            """INSERT INTO Employees(name, tel, email, salary) VALUES(?, ?, ?, ?)""", (name, tel, email, salary)    # передаём аргументы на места '?'
        )
        self.conn.commit()                                                                                          # Сохраняем запрос

if __name__ == "__main__":
    root = tk.Tk()                                  # Создали экземпляр Tk
    db = DB()                                       # Создание экземпляра класса с базой данных
    app = Main(root)                                # Передали экземпляр Tk в класс Main
    app.pack()                                      # Размещение app в окне
    root.title("Список сотрудников компании")       # Установили заголовок экземпляра Tk
    root.geometry("765x450")                        # Установили размер экземпляра Tk
    root.resizable(False, False)                    # Установили ограничения изменеия размеров окна
    root.mainloop()                                 # Запуск основного цикла обработки событий
    
# Код готов