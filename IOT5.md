Aim: Interfacing Ultrasonic Sensor with Arduino using Tinkercad.

            Steps:
•	Go to https://www.tinkercad.com & login using your account.
•	Click on Create  Circuits to get a blank canvas with basic components.
•	Select Arduino Uno R3, Ultrasonic  sensor & drop them on the canvas.
•	Connect the Arduino and Ultrasonic sensor through wires.
•	Connections
1.	Vcc : 5v
2.	Trg : -10
3.	Echo : -9
4.	GND : GND
•	After the connection > Now open the code section > write the below given code.

Code:
int trigPin= 10;
int echoPin = 9;
long time;
int distance;

void setup()
{
  pinMode(10,OUTPUT);
  pinMode(9,INPUT);
  Serial.begin(9600);
}

void loop()
{
  	digitalWrite(10,LOW);
 	 delayMicroseconds(2);
  
  digitalWrite(10,HIGH);
  	delayMicroseconds(10);
  	digitalWrite(10,LOW);
  
time = pulseIn(9,HIGH);
 	distance = time*0.034/2;
  
  Serial.print("Distance:");
  	Serial.println(distance);
	}
