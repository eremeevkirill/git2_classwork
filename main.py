import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint


class Prog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        self.setGeometry(800, 600, 800, 600)
        self.setFixedSize(800, 550)

        self.btn1 = QPushButton(self)
        self.btn1.setText('Нажми на меня')
        self.btn1.resize(125, 25)
        self.btn1.move(120, 10)
        self.btn1.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        N = randint(0, 255)
        P = randint(0, 255)
        C = randint(0, 255)
        qp.setBrush(QColor(N, P, C))
        S = randint(1, 490)
        qp.drawEllipse(300 - S / 2, 300 - S / 2, S, S)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Prog()
    calc.show()
    sys.exit(app.exec())