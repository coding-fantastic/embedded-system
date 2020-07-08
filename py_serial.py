# This code will allow me to switch on pin13 using the keyboard letter s 

import serial
import time 

ser1 = serial.Serial("/dev/ttyACM0",9600)
time.sleep(5)
ser1.write("s".encode())

