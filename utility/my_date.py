# Модуль datetime предоставляет классы для обработки времени и даты разными способами.
import datetime
# QCalendarWidget предоставляет виджет помесячного календаря.
# Он позволяет пользователю выбирать дату простым и интуитивным путём.
from PyQt5.QtWidgets import QCalendarWidget


class MyDate(object):
    """класс описывает дату, с которой удобно работать"""

    # статические массивы с названиями месяцев и дней недели
    month_array = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    day_array = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

    def __init__(self, date: QCalendarWidget = None):
        """
            С помощью метода __init__() присвоим значения None атрибутам класса по умолчанию.
            Если в конструктор передан параметр date, не являющийся None,
            то self.set_qt_date(date) устанавливает дату в зависимости от того,
            что было передано в параметре date,
            т.е. позволяет разделить поступающие данные формата QCalendar на составляющие.
        """
        self.__day = None
        self.__month = None
        self.__year = None
        self.__info = None
        self.__day_of_week_name = None
        if date is not None:
            self.set_qt_date(date)

    def set_date(self, day: int, month: int, year: int):
        """функция устанавливает значения полей объекта в зависимости 
            от переданных параметров: дня, месяца и года"""
        self.__day = day
        self.__month = month
        self.__year = year
        self.__info = datetime.date(year, month, day)
        self.__day_of_week_name = MyDate.day_array[self.get_number_of_day()]

    def set_qt_date(self, date: QCalendarWidget):
        """функция устанавливает поля класса исходя из переданной даты,
            дата имеет тип QCalendarWidget"""
        params = date.toString().split(' ')
        self.__day_of_week_name = params[0]
        self.__month = MyDate.month_array.index(params[1]) + 1
        self.__day = int(params[2])
        self.__year = int(params[3])
        self.__info = datetime.date(self.__year, self.__month, self.__day)

    def __to_digit(self):
        """приватная функция, помогающая сравнивать даты"""
        return self.__year * 1000 + self.__month * 100 + self.__day

    def __eq__(self, other):
        """Переопределяет оператор “=”."""
        if type(other) is MyDate:
            return self.__to_digit() == other.__to_digit()
        raise TypeError("Ошибка сравнения дат!")

    def __lt__(self, other):
        """Переопределяет оператор “ < “."""
        if type(other) is MyDate:
            return self.__to_digit() < other.__to_digit()
        raise TypeError("Ошибка сравнения дат!")

    def __le__(self, other):
        """Переопределяет оператор “<=”."""
        if type(other) is MyDate:
            return self.__to_digit() <= other.__to_digit()
        raise TypeError("Ошибка сравнения дат!")

    def __ne__(self, other):
        """Переопределяет оператор, обратный оператору  “=”."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Переопределяет оператор “>”."""
        return not self.__le__(other)

    def __ge__(self, other):
        """Переопределяет оператор “>=”."""
        return not self.__lt__(other)

    def __str__(self):
        """Строковое представление даты в формате ДД.ММ.ГГГГ"""
        day_str = str(self.__day)
        if self.__day < 10:
            day_str = '0' + day_str
        month_str = str(self.__month)
        if self.__month < 10:
            month_str = '0' + month_str
        return day_str + '.' + month_str + '.' + str(self.__year)

    def get_next_day(self):
        """функция, возвращающая объект типа MyDate, который является 
            представлением дня, следующего за тем, который лежит в текущем объекте"""
        d = self.__day + 1
        m = self.__month
        y = self.__year
        if self.__day == MyDate.month_array[self.__month - 1]:
            d = 1
            m += 1
        if m == 13:
            m = 1
            y += 1
        temp = MyDate()
        temp.set_date(d, m, y)
        return temp

    def get_number_of_week(self):
        """функция возвращает номер недели для текущей даты"""
        return self.__info.isocalendar()[1]

    def get_number_of_day(self):
        """функция возвращает номер (0-6) дня недели для текущей даты"""
        return self.__info.isoweekday() - 1

    def get_day(self):
        """функция возвращает число текущей даты"""
        return self.__day

    def get_month_number(self):
        """функция возвращает номер месяца текущей даты"""
        return self.__month

    def get_year(self):
        """функция возвращает год текущей даты"""
        return self.__year

    def get_month_name(self):
        """функция возвращает название месяца для текущей даты"""
        return MyDate.month_array[self.__month - 1]

    def get_name_of_day_in_week(self):
        """функция возвращает название дня недели для текущей даты"""
        return MyDate.day_array[self.get_number_of_day()]
