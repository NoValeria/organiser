from utility.my_date import *
import mysql.connector

from utility.note import Note


class NoteLoader(object):
    '''Данный класс позволяет загружать заметки из базы данных'''
    def __init__(self):
        # создаём соединение с базой данных с помощью дополнительных параметров соединения
        self.conn = mysql.connector.connect(host='localhost', database='organaiser', user='root', password='QWERTY123')
        self.cursor = self.conn.cursor()   # создаём cursor, являющийся специальным объектом, который делает запросы и получает их результаты.

    def upload(self, new_note: Note):
        '''Формирует запрос к базе данных.'''
        # Формируется строка request, в которой лежит текст запроса.
        #  Данный запрос добавляет в таблицу notes в базе данных organiser
        # значения day, month, year, start_time, end_time, title,
        # description, week_number, day_of_week.
        # Т.к. вначале значения этих полей не известны, то они прописываются как %s, строка.
        # Таким образом, в базе данных всё хранится в виде строк.
        request = "INSERT INTO organiser.notes (day, month, year, start_time, end_time, title, description, "
        request += "week_number, day_of_week) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        print(request)
        print("ready")
        try:
            # в метод execute() передаётся строка request и результат метода to_mysql_list(),
            # выполненного на объекте new_note.
            # Таким образом, метод execute() поставит элементы из списка,
            # который возвращает функция to_mysql_list(), на место %s.
            # В следующей строке кода регистрируется изменение в базе данных.
            self.cursor.execute(request, new_note.to_mysql_list())
            self.conn.commit()
        except Exception as e:
            print(e)


    def load_notes_by_week_number(self, selected_date: MyDate):

        '''
            данный метод получает на вход дату типа MyDate
            возвращет двумерный массив, который представляет собой 7 массивов для каждого дня недели,
            в каждом из которых содержится массив заметок для каждого дня
        '''

        # Формируется запрос на заметки с указанным годом и указанным номером недели.
        request = "SELECT * FROM notes WHERE week_number = '"
        request += str(selected_date.get_number_of_week()) + "' AND `year` = '"
        request += str(selected_date.get_year()) + "';"

        # Функции execute передаётся только строку request,
        # т.к. все параметры находятся в самом запросе
        self.cursor.execute(request)
        array = [[]] # создаём двумерный массив, элементами которого являются 7 одномерных массивов
        for i in range(7):
            array.append([])

        # Получаем результаты по одному, используя метод курсора .fetchone()
        # Он всегда возвращает кортеж или None. если запрос пустой
        row = self.cursor.fetchone()

        while row is not None:
            n = Note()   # Создаём новую заметку
            n.set_by_database_row(row) # Выделение из списка необходимых данных и занесение в соответсвующие поля
            array[n.get_date().get_number_of_day()].append(n)  # Запонение двумерного массива полученными заметками
            print(row, "\n")
            row = self.cursor.fetchone()  # Переход к следующей строке
        print(array)   # Выводим весь массив на экран
        return array   # Возвращаем как результат функции
