import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt_health import *

class MyMainForm(QMainWindow, Ui_Form):
	def __init__(self, name, pulse, blood_pressure, lcdNumber_3, parent=None):
		super(MyMainForm, self).__init__(parent)
		self.setupUi(self)
		self.name.setText(name)
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
 
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWin = MyMainForm(name='Yanyu Zhang', pulse='80', blood_pressure='120', lcdNumber_3='57')
	myWin.show()
	sys.exit(app.exec_())



