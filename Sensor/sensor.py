import random
import time

HOUR = 0
MIN = 0
SEC = 10

def tn(h,m,s):
    return h*3600+m*60+s

def sensor(n):
    data = {}
    #mmHg
    data['blood_pressure_low'] = round(random.uniform(60,80),n)
    data['blood_pressure_high'] = round(random.uniform(100,130),n)
    #%
    data['blood_oxygen'] = round(random.uniform(95,100),n)
    data['heart_rate'] = round(random.randint(60,100),n)
    data['awRR'] = random.randint(12,20)
    return data

def timer(h,m,s):
    t = tn(h,m,s)
    while True:
        time.sleep(t)
        return sensor(2)

def request_index():
    t = tn(HOUR, MIN, SEC)
    time.sleep(t//10)
    return sensor(2)

def request_time_interval():
    return tn(HOUR, MIN, SEC)


if __name__ == '__main__':
    timer(0,0,1)