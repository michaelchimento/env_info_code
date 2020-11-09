import datetime
import busio
import os
import sys
import time
import board
import adafruit_bh1750
import adafruit_si7021

 
i2c = board.I2C()
 
# Create library object using our Bus I2C port

try:
    sensor = adafruit_bh1750.BH1750(i2c) #lux sensor
    sensor2 = adafruit_si7021.SI7021(i2c) #temp/ humidity sensor


except Exception as e:
    print("problem with sensor: {}".format(e))
    sys.exit()

location="Gblock1"


time_stamp = datetime.datetime.now()
print("program is starting at {}".format(time_stamp))
file_name = "/home/pi/env_info_code/data/environmental_info_{}.csv".format(time_stamp.date())

if not os.path.isfile(file_name):
   with open(file_name, "a") as savefile:
       header = "timestamp,location,lux,temperature,humidity\n"
       savefile.write("#{} start time: {} \n".format(location,time_stamp))
       savefile.write(header)
else:
    with open(file_name, "a") as savefile: # open data file in write mode
        savefile.write("#{} start time: {} \n".format(location,time_stamp))

while __name__=="__main__":
    
    #read from lux sensor
    current_lux = sensor.lux
    
    #read from temp humidity sensor
    current_temp = sensor2.temperature
    current_humidity = sensor2.relative_humidity
    time_stamp = datetime.datetime.now()
    write_line = "{},{},{},{},{}\n".format(time_stamp,location,current_lux,current_temp,current_humidity)
    print(write_line)
    with open(file_name, "a") as savefile: # open data file in write mode
        savefile.write(write_line)
    time.sleep(600)
