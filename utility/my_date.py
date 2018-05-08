import datetime  # Модуль datetime предоставляет классы для обработки времени и даты разными способами.

from PyQt5.QtWidgets import QCalendarWidget   # QCalendarWidget предоставляет виджет помесячного календаря.
                                              # Он позволяет пользователю выбирать дату простым и интуитивным путём.


class MyDate(object):
    '''Методы данного класса позволяют нам описать входные данные в удобном для работы с ними формате.'''
    def __init__(self, date: QCalendarWidget = None):
        '''
            С помощью метода __init__() присвоим значения None атрибутам класса по умолчанию.
            Если в конструктор передан параметр date, не являющийся None,
            то self.set_qt_date(date) устанавливает дату в зависимости от того,
            что было передано в параметре date,
            т.е. позволяет разделить поступающие данные формата QCalendar на составляющие.
        '''
        self.__day = None
        self.__month = None
        self.__year = None
        self.__info = None
        self.__day_of_week_name = None
        if date is not None:
            self.set_qt_date(date)

    def set_date(self, day: int, month: int, year: int):
        '''
            Метод set_date() принимает 3 аргумента (день, месяц, год)
            и записывает их в соответствующие поля данного класса.
        '''
        self.__day = day
        self.__month = month
        self.__year = year
        self.__info = datetime.date(year, month, day)
        self.__day_of_week_name = day_array[self.get_number_of_day()]

    def set_qt_date(self, date: QCalendarWidget):
        '''
            Позволяет привести данные к строке.
            Это осуществляется с помощью встроенной функции  date.toString().
        '''
        line = date.toString()
        params = line.split(' ')   # Создаём массив, элементами которого будут день недели (day_of_week_name), месяц (month), день (day), год (year)
        self.__day_of_week_name = params[0]
        self.__month = month_array.index(params[1]) + 1
        self.__day = int(params[2])
        self.__year = int(params[3])
        self.__info = datetime.date(self.__year, self.__month, self.__day)  # Получаем номер недели

    def __to_digit(self):
        '''Позволяет более быстро осуществить сравнение дат.'''
        return self.__year * 10000 + self.__month * 100 + self.__day

    def __eq__(self, other):
        '''Переопределяет оператор “=”.'''
        if type(other) is MyDate:
            return self.__to_digit() == other.__to_digit()
        raise TypeError("Ошибка сравнения дат!")

    def __lt__(self, other):
        '''Переопределяет оператор “ < “.'''
        if type(other) is MyDate:
            return self.__to_digit() < other.__to_digit()
        raise TypeError("Ошибка сравнения дат!")

    def __le__(self, other):
        '''Переопределяет оператор “<=”.'''
        if type(other) is MyDate:
            return self.__to_digit() <= other.__to_digit()
        raise TypeError("Ошибка сравнения дат!")

    def __ne__(self, other):
        '''Переопределяет оператор, обратный оператору  “=”.'''
        return not self.__eq__(other)

    def __gt__(self, other):
        '''Переопределяет оператор “ > ”.'''
        return not self.__lt__(other)

    def __ge__(self, other):
        '''Переопределяет оператор “>=”.'''
        return not self.__le__(other)

    def __str__(self):
        '''Возвращает дату в формате “день.месяц”. '''
        day_str = str(self.__day)
        if self.__day < 10:
            day_str = '0' + day_str
        month_str = str(self.__month)
        if self.__month < 10:
            month_str = '0' + month_str
        return day_str + '.' + month_str + '.' + str(self.__year)

    '''
        Методы get_number_of_week(), get_number_of_day(), get_day(),
        get_month_number(), get_year(), get_month_name(), get_name_of_day_in_week() 
        позволяют получить соответствующие значения для более удобной работы с датой
    '''

    def get_number_of_week(self):
        return self.__info.isocalendar()[1]

    def get_number_of_day(self):
        return self.__info.isoweekday() - 1

    def get_day(self):
        return self.__day

    def get_month_number(self):
        return self.__month

    def get_year(self):
        return self.__year

    def get_month_name(self):
        return month_array[self.__month - 1]

    def get_name_of_day_in_week(self):
        return day_array[self.get_number_of_day()]

month_array = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
day_array = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
