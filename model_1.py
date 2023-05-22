from tkinter import *
import clouse
import name_file


# класс Paint
class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        # Параметры кисти по умолчанию
        self.brush_size = 10
        self.color = "red"
        self.color_rght_btn = "white"
        self.br = 1
        # Устанавливаем компоненты UI
        self.setUI()

    # Метод рисования на холсте

    # Метод рисования на холсте
    def gl_draw(self, event):
        if self.br == 0:
            # кисть
            if self.brush_size < 201:
                self.canvas_1.create_rectangle(event.x - self.brush_size,
                                               event.y - 2,
                                               event.x + self.brush_size,
                                               event.y + 2,
                                               fill=self.color, outline=self.color)
            else:
                self.canvas_1.create_rectangle(event.x - 200,
                                               event.y - 2,
                                               event.x + 200,
                                               event.y + 2,
                                               fill=self.color, outline=self.color)
        # ручка
        elif self.br == 1:
            self.canvas_1.create_oval(event.x - self.brush_size,
                                      event.y - self.brush_size,
                                      event.x + self.brush_size,
                                      event.y + self.brush_size,
                                      fill=self.color, outline=self.color)
        elif self.br == 2:
            self.canvas_1.create_oval(event.x - self.brush_size,
                                      event.y - self.brush_size,
                                      event.x + self.brush_size,
                                      event.y + self.brush_size,
                                      outline=self.color, width=2)

        elif self.br == 3:
            self.canvas_1.create_oval(event.x - self.brush_size,
                                      event.y - self.brush_size,
                                      event.x + self.brush_size,
                                      event.y + self.brush_size,
                                      outline=self.color, width=2)
            self.canvas_1.create_line(event.x,
                                      event.y - self.brush_size - self.brush_size / 25,
                                      event.x,
                                      event.y + self.brush_size + self.brush_size / 25,
                                      dash=(10, 5))
            self.canvas_1.create_line(event.x - self.brush_size - self.brush_size / 25,
                                      event.y,
                                      event.x + self.brush_size + self.brush_size / 25,
                                      event.y,
                                      dash=(10, 5))
        elif self.br == 4:
            self.canvas_1.create_rectangle(event.x - self.brush_size,
                                           event.y - self.brush_size,
                                           event.x + self.brush_size,
                                           event.y + self.brush_size,
                                           outline=self.color)
            self.canvas_1.create_rectangle(event.x - self.brush_size - self.brush_size / 2,
                                           event.y - self.brush_size + self.brush_size / 2,
                                           event.x + self.brush_size - self.brush_size / 2,
                                           event.y + self.brush_size + self.brush_size / 2,
                                           outline=self.color)
            self.canvas_1.create_line(event.x - self.brush_size - self.brush_size / 2,
                                      event.y - self.brush_size + self.brush_size / 2,
                                      event.x - self.brush_size,
                                      event.y - self.brush_size,
                                      fill=self.color)
            self.canvas_1.create_line(event.x + self.brush_size - self.brush_size / 2,
                                      event.y + self.brush_size + self.brush_size / 2,
                                      event.x + self.brush_size,
                                      event.y + self.brush_size,
                                      fill=self.color)
            self.canvas_1.create_line(event.x - self.brush_size - self.brush_size / 2,
                                      event.y + self.brush_size + self.brush_size / 2,
                                      event.x - self.brush_size,
                                      event.y + self.brush_size,
                                      fill=self.color)
            self.canvas_1.create_line(event.x + self.brush_size - self.brush_size / 2,
                                      event.y - self.brush_size + self.brush_size / 2,
                                      event.x + self.brush_size,
                                      event.y - self.brush_size,
                                      fill=self.color)
        elif self.br == 5:
            self.canvas_1.create_line(event.x,
                                      event.y - self.brush_size,
                                      event.x,
                                      event.y + self.brush_size,
                                      fill=self.color)
            self.canvas_1.create_line(event.x - self.brush_size,
                                      event.y,
                                      event.x + self.brush_size,
                                      event.y,
                                      fill=self.color)

    def draw_ruber(self, event):
        self.canvas_1.create_oval(event.x - self.brush_size,
                                  event.y - self.brush_size,
                                  event.x + self.brush_size,
                                  event.y + self.brush_size,
                                  fill=self.color_rght_btn, outline=self.color_rght_btn)

    def set_bg(self):
        self.color_rght_btn = self.color

    def set_pen(self, new_pen):
        self.br = new_pen

    # Изменение цвета кисти

    def set_color(self, new_color):
        self.color = new_color
        if self.brush_size == 9999:
            self.set_bg()

    # Изменение размера кисти

    def set_brush_size(self, new_size):
        self.brush_size = new_size
        if new_size == 9999:
            self.set_bg()

    def saver(self, cv):
        cv.update()
        cv.postscript(file="file_name.ps", colormode='color')
        clouse.main(root)

        name_file.main()

    def delite(self):
        self.canvas_1.delete("all")
        self.color_rght_btn = "white"

    def setUI(self):

        # Размещаем активные элементы на родительском окне
        self.pack(fill=BOTH, expand=1)

        # Создаем холст с серым фоном
        self.cnv = Canvas(self, bg='dim gray', height=660, width=1270)

        # Создаем холст с белым фоном
        self.canvas_1 = Canvas(self, bg='white', height=660, width=1075)

        self.cnv.place(x=0, y=0)
        self.canvas_1.place(x=64, y=0)
        # задаем реакцию холста на нажатие левой кнопки мыши
        self.canvas_1.bind("<Button-1>", self.gl_draw)
        self.canvas_1.bind("<B1-Motion>", self.gl_draw)
        # задаем реакцию холста на нажатие правой кнопки мыши
        self.canvas_1.bind("<Button-3>", self.draw_ruber)
        self.canvas_1.bind("<B3-Motion>", self.draw_ruber)

        # создаем кнопки

        # первый столбец

        # Создаем метку для кнопок изменения размера кисти

        clear_btn = Button(self, text="стереть все", command=lambda: self.delite())
        clear_btn.place(relheight=0.03, relwidth=0.05, x=0, y=0)

        one_btn = Button(self, text="1x", command=lambda: self.set_brush_size(1))
        one_btn.place(relheight=0.03, relwidth=0.05, x=0, y=20)

        two_btn = Button(self, text="2x", command=lambda: self.set_brush_size(2))
        two_btn.place(relheight=0.03, relwidth=0.05, x=0, y=40)

        five_btn = Button(self, text="5x", command=lambda: self.set_brush_size(5))
        five_btn.place(relheight=0.03, relwidth=0.05, x=0, y=60)

        seven_btn = Button(self, text="7x", command=lambda: self.set_brush_size(7))
        seven_btn.place(relheight=0.03, relwidth=0.05, x=0, y=80)

        ten_btn = Button(self, text="10x", command=lambda: self.set_brush_size(10))
        ten_btn.place(relheight=0.03, relwidth=0.05, x=0, y=100)

        twenty_btn = Button(self, text="20x", command=lambda: self.set_brush_size(20))
        twenty_btn.place(relheight=0.03, relwidth=0.05, x=0, y=120)

        fifty_btn = Button(self, text="50x", command=lambda: self.set_brush_size(50))
        fifty_btn.place(relheight=0.03, relwidth=0.05, x=0, y=140)

        seventy_btn = Button(self, text="70x", command=lambda: self.set_brush_size(70))
        seventy_btn.place(relheight=0.03, relwidth=0.05, x=0, y=160)

        onehondred_btn = Button(self, text="100x", command=lambda: self.set_brush_size(100))
        onehondred_btn.place(relheight=0.03, relwidth=0.05, x=0, y=180)

        onehundred_twenty_btn = Button(self, text="120x", command=lambda: self.set_brush_size(120))
        onehundred_twenty_btn.place(relheight=0.03, relwidth=0.05, x=0, y=200)

        onehundred_fifty_btn = Button(self, text="150x", command=lambda: self.set_brush_size(150))
        onehundred_fifty_btn.place(relheight=0.03, relwidth=0.05, x=0, y=220)

        onehundred_seventy_btn = Button(self, text="170x", command=lambda: self.set_brush_size(170))
        onehundred_seventy_btn.place(relheight=0.03, relwidth=0.05, x=0, y=240)

        twohundred_btn = Button(self, text="200x", command=lambda: self.set_brush_size(200))
        twohundred_btn.place(relheight=0.03, relwidth=0.05, x=0, y=260)

        twohundred_twenty_btn = Button(self, text="220x", command=lambda: self.set_brush_size(220))
        twohundred_twenty_btn.place(relheight=0.03, relwidth=0.05, x=0, y=280)

        twohundred_forty_btn = Button(self, text="240x", command=lambda: self.set_brush_size(240))
        twohundred_forty_btn.place(relheight=0.03, relwidth=0.05, x=0, y=300)

        twohundred_sex_btn = Button(self, text="260x", command=lambda: self.set_brush_size(260))
        twohundred_sex_btn.place(relheight=0.03, relwidth=0.05, x=0, y=320)

        twohundred_eught_btn = Button(self, text="280x", command=lambda: self.set_brush_size(280))
        twohundred_eught_btn.place(relheight=0.03, relwidth=0.05, x=0, y=340)

        trehundred_btn = Button(self, text="300x", command=lambda: self.set_brush_size(300))
        trehundred_btn.place(relheight=0.03, relwidth=0.05, x=0, y=360)

        bg_color_btn = Button(self, text="фон", command=lambda: self.set_brush_size(9999))
        bg_color_btn.place(relheight=0.03, relwidth=0.05, x=0, y=380)

        pen_btn = Button(self, text="ручка", command=lambda: self.set_pen(1))
        pen_btn.place(relheight=0.03, relwidth=0.05, x=0, y=400)

        brush_btn = Button(self, text="кисть", command=lambda: self.set_pen(0))
        brush_btn.place(relheight=0.03, relwidth=0.05, x=0, y=420)

        len_btn = Button(self, text="пустой\nкруг", command=lambda: self.set_pen(2))
        len_btn.place(relheight=0.06, relwidth=0.05, x=0, y=440)

        cerqul_geom_btn = Button(self, text="геометрический\nкруг", command=lambda: self.set_pen(3))
        cerqul_geom_btn.place(relheight=0.07, relwidth=0.05, x=0, y=480)

        scer_btn = Button(self, text="куб", command=lambda: self.set_pen(4))
        scer_btn.place(relheight=0.04, relwidth=0.05, x=0, y=526)

        scer_btn = Button(self, text="ось х y", command=lambda: self.set_pen(5))
        scer_btn.place(relheight=0.04, relwidth=0.05, x=0, y=552)

        save_btn = Button(self, text="сохранить", command=lambda: self.saver(self.canvas_1))
        save_btn.place(relheight=0.05, relwidth=0.05, x=0, y=578)

        # второй столбец

        red_btn = Button(self, bg="snow", command=lambda: self.set_color("snow"))
        red_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=0)

        green_btn = Button(self, bg="AntiqueWhite", command=lambda: self.set_color("AntiqueWhite"))
        green_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=20)

        blue_btn = Button(self, bg="AntiqueWhite1", command=lambda: self.set_color("AntiqueWhite1"))
        blue_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=40)

        blue_btn = Button(self, bg="AntiqueWhite2", command=lambda: self.set_color("AntiqueWhite2"))
        blue_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=60)

        white_btn = Button(self, bg="AntiqueWhite3", command=lambda: self.set_color("AntiqueWhite3"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=80)

        white_btn = Button(self, bg="AntiqueWhite4", command=lambda: self.set_color("AntiqueWhite4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=100)

        white_btn = Button(self, bg="gray25", command=lambda: self.set_color("gray25"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=120)

        white_btn = Button(self, bg="gray23", command=lambda: self.set_color("gray23"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=140)

        white_btn = Button(self, bg="gray19", command=lambda: self.set_color("gray19"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=160)

        white_btn = Button(self, bg="gray13", command=lambda: self.set_color("gray13"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=180)

        white_btn = Button(self, bg="gray9", command=lambda: self.set_color("gray9"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=200)

        white_btn = Button(self, bg="gray5", command=lambda: self.set_color("gray5"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=220)

        white_btn = Button(self, bg="blue4", command=lambda: self.set_color("blue4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=240)

        white_btn = Button(self, bg="blue3", command=lambda: self.set_color("blue3"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=260)

        white_btn = Button(self, bg="blue2", command=lambda: self.set_color("blue2"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=280)

        white_btn = Button(self, bg="blue1", command=lambda: self.set_color("blue1"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=300)

        white_btn = Button(self, bg="blue", command=lambda: self.set_color("blue"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=320)

        white_btn = Button(self, bg="cyan4", command=lambda: self.set_color("cyan4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=340)

        white_btn = Button(self, bg="cyan3", command=lambda: self.set_color("cyan3"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=360)

        white_btn = Button(self, bg="cyan2", command=lambda: self.set_color("cyan2"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=380)

        white_btn = Button(self, bg="cyan", command=lambda: self.set_color("cyan"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=400)

        white_btn = Button(self, bg="gold", command=lambda: self.set_color("gold"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=420)

        white_btn = Button(self, bg="goldenrod1", command=lambda: self.set_color("goldenrod1"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=440)

        white_btn = Button(self, bg="goldenrod2", command=lambda: self.set_color("goldenrod2"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=460)

        white_btn = Button(self, bg="goldenrod3", command=lambda: self.set_color("goldenrod3"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=480)

        white_btn = Button(self, bg="goldenrod4", command=lambda: self.set_color("goldenrod4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=500)

        white_btn = Button(self, bg="DarkOrange4", command=lambda: self.set_color("DarkOrange4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=520)

        white_btn = Button(self, bg="DarkRed", command=lambda: self.set_color("DarkRed"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=540)

        white_btn = Button(self, bg="DeepPink4", command=lambda: self.set_color("DeepPink4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=560)

        white_btn = Button(self, bg="DeepPink3", command=lambda: self.set_color("DeepPink3"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=580)

        white_btn = Button(self, bg="DeepPink2", command=lambda: self.set_color("DeepPink2"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=600)

        white_btn = Button(self, bg="DeepPink1", command=lambda: self.set_color("DeepPink1"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=620)

        white_btn = Button(self, bg="DeepSkyBlue", command=lambda: self.set_color("DeepSkyBlue"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1143, y=640)

        # третий столбик

        white_btn = Button(self, bg="red", command=lambda: self.set_color("red"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=0)

        white_btn = Button(self, bg="chartreuse4", command=lambda: self.set_color("chartreuse4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=20)

        white_btn = Button(self, bg="chartreuse3", command=lambda: self.set_color("chartreuse3"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=40)

        white_btn = Button(self, bg="chartreuse2", command=lambda: self.set_color("chartreuse2"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=60)

        white_btn = Button(self, bg="chartreuse1", command=lambda: self.set_color("chartreuse1"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=80)

        white_btn = Button(self, bg="DarkTurquoise", command=lambda: self.set_color("DarkTurquoise"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=100)

        white_btn = Button(self, bg="DarkSlateGray1", command=lambda: self.set_color("DarkSlateGray1"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=120)

        white_btn = Button(self, bg="DarkSlateGray2", command=lambda: self.set_color("DarkSlateGray2"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=140)

        white_btn = Button(self, bg="DarkSlateGray3", command=lambda: self.set_color("DarkSlateGray3"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=160)

        white_btn = Button(self, bg="DarkSlateGray4", command=lambda: self.set_color("DarkSlateGray4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=180)

        white_btn = Button(self, bg="DarkSlateGrey", command=lambda: self.set_color("DarkSlateGrey"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=200)

        white_btn = Button(self, bg="dark slate blue", command=lambda: self.set_color("dark slate blue"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=220)

        white_btn = Button(self, bg="dark slate blue", command=lambda: self.set_color("dark slate blue"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=240)

        white_btn = Button(self, bg="slate blue", command=lambda: self.set_color("slate blue"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=260)

        white_btn = Button(self, bg="medium slate blue", command=lambda: self.set_color("medium slate blue"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=280)

        white_btn = Button(self, bg="light slate blue", command=lambda: self.set_color("light slate blue"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=300)

        white_btn = Button(self, bg="medium orchid", command=lambda: self.set_color("medium orchid"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=320)

        white_btn = Button(self, bg="dark orchid", command=lambda: self.set_color("dark orchid"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=340)

        white_btn = Button(self, bg="dark violet", command=lambda: self.set_color("dark violet"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=360)

        white_btn = Button(self, bg="blue violet", command=lambda: self.set_color("blue violet"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=380)

        white_btn = Button(self, bg="purple", command=lambda: self.set_color("purple"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=400)

        white_btn = Button(self, bg="medium purple", command=lambda: self.set_color("medium purple"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=420)

        white_btn = Button(self, bg="dark olive green", command=lambda: self.set_color("dark olive green"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=440)

        white_btn = Button(self, bg="olive drab", command=lambda: self.set_color("olive drab"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=460)

        white_btn = Button(self, bg="dark green", command=lambda: self.set_color("dark green"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=480)

        white_btn = Button(self, bg="forest green", command=lambda: self.set_color("forest green"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=500)

        white_btn = Button(self, bg="yellow green", command=lambda: self.set_color("yellow green"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=520)

        white_btn = Button(self, bg="lime green", command=lambda: self.set_color("lime green"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=540)

        white_btn = Button(self, bg="spring green", command=lambda: self.set_color("spring green"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=560)

        white_btn = Button(self, bg="medium spring green", command=lambda: self.set_color("medium spring green"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=580)

        white_btn = Button(self, bg="lawn green", command=lambda: self.set_color("lawn green"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=600)

        white_btn = Button(self, bg="dark khaki", command=lambda: self.set_color("dark khaki"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=620)

        white_btn = Button(self, bg="coral4", command=lambda: self.set_color("coral4"))
        white_btn.place(relheight=0.03, relwidth=0.05, x=1207, y=640)


# функция для создания главного окна
def main():
    global root
    root = Tk()
    root.title("Fun Drawing")
    root.geometry('1270x640+0+0')
    root.resizable(height=False, width=False)
    Paint(root)
    root.mainloop()
