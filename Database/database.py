import csv
from threading import Lock
from Sensor.sensor import request_index, request_time_interval

data_path = './Database/datas.csv'
training_set_path = './Database/health.csv'
read_write_lock = Lock()
write_ptr = 0
fptr = open(data_path, 'w')
filewriter = csv.writer(fptr, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter.writerow(['Time', 'Pulse', 'BloodPressure', 'BloodOxygen'])
fptr.close()

def receive_data(stop_time=24*60*60):
    time_interval = request_time_interval()  # request the time interval from the sensor
    cnt = 0
    filewriter = csv.writer(open(data_path, 'a+'), delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while True and (cnt*time_interval <= stop_time):  # continously request data from the sensor and record it
        data = request_index()
        read_write_lock.acquire()  # acquire the lock before open the file and write
        filewriter.writerow([str(time_interval*cnt), str(data['heart_rate'])
            , str(data['blood_pressure_high']), str(data['blood_oxygen'])])
        read_write_lock.release()
        print(cnt)
        cnt = cnt + 1

def request_data():

    global write_ptr
    print(write_ptr)
    read_write_lock.acquire()  # acquire lock before use the datas.csv file
    rptr = open(data_path, 'rt')
    wptr = open(training_set_path, 'a+')
    reader = csv.reader(rptr)  # only copy new data
    writer = csv.writer(wptr)
    for idx, row in enumerate(reader):
        if idx >= write_ptr:
            writer.writerow(row)
            write_ptr = write_ptr + 1
    write_ptr = write_ptr + 1
    rptr.close()
    read_write_lock.release()  # release lock after using
    wptr.close()
    return training_set_path  # return the file path to prediction module

if __name__ == '__main__':

    receive_data(100)
    request_data()
    receive_data(100)
    request_data()
