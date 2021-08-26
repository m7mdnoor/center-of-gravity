import serial.tools.list_ports
import warnings
import serial





w1=0.0
w2=0.0
w3=0.0
w4=0.0




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



while True:
  while(serialInst.in_waiting()==0):
    pass
  Wt=str(w1)+str(w2)+str(w3)+str(w4)
  MX1 = str(w1)*4.5
  MY1 = str(w1)*21.5
  MX2 = str(w2)*4.5
  MY2 = str(w2)*3.2
  MX3= str(w3)*23.5
  MY3= str(w3)*3.2
  MX4 = str(w4)*23.5
  MY4 = str(w4)*21.5
  MXt = MX1 + MX2 + MX3 + MX4
  MYt = MY1 + MY2 + MY3 + MY4
  Xcg = MXt / Wt
  Ycg = MYt / Wt    
  drawnow(makefig)
  plt.plot(Xcg,Ycg)
  plt.clf()
  plt.show()
  # plt.pause(.000001) 


      


  






# (x1= ,y1)=(4.5,21.5)
# (x2= ,y2)=(4.5,3.2)
# (x3= ,y3)=(23.5,3.2)
# (x4= ,y4)=(23.5,21.5)
# Wt= sum of weights
#MXi = The X-Moment of LCi = Wi*Xi.
#MYi = The Y-Moment of LCi = Wi*Yi.
#MXt = The total X-Moment = sum of all MXi = Wt*Xcg
#MYt = The total Y-Moment = sum of all MYi = Wt*Ycg
#(Xcg,Ycg) = The position of the CoG (Center of Gravity).
#Xcg = MXt / Wt
#Ycg = MYt / Wt
#width of scale is 28cm and the highet is 28cm

#Wt=w1+w2+w3+w4 #total weight

#for first sensor
#MX1 = w1*4.5
#MY1 = w1*21.5

#for second sensor
#MX2 = w2*4.5
#MY2 = w2*3.2

#for third sensor
#MX3= w3*23.5
#MY3= w3*3.2            

#for fourth sensor

#MX4 = w4*23.5
#MY4 = w4*21.5

#MXt = MX1 + MX2 + MX3 + MX4
#MYt = MY1 + MY2 + MY3 + MY4

#Xcg = MXt / Wt
#Ycg = MYt / Wt             
