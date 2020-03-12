import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt_health import *

class MyMainForm(QMainWindow, Ui_Form):
	def __init__(self, parent=None):
		super(MyMainForm, self).__init__(parent)
		self.setupUi(self)
		self.name.setText("Yanyu Zhang")
		# self.time.setText("current")
		self.pulse.display("80")
		self.blood_pressure.display("120")
		self.lcdNumber_3.display("57")
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
	myWin = MyMainForm()
	myWin.show()
	sys.exit(app.exec_())



