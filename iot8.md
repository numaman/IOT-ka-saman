8. Raspberry Pi based Oscilloscope.
Requirements:
• Hardware Requirements :
1. Jumper Wires (Female to female)
• Software Requirements :
Raspbian Strech OS
STEPS:
1. Connect your ADC with Raspberry Pi’s GPIO Pins.

<img width="559" alt="image" src="https://github.com/user-attachments/assets/4fb4bf12-c21b-4b7e-b3d1-ab22c6de579d">

2. Enable Raspberry Pi 12C interface.
sudo raspi-config OR
Go to Interfacing Options →12C→Enable (Yes)

3: Update the Raspberry Pi
sudo apt-get update
sudo apt-get upgrade

4: Install the Adafruit ADS1115 library for ADC
To install the dependencies starting with the Adafruit python module for the ADS115 chip, Ensure you
are inthe Raspberry Pi home directory ($ cd ~)
sudo apt-get install build-essential python-dev python-smbus git
In the next line sudo apt install Python3-smbus
Next, clone the Adafruit git folder for the library by running

git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
use sudo
Change into the cloned file's directory and run the setup file
cd /home/pi/Adafruit Python_ADS1x15/
sudo python3 setup.py install

5: Test the library and 12C communication.
Now, it is important to test the library and ensure the ADC can communicate with the raspberry pi over
I2C. To do this use an example script that comes with the library.
$ cd examples
$ python simpletest.py

If the I2C module is enabled and connections good, it should display the data as below If an error
occurs, check to ensure the ADC is well connected to the PI and 12C communication is enabled on the Pi.
Step 6: Install Matplotlib (in home directory)
sudo apt-get install python3-matplotlib


**CODE:**
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val = []

adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')

fig, ax = plt.subplots()
ax.set_ylim(-5000,5000)
ax.set_title('Oscilloscope')
ax.grid(True)
ax.set_ylabel('ADC outputs')

line, = ax.plot([], 'ro-', label='Channel 0')
ax.legend(loc='lower right')

def update(cnt):
  value = adc.get_last_result()
  print('Channel 0: {0}'.format(value))
  line.set_data(list(range(len(val))),val)
  ax.relim()
  ax.autoscale_view()
  val.append(int(value))
  if(cnt>50):
    val.pop(0)
ani = FuncAnimation(fig, update, interval=500)
plt.show()

