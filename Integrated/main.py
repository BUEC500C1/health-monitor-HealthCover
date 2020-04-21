from alert import *
from sensor import sensor
from database import receive_data
from database import request_data
from predict import prediction
import health_monitor

if __name__ == '__main__':
	# simulate the monitor from time range 0 - 100
	start_time = 0
	stop_time = 100

	for i in range(start_time,stop_time,10):
		# create event
		event = Alert(i)
		# get parameters from sensor
		pulse = sensor(i)['heart_rate']
		blood_pressure = sensor(i)['blood_pressure_high']
		blood_oxygen = sensor(i)['blood_oxygen']
		# check if there is any alert triggered
		alert = event.check(timer(0,0,i))
		# default state is normal
		signal = "NORMAL"
		if len(event.alert) != 0:
			signal = event.alert[0]
		# pull GUI to display data and alert
		health_monitor.monitor(signal,pulse,blood_pressure,blood_oxygen)
		# make prediction based on data in database
		print("Prediction of future parameters :")
		print("time now is :", i)
		prediction(i)


