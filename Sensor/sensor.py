import random

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

if __name__ == '__main__':
    print(sensor(2))
