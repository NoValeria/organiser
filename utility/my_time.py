from exceptions import MyException


class MyTime(object):
    """класс описывает время"""
    def __init__(self, m: int = None, h: int = None, s: str = None):
        if (m is not None or h is not None) and s is not None:
            raise MyException("Нельзя испольовать строковый параметр вместе с числовыми")
        if s is not None:
            # разделение строки на 2 числа по сепаратору ":",
            # если в конструктор передан параметр s (строка типа “23:01”)
            temp = s.split(':')
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
        """функция восстанавливает время из строки вида '15:41' """
        temp = s.split(":")
        if len(temp) != 2:
            raise MyException("Некорректное время!")
        self.__hour = int(temp[0])
        self.__minute = int(temp[1])

    def __to_minutes(self):
        """функция, переводящая время в число, используется для быстрого сравнения"""
        return self.__hour * 60 + self.__minute

    def hour(self):
        """функция возвращает час текущего времени"""
        return self.__hour

    def minute(self):
        """функция возвращает минуты текущего времени"""
        return self.__minute

    def __eq__(self, other):
        """Переопределяет оператор “=”."""
        if type(other) is MyTime:
            return self.__to_minutes() == other.__to_minutes()
        raise TypeError("Ошибка сравнения времени!")

    def __lt__(self, other):
        """Переопределяет оператор “ < “."""
        if type(other) is MyTime:
            return self.__to_minutes() < other.__to_minutes()
        raise TypeError("Ошибка сравнения времени!")

    def __le__(self, other):
        """Переопределяет оператор “<=”."""
        if type(other) is MyTime:
            return self.__to_minutes() <= other.__to_minutes()
        raise TypeError("Ошибка сравнения времени!")

    def __ne__(self, other):
        """Переопределяет оператор, обратный оператору  “=”."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Переопределяет оператор “ > ”."""
        return not self.__le__(other)

    def __ge__(self, other):
        """Переопределяет оператор “>=”."""
        return not self.__lt__(other)


    def __str__(self):
        """Возвращает дату в формате “часы:минуты”. """
        minute_str = str(self.__minute)
        if self.__minute < 10:
            minute_str = '0' + minute_str
        hour_str = str(self.__hour)
        if self.__hour < 10:
            hour_str = '0' + hour_str
        return hour_str + ':' + minute_str
