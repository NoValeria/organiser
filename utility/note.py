from exceptions import MyException
from utility.my_date import MyDate
from utility.my_time import MyTime


class Note(object):
    """класс описывает заметку(задание)"""
    def __init__(self, start: MyTime = None, end: MyTime = None, date: MyDate = None, title: str = None, description: str = None, important: int = None):
        if start is not None and end is not None and start >= end:
            raise MyException("Конечное время меньше или равно начальному!")
        if title == "" or description == "":
            raise MyException("Заполните все поля!")
        #  заполнение полей объекта
        self.__start = start
        self.__end = end
        self.__date = date
        self.__title = title
        self.__description = description
        self.__important = important

    def __str__(self):
        """строковое представление заметки"""
        answer = str(self.__start) + "-" + str(self.__end) + " "
        answer += str(self.__date) + "\n" + self.__title + "\n" + self.__description
        return answer

    def __eq__(self, other):
        if type(other) is Note:
            return other.__date == self.__date and other.__start == self.__start
        raise TypeError("Ошибка сравнения заметок!")

    def set_by_database_row(self, row: list):
        """функция устанавливает значения полей класса исходя из списка 
            элементов, полученного из базы данных"""
        self.__start = MyTime(s=row[4])
        self.__end = MyTime(s=row[5])
        self.__title = row[6]
        self.__description = row[7]
        self.__important = int(row[10])
        d = MyDate()
        d.set_date(int(row[1]), int(row[2]), int(row[3]))
        self.__date = d

    def to_mysql_list(self):
        """функция формирует список параметров для занесения заметки в БД"""
        return (str(self.__date.get_day()), str(self.__date.get_month_number()),
                str(self.__date.get_year()), str(self.__start), str(self.__end),
                self.__title, self.__description, str(self.__date.get_number_of_week()),
                self.__date.get_name_of_day_in_week(), str(self.__important))

    def get_date(self) -> MyDate:
        """функция возвращает дату текущей заметки"""
        return self.__date

    def get_start(self) -> MyTime:
        """функция возвращает время начала текущего задания(заметки)"""
        return self.__start

    def get_end(self) -> MyTime:
        """функция возвращает время окончания текущего задания(заметки)"""
        return self.__end

    def get_title(self) -> str:
        """функция возвращает заголовок заметки"""
        return self.__title

    def get_description(self) -> str:
        """функция возвращает описание заметки"""
        return self.__description

    def is_important(self) -> bool:
        """функция возвращает значение важности заметки"""
        return self.__important == 1
