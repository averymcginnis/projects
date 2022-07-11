// Northbound/southbound lights
const int nsRed = 12;
const int nsYellow = 11;
const int nsGreen = 10;

// Eastbound/westbound lights
const int ewRed = 7;
const int ewYellow = 6;
const int ewGreen = 5;

void setup() 
{
  // Declare the LEDs pins as output pins.
  pinMode(nsRed,OUTPUT);
  pinMode(nsYellow,OUTPUT);
  pinMode(nsGreen,OUTPUT);
  pinMode(ewRed,OUTPUT);
  pinMode(ewYellow,OUTPUT);
  pinMode(ewGreen,OUTPUT);

  // Turn all lights off to begin.
  digitalWrite(nsRed,LOW);
  digitalWrite(nsYellow,LOW);
  digitalWrite(nsGreen,LOW);
  digitalWrite(ewRed,LOW);
  digitalWrite(ewYellow,LOW);
  digitalWrite(ewGreen,LOW);
}

void loop() 
{
  // Northbound/southbound light is green for 48 seconds.
  digitalWrite(nsGreen,HIGH);
  digitalWrite(ewRed,HIGH);
  delay(48000);

  // Northbound/southbound light turns yellow for 5 seconds.
  digitalWrite(nsGreen,LOW);
  digitalWrite(nsYellow,HIGH);
  delay(5000);

  // Northbound/southbound light turns red, delay 4 seconds until turning 
  // eastbound/westbound light green for 16 seconds.
  digitalWrite(nsYellow,LOW);
  digitalWrite(nsRed,HIGH);
  delay(4000);
  digitalWrite(ewRed,LOW);
  digitalWrite(ewGreen,HIGH);
  delay(16000);

  // Eastbound/westbound light turns yellow for 5 seconds.
  digitalWrite(ewGreen,LOW);
  digitalWrite(ewYellow,HIGH);
  delay(5000);

  // Eastbound/westbound light turns red, delay 4 seconds.
  digitalWrite(ewYellow,LOW);
  digitalWrite(ewRed,HIGH);
  delay(4000);
  digitalWrite(nsRed,LOW);
}
