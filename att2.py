import tkinter.tix as tk


window = tk.Tk()
window.title("Органайзер")
screen_width = window.winfo_screenwidth() // 2
screen_height = window.winfo_screenheight() // 2
window.geometry("800x600+" + str(screen_width - 400) + "+" + str(screen_height - 300))
window.resizable(False, False)


#   Конфигурирование упаковщика. Методы принимают номер строки/столбца и аргументы конфигурации
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#  Создаем виджет.
# header=True значит, что мы хотим показывать заголовок.
tab = tk.HList(window, columns=3, header=True)
tab.grid(row=0, column=0, sticky="nswe")

# Просто скрол. В принципе, есть виджет ScrolledHList.
'''scroll = tk.Scrollbar(window, command=tab.yview)
tab['yscrollcommand'] = scroll.set
scroll.grid(row=0, column=1, sticky="nwse")'''

# Создаем заголовки.
tab.header_create(0, text="1")
tab.header_create(1, text="2")
tab.header_create(2, text="bottom")


# Добавим двадцать элементов
for i in range(20):
    # Добавляется строка.
    # Первый параметр - уникальное имя, он же идентификатор строки.
    # data - ассоциированные данные.
    index = '%s' % i
    tab.add(index, data="--<%s>--" % i)
    # Для каждой строки можно заполнить ячейки (столбцы).
    tab.item_create(index, 0, text=('Item1 ' + index))
    tab.item_create(index, 1, text=('Item2 ' + index))
    tab.item_create(index, 2, text=('Item3 ' + index))


    #  Функция демонстрирует методы конфигурирования ячеек
    # и получения данных.
    def funcgen(index):
        def func():
            print (tab.info_data(index))
            tab.item_configure(index, 1, text='Clicked')

        return func


    # Добавим кнопку в четвертый столбец.
    button = tk.Button(tab, text='test', command=funcgen(index))
    tab.item_create(index, 2, itemtype=tk.WINDOW, window=button)

def test_button_click(event):
    if window["bg"] == "green":
        window["bg"] = "white"
        print ('white')
    else:
        window["bg"] = "green"
        print ('green')

test_button = tk.Button(window, text="Test_back_color")
test_button.place(x=700, y=500)
test_button.bind("<Button-1>", test_button_click)

window.mainloop()
