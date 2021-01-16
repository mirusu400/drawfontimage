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
import sys
import core


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initMenu(self):
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

    def initUI(self):
        self.resize(800, 600)
        self.initMenu()
        btn = QPushButton('button01', self)
        btn.move(100,100)
        self.setWindowTitle("FontEditor")
        self.show()

    def onClick(self):
        self.label.setText("Button clicked")


class Widgets(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)

if __name__ == '__main__':
    cv = core.canvas(font="example/NanumGothic.ttf", mode="RGB", size=16)
    cv.create("귓규균", output="output3.png", mode="n")
    cv.posterize_palette()
    # app = QApplication(sys.argv)
    # widget = Widgets()
    # window = MainWindow()
    # sys.exit(app.exec_())
