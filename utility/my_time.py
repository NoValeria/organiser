class MyTime(object):
    '''Позволяет нам описать входные данные в удобном для работы с ними формате.'''
    def __init__(self, m: int = None, h: int = None, s: str = None):
        if (m is not None or h is not None) and s is not None:
            raise Exception("Нельзя испольовать строковый параметр вместе с числовыми")
        if s is not None:
            temp = s.split(':')   # разделение строки на 2 числа по сепаратору ":", если в конструктор передан параметр s (строка типа “23:01”),
            self.__minute = int(temp[1])
            self.__hour = int(temp[0])
        else:
            if m is not None:
                self.__minute = m
            else:
                self.__minute = 0
            if h is not None:
                self.__hour = h
            else:
                self.__hour = 0

    def set_from_string(self, s: str):
        '''Oсуществляет проверку на корректность заданной строки.'''
        temp = s.split(":")
        if len(temp) != 2:
            raise Exception("Некорректное время!")
        self.__hour = int(temp[0])
        self.__minute = int(temp[1])

    def __to_minutes(self):
        '''Позволяет переводить заданное время в минуты.'''
        return self.__hour * 60 + self.__minute

    def hour(self):
        return self.__hour

    def minute(self):
        return self.__minute

    def __eq__(self, other):
        '''Переопределяет оператор “=”.'''
        if type(other) is MyTime:
            return self.__to_minutes() == other.__to_minutes()
        raise TypeError("Ошибка сравнения времени!")

    def __lt__(self, other):
        '''Переопределяет оператор “ < “.'''
        if type(other) is MyTime:
            return self.__to_minutes() < other.__to_minutes()
        raise TypeError("Ошибка сравнения времени!")

    def __le__(self, other):
        '''Переопределяет оператор “<=”.'''
        if type(other) is MyTime:
            return self.__to_minutes() <= other.__to_minutes()
        raise TypeError("Ошибка сравнения времени!")

    def __ne__(self, other):
        '''Переопределяет оператор, обратный оператору  “=”.'''
        return not self.__eq__(other)

    def __gt__(self, other):
        '''Переопределяет оператор “ > ”.'''
        return not self.__le__(other)

    def __ge__(self, other):
        '''Переопределяет оператор “>=”.'''
        return not self.__lt__(other)

    def __str__(self):
        '''Возвращает дату в формате “часы:минуты”. '''
        minute_str = str(self.__minute)
        if self.__minute < 10:
            minute_str = '0' + minute_str
        hour_str = str(self.__hour)
        if self.__hour < 10:
            hour_str = '0' + hour_str
        return hour_str + ':' + minute_str

