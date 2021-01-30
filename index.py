from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
    QApplication,
    QAction,
    QWidget,
    qApp
)
from PyQt5.QtGui import (
    QIcon
)
from PyQt5 import uic
import sys
import core


form_class = uic.loadUiType("./form/form.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    cv = core.canvas(font="example/NanumGothic.ttf", bgcolor=(250,250,250,255), fcolor=(32,16,13,255), size=32)
    cv.create("안녕하슈")
    cv.save("output2.png")
    cv.change_palette("./example/TLP.pal")
    cv.save("output3.png")
    # cv.posterize_palette()
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
