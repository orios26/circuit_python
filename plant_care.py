from adafruit_circuitplayground.express import cpx 
from time import sleep 
import touchio

#use the touchio library in conjunction with the A1 analog pin 
#we are reading the capacitance of the analog pin which is connected with an aligator clip and metal object 
#as moisture levels increase so does the capacitance value 

while True:
  touch = touchio.TouchIn(A1)
  if cpx.switch:
    if cpx.button_a:
      print("Temp", cpx.temperature)
    if cpx.button_b:
      print("Light: ", cpx.light)
  else:
    print(touch.raw_value)
