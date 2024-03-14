#include <WiFi.h>

const char* ssid = "InnovationForumGuests";
const char* password = "";

int zone1 = 14;
int zone2 = 13;
int zone3 = 12;
int zone4 = 11;
int zone5 = 10;
int zone6 = 9;
int zone7 = 3;
int zone8 = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);

  WiFi.mode(WIFI_STA); //Optional
  WiFi.begin(ssid, password);
  Serial.println("\nConnecting");

  while(WiFi.status() != WL_CONNECTED){
      Serial.print(".");
      delay(100);
  }

  Serial.println("\nConnected to the WiFi network");
  Serial.print("Local ESP32 IP: ");
  Serial.println(WiFi.localIP());

  pinMode(zone1, INPUT);
  pinMode(zone2, INPUT);
  pinMode(zone3, INPUT);
  pinMode(zone4, INPUT);
  pinMode(zone5, INPUT);
  pinMode(zone6, INPUT);
  pinMode(zone7, INPUT);
  pinMode(zone8, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (analogRead(zone1) >= 2000)
  {
    Serial.println(analogRead(zone1));
    Serial.println("HIT! ZONE1");
  }
  if (analogRead(zone2) >= 2000)
  {
    Serial.println(analogRead(zone2));
    Serial.println("HIT! ZONE2");
  }
  if (analogRead(zone3) >= 2000)
  {
    Serial.println(analogRead(zone3));
    Serial.println("HIT! ZONE3");
  }
  if (analogRead(zone4) >= 2000)
  {
    Serial.println(analogRead(zone4));
    Serial.println("HIT! ZONE4");
  }
  if (analogRead(zone5) >= 2000)
  {
    Serial.println(analogRead(zone5));
    Serial.println("HIT! ZONE5");
  }
  if (analogRead(zone6) >= 2000)
  {
    Serial.println(analogRead(zone6));
    Serial.println("HIT! ZONE6");
  }
  if (analogRead(zone7) >= 2000)
  {
    Serial.println(analogRead(zone7));
    Serial.println("HIT! ZONE7");
  }
  if (analogRead(zone8) >= 2000)
  {
    Serial.println(analogRead(zone8));
    Serial.println("HIT! ZONE8");
  }

  delay(100);
}