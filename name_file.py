from tkinter import *
from webbrowser import *


def main():
    root = Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (700 / 2)
    y = (screen_height / 2) - (300 / 2)

    root.geometry("500x300+%d+%d" % (x, y))
    root.resizable(width=False, height=False)

    def show_message(link):
        root.destroy()
        open(link)

    text = Button(text='on which site do you want to convert your file',
                  bg="dim gray")

    text.place(relheight=0.1, relwidth=0.9, x=15, y=10)

    Any_btn = Button(text="Any Conv",
                     bg="dim gray",
                     command=lambda: show_message("https://anyconv.com/ru/konverter-ps-v-jpg"))

    Any_btn.place(relheight=0.1, relwidth=0.3, x=10, y=50)

    aspose_btn = Button(text="Aspose",
                        bg="dim gray",
                        command=lambda: show_message("https://products.aspose.app/page/ru/conversion/ps-to-jpg"))

    aspose_btn.place(relheight=0.1, relwidth=0.3, x=180, y=50)

    convetio_btn = Button(text="Convertio",
                          bg="dim gray",
                          command=lambda: show_message(""))

    convetio_btn.place(relheight=0.1, relwidth=0.3, x=340, y=50)

    instruction = Label(text=
                        'Я напоминаю вам, что ваш файл в настоящее время \no'
                        'называется: имя_файла и имеет расширение ps\n'
                        'Я настоятельно рекомендую это после преобразования \n'
                        'переименуйте его в противном случае\n'
                        'может произойти автозамена.',
                        font=50)

    instruction.place(x=10, y=100)

    root.mainloop()
