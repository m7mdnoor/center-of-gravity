from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import warnings
import serial
import serial.tools.list_ports
import time
import threading

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description  # may need tweaking to match new arduinos
]
if not arduino_ports:
    raise IOError("No Arduino found")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[0])
ser.baudrate = 9600

w1=1.0
w2=1.0
w3=1.0
w4=1.0

temp = ""
x=[]
while True:
    if ser.in_waiting:
        packet = ser.readline()
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
    Wt=float(w1)+float(w2)+float(w3)+float(w4)
    MX1 = float(w1)*4.5
    MY1 = float(w1)*21.5
    MX2 = float(w2)*4.5
    MY2 = float(w2)*3.2
    MX3= float(w3)*23.5
    MY3= float(w3)*3.2
    MX4 = float(w4)*23.5
    MY4 = float(w4)*21.5
    MXt = MX1 + MX2 + MX3 + MX4
    MYt = MY1 + MY2 + MY3 + MY4
    Xcg = MXt / Wt
    Ycg = MYt / Wt    

    print(Xcg)
    print(Ycg)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Center of Gravity Graph"
        self.top = 200
        self.left = 200
        self.width = 500
        self.height = 500
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
   
    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.drawEllipse(250,250,4,4)   
      
        painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        painter.drawEllipse(Xcg,Ycg,4,4)   


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
