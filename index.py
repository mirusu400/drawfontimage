from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QApplication,
)
import sys
import core
def printa(a,b=10,c=10):
    print(a+b+c)

class Dialog(QDialog):
    def onClick(self):
        self.label.setText("Button clicked")

    def __init__(self):
        super(Dialog, self).__init__()
        self.button = QPushButton("Click me")
        self.button.clicked.connect(self.onClick)
        self.label = QLabel("", self)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.button)
        mainLayout.addWidget(self.label)
        self.setLayout(mainLayout)
        self.setWindowTitle("Example")


if __name__ == '__main__':
    cv = core.canvas(font="gulim.ttf")
    cv.createImg("안녕하세요",15,15)
    app = QApplication(sys.argv)
    dialog = Dialog()
dialog.exec_()
