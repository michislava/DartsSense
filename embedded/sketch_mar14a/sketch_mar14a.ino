int analog = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(analog, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (analogRead(analog) >= 2000)
  {
    Serial.println(analogRead(analog));
    Serial.println("HIT! TRUST!");
  }
  delay(100);
}