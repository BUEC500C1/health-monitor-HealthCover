import csv
import shutil
import sys
from sys import path
from threading import Lock
path.append('../Sensor')
from sensor import request_index, request_time_interval

data_path = '../Database/datas.csv'
training_set_path = '../Database/health.csv'
read_write_lock = Lock()
# write_ptr = 0

def write_title():
    fptr = open(data_path, 'w')
    filewriter = csv.writer(fptr, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Time', 'HeartRate', 'BloodPressureLow', 'BloodPressureHigh', 'BloodOxygen', 'awRR'])
    fptr.close()

def receive_data(stop_time=60*60*1):
    time_interval = request_time_interval()  # request the time interval from the sensor
    cnt = 0
    filewriter = csv.writer(open(data_path, 'a+'), delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while True and (cnt*time_interval <= stop_time):  # continously request data from the sensor and record it
        data = request_index()
        read_write_lock.acquire()  # acquire the lock before open the file and write
        filewriter.writerow([str(cnt), str(data['heart_rate']), str(data['blood_pressure_low'])
            , str(data['blood_pressure_high']), str(data['blood_oxygen']), str(data['awRR'])])
        read_write_lock.release()
        print("Time: " + str(time_interval*cnt) + "s.")
        print(" Pulse: " + str(data['heart_rate'])
            + " low blood pressure: " + str(data['blood_pressure_low'])
            + " high blood pressure: " + str(data['blood_pressure_high'])
            + " blood oxygen: " + str(data['blood_oxygen'])
            + " awRR: " + str(data['awRR']))
        print("...Data stored")
        cnt = cnt + 1

def request_data():

    read_write_lock.acquire()  # acquire lock before use the datas.csv file
    shutil.copy(data_path, training_set_path)
    read_write_lock.release()  # release lock after using
    return training_set_path  # return the file path to prediction module

if __name__ == '__main__':
    write_title()
    receive_data(2990)