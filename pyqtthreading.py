from re import I
import warnings
import serial
import serial.tools.list_ports
import sys
import matplotlib.pyplot as plt
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QMainWindow


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

w1=0.0
w2=0.0
w3=0.0
w4=0.0
temp = ""
x=[]

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    
    def run(self):
    # """Long-running task."""
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
                #print("we are at this point")

                    
                    # self.s1weight = QLabel(str(w1), self)
                    # self.s2weight = QLabel(str(w2), self)
                    # self.s3weight = QLabel(str(w3), self)
                    # self.s4weight = QLabel(str(w4), self)
                
                
        
             #   self.progress.emit(I)
            #self.finished.emit()


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.w = QtWidgets.QWidget()
        
        self.s1lable = QLabel('Sensor1', self)
        self.s2lable = QLabel('Sensor2', self)
        self.s3lable = QLabel('Sensor3', self)
        self.s4lable = QLabel('Sensor4', self)
        self.s1weight = QLabel(str(w1), self)
        self.s2weight = QLabel(str(w2), self)
        self.s3weight = QLabel(str(w3), self)
        self.s4weight = QLabel(str(w4), self)
                 

        self.setWindowTitle('Sensors weights')
        self.setGeometry(100, 100, 300, 200)
        self.s1lable.move(200, 10)
        self.s2lable.move(200, 150)
        self.s3lable.move(10, 150)
        self.s4lable.move(10, 10)
        self.s1weight.move(200, 20)
        self.s2weight.move(200, 160)
        self.s3weight.move(10, 160)
        self.s4weight.move(20, 20)  
    
    def runLongTask(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.thread.start()



app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())