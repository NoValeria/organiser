class MyException(Exception):
    """класс, описывающий ошибки в работе программы"""
    def __init__(self, message: str):
        self.message = message


class DatabaseException(MyException):
    """класс, описывающий ошибки при работе с базой данных"""
    def __init__(self, message: str):
        MyException.__init__(self, message)
