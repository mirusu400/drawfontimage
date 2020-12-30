from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QApplication,
    QWidget
)
import sys
import core


class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.onClick)
        self.label = QLabel("", self)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.button)
        mainLayout.addWidget(self.label)
        self.setLayout(mainLayout)
        self.setWindowTitle("Example")

    def onClick(self):
        self.label.setText("Button clicked")


if __name__ == '__main__':
    cv = core.canvas(font="example/NanumGothic.ttf", mode="RGB", size=16)
    cv.create("귓규균", output="output3.png", mode="n")
    cv.posterize_palette()
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.exec_()
