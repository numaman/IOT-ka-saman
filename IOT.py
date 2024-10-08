Q.) Displaying different LED patterns with raspberry Pi.
STEPS:
1) Connect LEDs to GPIO pins.
LED1 = 35
LED2 = 33
LED3 = 31
LED4 = 21
2) Connect GND pin of raspberry Pi to GROUND of LED Module.
GND = 39
3) Write Code in Thonny IDLE.
CODE:
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led1=35
led2=33
led3=31
led4=21
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)
GPIO.output(led1, False)
GPIO.output(led2, False)
GPIO.output(led3,False)
GPIO.output(led4, False)
def ledpattern(v1, v2, v3,v4):
GPIO.output(led 1.v1)
GPIO.output(led2,v2)
GPIO.output(led3,v3)
GPIO.output(led4,v4)

try:
  while True:
    for i in range(0,4):
      ledpattern(1,0,0,0)
      time.sleep(0.5)
      ledpattern(0,1,0,0)
      time.sleep(0.5)
      ledpattern(0,0,1,0)
      time.sleep(0.5)
      ledpattern(0,0,0,1)
      time.sleep(0.5)
finally:
  GPIO.cleanup()
