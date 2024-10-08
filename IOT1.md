AIM: Displaying different led patterns using Arduino on tinkercad.

STEPS:

1.	Open Google.com > Create an account on TinkerCad using personal account.
2.	Click on Create > Select Circuits > Under the components select BreadBoard and place it in the field > Select Arduino and place it in the field.
3.	Select LED bulb > Place 6 LED bulbs with different colors on the BreadBoard.
4.	Select Resistor > Place 6 Resistor above each LED’s > connect Anode of each LED with it’s corresponding Resistor > now connect each resistor with the GPIO pins of Arduino.
5.	Connect the Cathode of each LED’s with the Ground of the BreadBoard > Connect the BreadBoard Ground with GND pin of the Arduino.
6.	Now open the code section > write the below given code for a wonderful LED pattern.


CODE:

// C++ code
//

int ledr1 = 13;
int ledr2 = 10;
int ledg1 = 12;
int ledg2 = 9;
int ledb1 = 11;
int ledb2 = 8;
  
void setup()
{
void setup()
{
  pinMode(ledr1, OUTPUT);
  pinMode(ledr2, OUTPUT);
  pinMode(ledg1, OUTPUT);
  pinMode(ledg2, OUTPUT);
  pinMode(ledb1, OUTPUT);
  pinMode(ledb2, OUTPUT);
}

void loop()
{
  digitalWrite(ledb1, LOW);
  digitalWrite(ledb2, LOW);
  digitalWrite(ledr1, HIGH);
  digitalWrite(ledr2, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(ledr1, LOW);
  digitalWrite(ledr2, LOW);
  digitalWrite(ledg1, HIGH);
  digitalWrite(ledg2, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(ledg1, LOW);
  digitalWrite(ledg2, LOW);
  digitalWrite(ledb1, HIGH);
  digitalWrite(ledb2, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
}
