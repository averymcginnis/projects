// Blinky Ring Thing
// 12 LEDs in a ring, use switch to stop the light on the top LED to win.

#define button 13
int i = 1;
int j = 0;
int buttonState = 0;
int lastButtonState = 0;
int lastLight = 12;

void setup()
{
  pinMode(button,INPUT);
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(1,OUTPUT);
  digitalWrite(lastLight,HIGH);
}

void loop()
{
  buttonState = digitalRead(button);
  if (buttonState != lastButtonState)
  {
    digitalWrite(lastLight,LOW);
    for (i;i < 13;i++)
    {
      buttonState = digitalRead(button);
      if (buttonState == lastButtonState)
      {
        digitalWrite(i,HIGH);
        lastLight = i;
        if (i == 12)
        {
          for (j;j<3;j++)
          {
            digitalWrite(1,HIGH);
            digitalWrite(2,HIGH);
            digitalWrite(3,HIGH);
            digitalWrite(4,HIGH);
            digitalWrite(5,HIGH);
            digitalWrite(6,HIGH);
            digitalWrite(7,HIGH);
            digitalWrite(8,HIGH);
            digitalWrite(9,HIGH);
            digitalWrite(10,HIGH);
            digitalWrite(11,HIGH);
            digitalWrite(12,HIGH);
            delay(400);
            digitalWrite(1,LOW);
            digitalWrite(2,LOW);
            digitalWrite(3,LOW);
            digitalWrite(4,LOW);
            digitalWrite(5,LOW);
            digitalWrite(6,LOW);
            digitalWrite(7,LOW);
            digitalWrite(8,LOW);
            digitalWrite(9,LOW);
            digitalWrite(10,LOW);
            digitalWrite(11,LOW);
            digitalWrite(12,LOW);
            delay(400);
          }
          digitalWrite(12,HIGH);
        }
        j = 0;
        break;
      }
      
      digitalWrite(i,HIGH);
      delay(35);
      digitalWrite(i,LOW);
      
    buttonState = digitalRead(button);
      if (buttonState == lastButtonState)
      {
        digitalWrite(i,HIGH);
        lastLight = i;
        if (i == 12)
        {
          for (j;j<3;j++)
          {
            digitalWrite(1,HIGH);
            digitalWrite(2,HIGH);
            digitalWrite(3,HIGH);
            digitalWrite(4,HIGH);
            digitalWrite(5,HIGH);
            digitalWrite(6,HIGH);
            digitalWrite(7,HIGH);
            digitalWrite(8,HIGH);
            digitalWrite(9,HIGH);
            digitalWrite(10,HIGH);
            digitalWrite(11,HIGH);
            digitalWrite(12,HIGH);
            delay(400);
            digitalWrite(1,LOW);
            digitalWrite(2,LOW);
            digitalWrite(3,LOW);
            digitalWrite(4,LOW);
            digitalWrite(5,LOW);
            digitalWrite(6,LOW);
            digitalWrite(7,LOW);
            digitalWrite(8,LOW);
            digitalWrite(9,LOW);
            digitalWrite(10,LOW);
            digitalWrite(11,LOW);
            digitalWrite(12,LOW);
            delay(400);
          }
          digitalWrite(12,HIGH);
        }
        j = 0;
        break;
      }
      
      if (i == 12)
      {
        i = 0;
      }
    }
  }
}
