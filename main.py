import random
import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor


class CircleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super(CircleDrawer, self).__init__()
        self.setWindowTitle("Git и случайные окружности")
        self.setGeometry(100, 100, 400, 300)
        self.drawButton = QtWidgets.QPushButton("Рисовать", self)
        self.drawButton.setGeometry(150, 220, 100, 50)
        self.drawButton.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter - 60)

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter, color) in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
