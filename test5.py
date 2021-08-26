import sys
from PyQt5 import QtWidgets, QtGui
import serial.tools.list_ports
import matplotlib.pyplot as plt
from drawnow import *
import threading
import time


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

def threadFunc():
     while True:
             if serialInst.in_waiting:
                 packet = serialInst.readline()
                 temp=packet.decode('utf-8').rstrip('\n')
                 x=temp.split("Kg ")
                 if (len(x)>=4):
                     t = x[0]
                     if(len(t)==4):
                         w1=abs(float(t[-4:]))
                     t = x[1]
                    
                     if(len(t)==4):
                         w2=abs(float(t[-4:]))
                     t = x[2]
                     if(len(t)==4):
                         w3=abs(float(t[-4:]))
                     t = x[3]
                     if(len(t)==4):
                         w4=abs(float(t[-4:]))    
                     print("w1 = " + str(w1) + " w2 = "+str(w2)+" w3 = "+str(w3)+" w4 = "+str(w4))
                 #print("we are at this point")

                 l5.setText(str(w1))
                 l6.setText(str(w2))
                 l7.setText(str(w3))
                 l8.setText(str(w4))
                 
th = threading.Thread(target=threadFunc)

w1=0.0
w2=0.0
w3=0.0
w4=0.0
portlist = []

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
l1 = QtWidgets.QLabel(w)
l2 = QtWidgets.QLabel(w)
l3 = QtWidgets.QLabel(w)
l4 = QtWidgets.QLabel(w)
l5 = QtWidgets.QLabel(w) 
l6 = QtWidgets.QLabel(w)
l7 = QtWidgets.QLabel(w)
l8 = QtWidgets.QLabel(w)
l1.setText('Sensor #1')
l2.setText('Sensor #2')
l3.setText('Sensor #3')
l4.setText('Sensor #4')
l5.setText('0.00')
l6.setText('0.00')
l7.setText('0.00')
l8.setText('0.00')
w.setWindowTitle('Sensors weights')
w.setGeometry(100, 100, 300, 200)
l1.move(200, 10)
l2.move(200, 150)
l3.move(10, 150)
l4.move(10, 10)
l5.move(200, 20)
l6.move(200, 160)
l7.move(10, 160)
l8.move(20, 20)  
#w.show()



for OnePort in ports:
    portlist.append(str(OnePort))
    print(str(OnePort))

    val = input("select Port : COM") 
for x in range(0,len(portlist)):
    if portlist[x].startswith("COM"+str(val)):
        portvar="COM"+str(val)
        print(portvar)

        serialInst.baudrate = 9600
        serialInst.port = portvar
        serialInst.open()

        temp = ""
        
        x=[]

        th.start()

        th.join()

#app = QtWidgets.QApplication(sys.argv)
w.show()
sys.exit(app.exec_())