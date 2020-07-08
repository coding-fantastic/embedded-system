# print data from serial port to the terminal until program is closed 
import serial

ser = serial.Serial("/dev/ttyACM0",9600)
while True:
    thing = ser.readline()
    print(thing)
