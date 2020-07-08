import serial
import matplotlib.pyplot as plt

plt.ion();
fig = plt.figure()
i=0
x=list()
y=list()
ser =serial.Serial("/dev/ttyACM0", 9600)
ser.close()
ser.open()
timeout =0;

while timeout < 100:
    data = ser.readline()
    print(data.decode())
    # print when its less than 200
    if (int(data.decode()) < 200):

        x.append(i)
        y.append(data.decode())
        plt.scatter(i, float(data.decode()))
        i+=1;
        timeout+=1;
        plt.show()
        plt.pause(0.0001)
