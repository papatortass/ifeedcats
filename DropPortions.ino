#include <Servo.h>

Servo servo;
const int servoPin = 9;
const int ledPin = 13;
const int minMoveTime = 130;
const int servingTime = 1400;
const int jerkPeriod = 700;

void setup ()
{
    Serial.begin(57600);
    Serial.println();
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);
    buzz();
}

void loop () 
{
  delay(10);
}

void dispense()
{
  servo.attach(servoPin);
  for(int dispenseTime = servingTime; dispenseTime > 0; dispenseTime -= jerkPeriod)
  {
    servo.write(100);
    delay(dispenseTime >= jerkPeriod ? jerkPeriod : dispenseTime % 1000);
    jerk();
  }
  stop();
}

void jerk()
{
  servo.write(0);
  delay(minMoveTime);
  servo.write(180);
  delay(minMoveTime);
}

void stop()
{
  servo.write(90);
  delay(100);
  servo.detach();
}

void buzz()
{
  servo.attach(servoPin);
  servo.write(0);
  delay(50);
  jerk();
  jerk();
  stop();
}
