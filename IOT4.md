AIM: Implement Braille Script via leds and Arduino using Tinkercad.

STEPS:

1.	Open Google.com  Create an account on TinkerCad using personal account.
2.	Click on Create Select Circuits  Under the components select BreadBoard and place it in the field Select Arduino and place it in the field.
3.	Select LED bulb Place 6 LED on the BreadBoardPlace the 6 LEDs on the breadboard in two columns and three rows, representing the 2x3 Braille grid.
4.	Select Resistor  Place 6 Resistor below each LED’s connect Anode to a row on the breadboard where you will later connect it to the Arduino.
5.	Connect the Cathode of each LED’s with the Ground of the BreadBoard Connect the BreadBoard Ground with GND pin of the Arduino.
6.	Now open the code section  write the below given code for a wonderful LED pattern.


CODE:
// C++ code
//
void setup()
{
  pinMode(8, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop()
{
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(8, LOW);
  delay(2000);
  
  digitalWrite(13, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, LOW);
  digitalWrite(10, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(8, LOW);
  delay(2000);
  
  digitalWrite(13, HIGH);
  digitalWrite(12, LOW);
  digitalWrite(11, LOW);
  digitalWrite(10, LOW);
  digitalWrite(9, LOW);
  digitalWrite(8, LOW);
  delay(2000);

  digitalWrite(13, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, LOW);
  digitalWrite(10, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(8, LOW);
  delay(2000);
  
  digitalWrite(13, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(10, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(8, LOW);
  delay(2000);
  
  digitalWrite(13, HIGH);
  digitalWrite(12,  LOW);
  digitalWrite(11, HIGH);
  digitalWrite(10, LOW);
  digitalWrite(9,  LOW);
  digitalWrite(8,HIGH);
  delay(2000);
  
  digitalWrite(13, HIGH);
  digitalWrite(12,  LOW);
  digitalWrite(11, HIGH);
  digitalWrite(10, LOW);
  digitalWrite(9,  LOW);
  digitalWrite(8, LOW);
  delay(2000);
   
  digitalWrite(13, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(11, LOW);
  digitalWrite(10, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(8, LOW);
  delay(2000);
}

