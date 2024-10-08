Q.) Controlling Raspberry Pi with Telegram.

Steps for connecting telegram:
• Connect LED module to GPIO pins:
1. GND = 39
2. LED = 38
3. LED1 = 40
• Download Telegram App - Go to search Bat Father → Bot Father chat → /stat/newbot
→ Enter a Enter a username Name for bot Eg.TYIT2024
• Enter a username Demo_bot . Must end with "bot"
• You will get an access Token.
• Now connect the pins for LED.
(2Leds Atleast)
• After writing the code Go to terminal
→sudo apt-get update
→sudo apt-get install python-pip.
→sudo apt pip install relepot
• Python telegram.py should give you but details
• search with username, on Telegram
• click on start
• On

CODE:

import random
import datetime
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop
import time
red=40
red1=38
now=datetime.datetime.now()
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(red1,GPIO.OUT)
GPIO.output(red,0)
GPIO.output(red1,0)
def action(msg):
chat_id=msg['chat']['id']
command=msg['text']
print('Got command: %s' %command)

if 'On' in command:
  message="Turn On"
  message=message+"red"
  GPIO.output(red,1) GPIO.output(red1,1)
  bot.sendMessage(chat_id, message)
  if 'Blink' in command:
  while 'Blink':
  message="Turn On"
  message=message+"red"
  GPIO.output(red,1)
  time.sleep(0.5)
  GPIO.output(red,0)
  time.sleep(0.5)
  GPIO.output(red1,1)
  time.sleep(0.5)
  GPIO.output(red1,0)
  time.sleep(0.5)
  bot.sendMessage(chat_id,message)

if 'Off' in command:
  message="Turn Off"
  message=message+"red"
  GPIO.output(red,0)
  GPIO.output(red1,0)
  bot.sendMessage(chat id, message)
bot = telepot.Bot('7443147530:AAFyEj6xVtdBajuAkjo5dLawpDodbgjX9L0')
print(bot.getMe())
MessageLoop (bot,action).run as thread()
print('I am Listening....”)
while 1:
time.sleep(10)
