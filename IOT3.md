Q. 3) Interfacing LCD display with Arduino using Tinkercad

Steps: 
1.	Go to https://www.tinkercad.com & login using your account.
2.	Click on Create  Circuits to get a blank canvas with basic components.
3.	Select breadboard, Arduino Uno R3, Potentiometer & drop them on the canvas.
4.	Make positive to 5v and Negative to GND (Ground) connection to the board & connect LED’s and Resistors accordingly(220Ω).(note: resistors in different column.)
5.	Connections: 
•	Arduino – LCD:
12 – RS
11 – RW
5 – DB4
4 – DB5
3 – DB6
2 – DB7

•	LCD – Breadboard
VCC - positive
RW – negative
LED - negative

•	Potentiometer
Left pin – positive (breadboard)
Middle pin – V0 (LED)
Right pin – GND (LED)

6.	Start stimulation.

Code:
#include <LiquidCrystal.h>

int seconds = 0;
LiquidCrystal lcd_1(12, 11, 5, 4, 3, 2);

void setup()
{
  lcd_1.begin(16, 2);
  lcd_1.print("SHAHRUKH");
}

void loop()
{
  lcd_1.setCursor(0, 1);
  lcd_1.print(seconds);
  delay(1000);
  seconds += 1;
}
