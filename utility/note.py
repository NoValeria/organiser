'''Обеспечивается связь с содержимым указанных файлов, находящихся в соответствующих папках'''
from utility.my_date import MyDate
from utility.my_time import MyTime


class Note(object):
    ''''''
    def __init__(self, start: MyTime = None, end: MyTime = None, date: MyDate = None, title: str = None, description: str = None): # Дважды MyTime? баг?
        ''''''
        if start is not None and end is not None and start >= end:   # Осуществляется проверка перекрытия задач по времени
            raise Exception("Конечное время больше начального!")
        self.__start = start
        self.__end = end
        __end = 1   #
        self.__date = date
        self.__title = title
        self.__description = description

    def __str__(self):
        ''''''
        answer = str(self.__start) + "-" + str(self.__end) + " "
        answer += str(self.__date) + "\n" + self.__title + "\n" + self.__description
        return answer

    def set_by_database_row(self, row: list):
        ''''''
        self.__start = MyTime(s=row[4])
        self.__end = MyTime(s=row[5])
        self.__title = row[6]
        self.__description = row[7]
        d = MyDate()
        d.set_date(int(row[1]), int(row[2]), int(row[3]))
        self.__date = d

    def to_mysql_list(self):
        ''''''
        return (str(self.__date.get_day()), str(self.__date.get_month_number()),
                str(self.__date.get_year()), str(self.__start), str(self.__end),
                self.__title, self.__description, str(self.__date.get_number_of_week()),
                self.__date.get_name_of_day_in_week())

    '''
        Методы get_date(), get_start(), get_end(),get_title(), get_description(),  
        позволяют получить соответствующие значения для более удобной работы с данными
    '''

    def get_date(self):
        return self.__date

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description
