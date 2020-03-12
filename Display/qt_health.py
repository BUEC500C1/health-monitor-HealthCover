# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(800, 391)
        background = QPalette()
        background.setBrush(Form.backgroundRole(), QBrush(QPixmap('background.jpg')))   # 设置背景图片
        Form.setPalette(background)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 10, 211, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pulse = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.pulse.setStyleSheet("")
        self.pulse.setObjectName("pulse")
        self.verticalLayout.addWidget(self.pulse)
        self.blood_pressure = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.blood_pressure.setObjectName("blood_pressure")
        self.verticalLayout.addWidget(self.blood_pressure)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout.addWidget(self.lcdNumber_3)
        self.name = QtWidgets.QTextBrowser(Form)
        self.name.setGeometry(QtCore.QRect(130, 90, 180, 31))
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 90, 71, 31))
        self.label.setMinimumSize(QtCore.QSize(71, 0))
        self.label.setMaximumSize(QtCore.QSize(71, 16777215))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(590, 40, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(580, 150, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(590, 250, 21, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 71, 31))
        self.label_5.setObjectName("label_5")
        self.time = QtWidgets.QTextBrowser(Form)
        self.time.setGeometry(QtCore.QRect(130, 190, 180, 31))
        self.time.setObjectName("time")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowIcon(QIcon('icon.jpg'))
        Form.setWindowTitle(_translate("Form", "Health Monitor"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt;\">Name</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Name:</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">BPM</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">mmHg</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">%</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Time:</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

