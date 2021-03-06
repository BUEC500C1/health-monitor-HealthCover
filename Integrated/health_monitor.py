import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt_health import *

class MyMainForm(QMainWindow, Ui_Form):
	def __init__(self, alert, pulse, blood_pressure, lcdNumber_3, parent=None):
		super(MyMainForm, self).__init__(parent)
		self.setupUi(self)
		self.name.setText(alert)
		# self.time.setText("current")
		self.pulse.display(pulse)
		self.blood_pressure.display(blood_pressure)
		self.lcdNumber_3.display(lcdNumber_3)
		timer = QTimer(self.time)
		timer.timeout.connect(self.showtime)
		timer.start()

	def showtime(self):
		datetime = QDateTime.currentDateTime()
		text = datetime.toString()
		self.time.setText(text)
		self.time.setFont(QFont("Roman times",12,QFont.Bold))


def monitor(alert,pulse,blood_pressure,lcdNumber_3):
	app = QApplication(sys.argv)
	myWin = MyMainForm(alert = alert, pulse = pulse, blood_pressure = blood_pressure, lcdNumber_3 = lcdNumber_3)
	myWin.show()
	sys.exit(app.exec_())

 
# if __name__ == "__main__":
# 	monitor('test','12','123','23')
	# app = QApplication(sys.argv)
	# myWin = MyMainForm(alert='None', pulse='80', blood_pressure='120', lcdNumber_3='57')
	# myWin.show()
	# sys.exit(app.exec_())



