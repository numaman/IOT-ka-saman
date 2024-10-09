Q. Displaying Time over 4-digit 7-Segment Display using Rasberry Pi.

Requirements:
• Hardware Requirements :
1. Rasberry Pi Model A/B/B+
2. 4 digit 7 Segment/Display
3. Jumper Wires (Female to female)
• Software Requirements :
Raspbian Strech OS
Connection Steps:
1.	Connect your 5v Relay with Raspberry Pi’s GPIO pins using jumperwires(female to female).
LED 1 to GPIO pin
2.	Connect GND pin of raspberry Pi to GROUND of LED Module.
Connect a ground (GND) pin from the Raspberry Pi to the ground rail on the breadboard.




<img width="724" alt="{D192231E-BD1D-409C-9C54-8C85E375BEB9}" src="https://github.com/user-attachments/assets/1c6d5619-f081-46fd-aff2-778be2b9a7f5">

2. Download libraries from :
o https://github.com/timwaizenegger/raspberrypi-examples/tree/master/actor-led-7segment-
4numbers
Click on actor-led-7segment-4numbers.zip folder. Click on Download Button.
3. Unzip the file.
4. Write the python script to display Time & save it in the actor-led-7segment-4numbers folder & run it
5. CODE:


from time import sleep
import tm1637
try:
import thread
except ImportError:
import thread as thread
Display = tm1637.TM1637(CLK=21,DIO=20,brightness=1.0)
try:
  print ("Starting clock in the background (press CTRL + C to stop):")
  Display StartClock(military_time=True)
  Display.SetBrightness(1.0)
  while True:
    Display.ShowDoublepoint(True)
    sleep(1)
    Display Show Doublepoint(False)
    sleep(1)
    Display StopClock()
    thread.interrupt_main()
except Keyboardinterrupt:
  print ("Properly closing the clock and open GPIO pins")
  Display.cleanup()


CODE:
import tm1637
import time

display = tm1637.TM1637(DIO=29,CLK=31,brightness=1.0)
print("Showing time of the clock")
display.StartClock(miltary_time=True)
try:
	while 1:
		display.ShowDoublePoint(True)
		time.sleep(1)
		display.ShowDoubleTime(False)

except KeyboardIterrupt:
	display.StopClock()
	display.cleanup()


 sudo python3 time.py
