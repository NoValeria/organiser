from exceptions import DatabaseException
from utility import logger
from utility.my_date import *
import mysql.connector

from utility.note import Note

host = "localhost"
database = "organaiser"
user = "root"
password = "QWERTY123"


class NoteLoader(object):
    @staticmethod
    def upload(new_note: Note):
        """данный метод загружает заметку в базу данных"""
        try:
            # Формируется строка request, в которой лежит текст запроса.
            #  Данный запрос добавляет в таблицу notes в базе данных organiser
            # значения day, month, year, start_time, end_time, title,
            # description, week_number, day_of_week.
            # Т.к. в базе данных всё хранится в виде строк, то параметры прописываются как %s, строка.
            request = "INSERT INTO notes (day, month, year, start_time, end_time, title, description, "
            request += "week_number, day_of_week, important) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            # создаём соединение с базой данных с помощью дополнительных параметров соединения
            conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
            # создаём cursor, являющийся специальным объектом, который делает запросы и получает их результаты.
            cursor = conn.cursor()
            cursor.execute(request, new_note.to_mysql_list())
            conn.commit()
        except Exception as e:
            logger.log_exception(e)
            raise DatabaseException("Ошибка про загрузке в базу данных")

    @staticmethod
    def load_notes_by_week_number(selected_date: MyDate):
        """данный метод загружает заметки за неделю, в которой находится дата selected_date"""
        try:
            request = "SELECT * FROM notes WHERE week_number=%s AND `year`=%s;"
            params = (str(selected_date.get_number_of_week()), str(selected_date.get_year()))
            conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
            cursor = conn.cursor()
            cursor.execute(request, params)
            array = [[]]
            for i in range(7):
                array.append([])

            row = cursor.fetchone()

            while row is not None:
                n = Note()
                n.set_by_database_row(row)
                array[n.get_date().get_number_of_day()].append(n)
                row = cursor.fetchone()
            cursor.close()
            conn.close()
            return array
        except Exception as e:
            logger.log_exception(e)
            raise DatabaseException("Ошибка про загрузке из базы данных")

    @staticmethod
    def delete(note: Note):
        """данный метод удаляет заметку из базы данных"""
        try:
            request = "DELETE FROM notes WHERE `day`=%s AND `month`=%s AND `year`=%s "
            request += "AND `start_time`=%s;"
            params = (str(note.get_date().get_day()),
                      str(note.get_date().get_month_number()),
                      str(note.get_date().get_year()),
                      str(note.get_start()))
            conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
            cursor = conn.cursor()
            cursor.execute(request, params)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            logger.log_exception(e)
            raise DatabaseException("Ошибка про удалении заметки из базы данных")

    @staticmethod
    def load_notes_by_day(date: MyDate) -> []:
        """данный метод загружает из базы данных заметки за один день"""
        try:
            request = "SELECT * FROM notes WHERE `day`=%s AND `month`=%s AND `year`=%s;"
            params = (str(date.get_day()),
                      str(date.get_month_number()),
                      str(date.get_year()))
            conn = mysql.connector.connect(host=host, database=database, user=user, password=password)
            cursor = conn.cursor()
            cursor.execute(request, params)
            array = []
            row = cursor.fetchone()

            while row is not None:
                n = Note()
                n.set_by_database_row(row)
                array.append(n)
                row = cursor.fetchone()
            cursor.close()
            conn.close()
            return array
        except Exception as e:
            logger.log_exception(e)
            raise DatabaseException("Ошибка про загрузке из базы данных")
