import sys

import random

from PIL import Image, ImageFilter, ImageEnhance
from PyQt5 import QtGui, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.QtGui import QIcon


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('YL.ui', self)
        self.setWindowTitle("SYLP1D")
        self.setWindowIcon(QIcon('gcon.png'))

        Picture = QFileDialog.getOpenFileName(
            self, 'Выберете изображение (рек. 450х450):', '',
            'Картинка (*.jpg);;Все файлы(*);')[0]
        '''self.fname.move(300, 300)'''
        self.start_image = Picture  # исходник
        self.imge = 'imge.jpg'
        self.intermediate_img = 'intermediate.jpg' # промежуточный результат
        self.new_img = 'new.jpg'  # конечный результат
        self.main_image = "main.jpg"
        self.back_img = "back_image.jpg"
        if Picture:
            img = Image.open(self.start_image)
            img = img.resize((450, 450))
            img.save(self.new_img)
            img.save(self.intermediate_img)
            self.pixmap = QPixmap(self.new_img)
            self.Image.setPixmap(self.pixmap)

            imge = Image.open(self.start_image)
            imge = imge.resize((130, 130))
            imge.save(self.imge)
            self.pixmap = QPixmap(self.imge)
            self.Image_2.setPixmap(self.pixmap)

            self.last_x, self.last_y = None, None
            self.pen_color = QtGui.QColor('#111111')
        else:
            sys.exit(1)
        self.InitUI()

    def InitUI(self):
        self.open.clicked.connect(self.open_image)
        self.ac.clicked.connect(self.average_color)
        self.ng.clicked.connect(self.negativity)
        self.mp.clicked.connect(self.main_picture)
        self.save.clicked.connect(self.save_image_as)
        self.red.clicked.connect(self.r_color)
        self.green.clicked.connect(self.g_color)
        self.blue.clicked.connect(self.b_color)
        self.bw.clicked.connect(self.black_and_white)
        self.three_D.clicked.connect(self.Three_D)
        self.gauss_slider.valueChanged.connect(self.gaussian_blure)
        self.b_slider.valueChanged.connect(self.brightness)
        self.d_slider.valueChanged.connect(self.dullness)
        self.cnt_slider.valueChanged.connect(self.contrast)
        self.spn.clicked.connect(self.sharpness)
        self.rl.clicked.connect(self.rotate_l)
        self.rr.clicked.connect(self.rotate_r)
        self.cn.clicked.connect(self.contur)
        self.bb.clicked.connect(self.black_balance)
        self.wb.clicked.connect(self.white_balance)
        self.hm.clicked.connect(self.horizontal_mirror)
        self.vm.clicked.connect(self.vertical_mirror)
        self.ns.clicked.connect(self.noise)
        self.sp.clicked.connect(self.sepia)
        self.bc.clicked.connect(self.back)
        self.im_ugol = 0

    def mouseMoveEvent(self, e):
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        if self.last_x is None:
            self.last_x = e.x() - 220
            self.last_y = e.y() - 10
            return

        painter = QtGui.QPainter(self.Image.pixmap())
        painter.drawLine(self.last_x, self.last_y, e.x() - 220, e.y() - 10)
        painter.end()
        self.update()

        self.last_x = e.x() - 220
        self.last_y = e.y() - 10

        img = (self.Image.pixmap())

        img.save(self.new_img)
        img.save(self.intermediate_img)



    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def open_image(self):  # открытие изображения
        fname = QFileDialog.getOpenFileName(
            self, 'Выберете изображение (рек. 450х450):', '',
            'Картинка (*.jpg);;Картинка (*.jpg);;Все файлы (*)')[0]
        '''self.fname.move(300, 300)'''
        if fname:
            self.start_image = fname
            img = Image.open(self.start_image)
            img = img.resize((450, 450))
            img.save(self.new_img)
            img.save(self.intermediate_img)
            self.pixmap = QPixmap(self.new_img)
            self.Image.setPixmap(self.pixmap)

            imge = Image.open(self.start_image)
            imge = imge.resize((130, 130))
            imge.save(self.imge)
            self.pixmap = QPixmap(self.imge)
            self.Image_2.setPixmap(self.pixmap)
        else:
            self.start_image = self.start_image

    def save_image_as(self):  # сохранить изображение как
        fname = QFileDialog.getSaveFileName(
            self, '', self.save_name.text(),
            'Картинка (*.jpg);;Все файлы (*)')[0]
        '''self.fname.move(300, 300)'''
        if fname:
            img = Image.open(self.new_img)
            img.save(fname)
            self.Condition.setText('Изображение сохраненно.')
            self.Condition.setStyleSheet('QLabel {color: green;}')
        else:
            self.Condition.setText('Изображение не сохраненно.')
            self.Condition.setStyleSheet('QLabel {color: red;}')

    def r_color(self):  # данная функция оставляет только красный профиль цветов
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, 0, 0
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def g_color(self):  # данная функция оставляет только зеленый профиль цветов
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, 0
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def b_color(self):  # данная функция оставляет только синий профиль цветов
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, 0, b
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def average_color(self):  # средний цвет изображения
        img = Image.open(self.new_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        a, u, c = 0, 0, 0
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                a += r
                u += g
                c += b
        red = a // (x * y)
        green = u // (x * y)
        blue = c // (x * y)
        for i in range(x):
            for j in range(y):
                pixels[i, j] = red, green, blue
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def negativity(self):  # негатив
        img = Image.open(self.new_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 255 - r, 255 - g, 255 - b
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def main_picture(self):  # возвращение к исходнику
        img = Image.open(self.start_image)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        img = img.resize((450, 450))
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def back(self):
        img = Image.open(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        img = img.resize((450, 450))
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def black_and_white(self):  # черно-белое изобраение
        img = Image.open(self.new_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = (r + g + b) // 3, (r + g + b) // 3, (r + g + b) // 3
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def Three_D(self):  # стереопара
        img = Image.open(self.new_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x - 1, 5 - 1, -1):
            for j in range(y):
                r = pixels[i - 5, j][0]
                R, g, b = pixels[i, j]
                pixels[i, j] = r, g, b
        for i in range(5):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = 0, g, b
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def gaussian_blure(self):  # размытие по гаусу
        slider_value = int(self.gauss_slider.value())
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        img = img.filter(ImageFilter.GaussianBlur(radius=slider_value))
        img.save(self.new_img)
        self.gbpct.setText(str(slider_value))
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def sharpness(self):  # резкость
        img = Image.open(self.new_img)
        img.save(self.back_img)
        img = img.filter(ImageFilter.SHARPEN)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def contur(self):  # контур
        img = Image.open(self.new_img)
        img.save(self.back_img)
        img = img.filter(ImageFilter.CONTOUR)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def rotate_l(self):  # поворот налево
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        img = img.rotate(+90)
        self.im_ugol += 90
        self.im_ugol %= 360
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.intermediate_img)
        self.Image.setPixmap(self.pixmap)

    def rotate_r(self):  # поворот направо
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        img = img.rotate(-90)
        self.im_ugol -= 90
        self.im_ugol %= 360
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.intermediate_img)
        self.Image.setPixmap(self.pixmap)

    def black_balance(self):  # баланс черного
        img = Image.open(self.new_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if (r + g + b) <= 35:
                    pixels[i, j] = 0, 0, 0
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def white_balance(self):  # баланс белого
        img = Image.open(self.new_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if (r + g + b) >= 725:
                    pixels[i, j] = 255, 255, 255
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def vertical_mirror(self):  # отражение по вертикали
        img = Image.open(self.new_img)
        img.save(self.back_img)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def horizontal_mirror(self):  # отражение по горизонтали
        img = Image.open(self.new_img)
        img.save(self.back_img)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def brightness(self):  # яркость
        slider_value = int(self.b_slider.value())
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        imge = ImageEnhance.Brightness(img)
        imge = imge.enhance(((slider_value + 10) / 100) + 0.9)
        imge.save(self.new_img)
        self.bpct.setText(str((slider_value) / 100))
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def dullness(self):  # затемнение
        slider_value = int(self.d_slider.value())
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        imge = ImageEnhance.Brightness(img)
        imge = imge.enhance((-slider_value + 100) / 100)
        imge.save(self.new_img)
        self.dpct.setText(str((-slider_value) / 100))
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def contrast(self):
        slider_value = int(self.cnt_slider.value())
        img = Image.open(self.intermediate_img)
        img.save(self.back_img)
        img = ImageEnhance.Contrast(img)
        img = img.enhance((slider_value + 100) / 100)
        img.save(self.new_img)
        self.cntpct.setText(str((slider_value) / 100))
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def noise(self):  # шум
        img = Image.open(self.new_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                rand = random.randint(-15, 15)
                r, g, b = pixels[i, j]
                pixels[i, j] = r + rand, g + rand, b - rand
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)

    def sepia(self):  # сепия
        img = Image.open(self.new_img)
        img.save(self.back_img)
        pixels = img.load()
        x, y = img.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                S = (r + g + b) // 3
                pixels[i, j] = S + 10 * 2, S + 10, S
        img.save(self.new_img)
        img.save(self.intermediate_img)
        self.pixmap = QPixmap(self.new_img)
        self.Image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainScreen()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
