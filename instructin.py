from tkinter import *


def clous():
    root.destroy()


def viget():
    global root
    root = Tk()
    root.title("Инструкция")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (700 / 2)
    y = (screen_height / 2) - (300 / 2)

    root.geometry("700x220+%d+%d" % (x, y))
    root.resizable(height=False, width=False)
    instruction = Label(text=
                        'Левая кнопка мыши - рисовать;\n'
                        'Правая кнопка мыши - ластик;\n'
                        'Все изображения сохраняются с расширением .ps и именем file_name.\n'
                        'в том же каталоге, что и это приложение\n'
                        'как только вы нажмете на кнопку сохранить, вы будете переведены в \n'
                        'сайт, где вы можете конвертировать в jpg\n'
                        'Наслаждайтесь рисованием :]'
                        , font=150)
    instruction.pack()
    clouse_btn = Button(root, text="OK", width=10, command=lambda: clous())
    wishes = Label(root, text="Приятного рисования от Всеволода. ;)")
    wishes.pack(side=BOTTOM)
    clouse_btn.pack()
    root.mainloop()


def main_viget():
    viget()
