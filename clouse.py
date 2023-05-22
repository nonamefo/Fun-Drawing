from tkinter import *


def closer(frame):
    root.destroy()
    frame.destroy()

def stoper():
    root.destroy()

def main(frame):
    global root
    root = Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (700 / 2)
    y = (screen_height / 2) - (300 / 2)

    root.geometry("500x200+%d+%d" % (x, y))
    root.resizable(False, False)

    qestion = Label(root, text="Вы хотите закрыть свой рисунок?", font=150)
    qestion.pack()

    stop_btn = Button(root, text="Cancel", bg="dim gray", command=lambda: stoper())
    stop_btn.place(relheight=0.2, relwidth=0.4, x=20, y=100)

    cnt_btn = Button(root, text="Ok", bg="dim gray", command=lambda: closer(frame))
    cnt_btn.place(relheight=0.2, relwidth=0.4, x=250, y=100)

    root.mainloop()


