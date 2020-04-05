

# This Python file uses the following encoding: utf-8
import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mainwindow import Ui_MainWindow


COLD_STYLE = """
QProgressBar::chunk{
    background-color: #63a1f2;
    width: 22px;
}
"""

NORMAL_STYLE = """
QProgressBar::chunk{
    background-color: #63f280;
    width: 22px;
}
"""

HOT_STYLE = """
QProgressBar::chunk{
    background-color: #f04f57;
    width: 22px;
}
"""


class Main_Win(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.setupUi(self)
        self.show()

        # self.pbOutside.setStyle(QStyleFactory.create('Fusion'))
        # self.pbInside.setStyle(QStyleFactory.create('Fusion'))
        # self.pbGarage.setStyle(QStyleFactory.create('Fusion'))
        # self.pbStorage.setStyle(QStyleFactory.create('Fusion'))
        self.btnGarage.setCheckable(True)
        self.btnGarage.toggled.connect(self.btnGarage_changed)
        self.btnStorage.setCheckable(True)
        self.btnStorage.toggled.connect(self.btnStorage_changed)
        self.btnAir.setCheckable(True)
        self.btnAir.toggled.connect(self.btnAir_changed)

    def btnGarage_changed(self):

        if self.btnGarage.isChecked():
            self.btnGarage.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                         "margin: 1px;\n"
                                         "border-color: #343536;\n"
                                         "border-style: outset;\n"
                                         "border-radius: 3px;\n"
                                         "border-width: 1px;"
                                         )
        else:
            self.btnGarage.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                         "margin: 1px;\n"
                                         "border-color: #343536;\n"
                                         "border-style: outset;\n"
                                         "border-radius: 3px;\n"
                                         "border-width: 1px;"
                                         )
        self.pbGarage.setValue(random.randrange(-15, 110))
        if self.pbGarage.value() <= 34:
            self.pbGarage.setStyleSheet(COLD_STYLE)
        elif self.pbGarage.value() <= 90:
            self.pbGarage.setStyleSheet(NORMAL_STYLE)
        else:
            self.pbGarage.setStyleSheet(HOT_STYLE)

    def btnStorage_changed(self):
        if self.btnStorage.isChecked():
            self.btnStorage.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                          "margin: 1px;\n"
                                          "border-color: rgb(255, 255, 255);\n"
                                          "border-style: outset;\n"
                                          "border-radius: 3px;\n"
                                          "border-width: 1px;"
                                          )
        else:
            self.btnStorage.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                          "margin: 1px;\n"
                                          "border-color: rgb(255, 255, 255);\n"
                                          "border-style: outset;\n"
                                          "border-radius: 3px;\n"
                                          "border-width: 1px;"
                                          )
        self.pbStorage.setValue(random.randrange(-15, 110))
        if self.pbStorage.value() <= 34:
            self.pbStorage.setStyleSheet(COLD_STYLE)
        elif self.pbStorage.value() <= 90:
            self.pbStorage.setStyleSheet(NORMAL_STYLE)
        else:
            self.pbStorage.setStyleSheet(HOT_STYLE)

    def btnAir_changed(self):
        if self.btnAir.isChecked():
            self.btnAir.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                      "margin: 1px;\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "border-style: outset;\n"
                                      "border-radius: 3px;\n"
                                      "border-width: 1px;"
                                      )
        else:
            self.btnAir.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                      "margin: 1px;\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "border-style: outset;\n"
                                      "border-radius: 3px;\n"
                                      "border-width: 1px;"
                                      )

        newVal = random.randrange(-15, 110)
        self.pbOutside.setValue(newVal)
        # self.pbOutside.setStyle(QStyleFactory.create('Fusion'))
        if newVal <= 34:
            self.pbOutside.setStyleSheet(COLD_STYLE)
        elif newVal <= 90:
            self.pbOutside.setStyleSheet(NORMAL_STYLE)
        else:
            self.pbOutside.setStyleSheet(HOT_STYLE)


def main():
    app = QApplication(sys.argv)
    window = Main_Win()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
