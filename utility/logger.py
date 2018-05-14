def log_exception(ex: Exception):
    """функция дозаписывает сообщение об ошибке в файл"""
    file = open("exception_log.txt", "a", encoding="utf-8")
    file.write(str(ex) + "\r\n")
    file.close()
