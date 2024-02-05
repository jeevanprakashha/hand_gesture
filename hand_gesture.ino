#include <AFMotor.h>
AF_DCMotor m1(1);
AF_DCMotor m2(2);
void setup()
{
  Serial.begin(9600);
}
void loop(){
if(Serial.available())
{
  int c = Serial.parseIntO;
  Serial.println(c);
  if (c == 0) //forward
  {
    m1.run(RELEASE); 
    m2.run(RELEASE);
  }
  //custom
}}
