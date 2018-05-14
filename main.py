# В модуле sys содержатся функции и константы для взаимодействия с интерпретатором Python.
import sys
# Связываемся с классом MyWin в файле controllers
from controllers import MyWin, controllers

# Модуль QtWidgets содержит классы,
# которые обеспечивают набор UI-элементов для создания классических пользовательских интерфейсов.
# Виджет Qwidget является базовым классом для всех объектов интерфейса пользователя в PyQt5.   
from PyQt5 import QtWidgets   

# показываем окно органайзера
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin()
        myapp.show()
        sys.exit(app.exec_())
