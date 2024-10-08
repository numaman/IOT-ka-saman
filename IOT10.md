10. IoT based Web Controller Home Automation using Raspberry Pi.
Hardware Requirement:
1. Raspberry Pi Model B/B+ 5vRelays
2. LEDs to test
3. Jumperwires (female to female)
Software Requirements:
1. Raspbian StreachOS
2. WebIOPI framework
Connection Steps:
1. Connect your 5v Relay with Raspberry Pi’s GPIO pins using jumperwires(female to female).
LED 1 to GPIO pin
2. Connect GND pin of raspberry Pi to GROUND of LED Module.
Connect a ground (GND) pin from the Raspberry Pi to the ground rail on the breadboard.
STEPS:
1) Download th WebIOPI Framework file:
Use wget command to get the installer file of WebIOPI framework from sourceforge page .
Make sure that you are in home directory.
COMMAND:
wget https://sourceforge.net/projects/webiopi/files/WebIOPI-0.7.1.tar.gz
Extract the files uaing tar command
COMMAND:
tar xzvf WebIOPI-0.7.1/
2) Install patch file:
COMMAND:
wget https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch
install the patch file using patch command:
COMMAND:
patch -p1 -I webiopi-pi2bplus.patch
a. Install setup of WebIOPi framework, Run setup file.
COMMAND:
./setup.sh

Reboot the system:
sudo reboot

3) Test WebIOPi Installation.
We will need to test our WebIOPi installation to be sure everything works fine as desired. Run
following command on terminal.
sudo webiopi -d -c /etc/webiopi/config
Now, open web browser and connect to http://PI's IP address:8000
4) The system will prompt you to for username and password.
Username: webiopi
Password: raspberry
5) Go to GPIO Header from WebIOPI Main Menu
Test your devices which are connected to Raspberry Pi’s GPIO pins. This way we can control Raspberry
Pi GPIO using WebIOPI.
