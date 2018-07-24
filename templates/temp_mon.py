import os
import time

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","").replace('\\n', ' '))

while True:
        print(os.uname()[1] + '\'s cpu temp: '  + measure_temp()),
        time.sleep(1)