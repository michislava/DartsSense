#include <WiFi.h>
#include <IRremote.h>

const char* ssid = "InnovationForumGuests";
const char* password = "";

IRrecv IR(19);

//IR CODES TABLE
#define IR1 0xF30CFF00
#define IR2 0xE718FF00
#define IR3 0xA15EFF00
#define IR4 0xF708FF00
#define IR5 0xE31CFF00
#define IR6 0xE31CFF00

//ZONE PINS
int zone1 = 14;
int zone2 = 13;
int zone3 = 12;
int zone4 = 11;
int zone5 = 10;
int zone6 = 9;
int zone7 = 3;
int zone8 = 8;

//player logic
int playerTurn = 1;
int p1pts = 0;
int p2pts = 0;
int p3pts = 0;
int p4pts = 0;

int hit = 0;
int pointsToEarn = 0;

//POINTS TABLE
#define ZONE1_PTS 20
#define ZONE2_PTS 50
#define ZONE3_PTS 10
#define ZONE4_PTS 8
#define ZONE5_PTS 3
#define ZONE6_PTS 15
#define ZONE7_PTS 18
#define ZONE8_PTS 11

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  IR.enableIRIn();  
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

  hit = 0;

  if (IR.decode())
  {
    Serial.println(IR.decodedIRData.decodedRawData, HEX);
    /*
    if(IR.decodedIRData.decodedRawData == IR1)
    {
      Serial.println("cenk");
    }
    */
    switch(IR.decodedIRData.decodedRawData)
    {
      case IR1:
        Serial.println("Player1 Selected");
        playerTurn = 1;
      break;
      case IR2:
        Serial.println("Player2 Selected");
        playerTurn = 2;
      break;
      case IR3:
        Serial.println("Player3 Selected");
        playerTurn = 3;
      break;
      case IR4:
        Serial.println("Player4 Selected");
        playerTurn = 4;
      break;
    }
    delay(1500);
    IR.resume();
  }

  if (analogRead(zone1) >= 2000)
  {
    Serial.println(analogRead(zone1));
    hit = 1;
    pointsToEarn = ZONE1_PTS;
    Serial.println("HIT! ZONE1");
  }
  if (analogRead(zone2) >= 2000)
  {
    Serial.println(analogRead(zone2));
    hit = 1;
    pointsToEarn = ZONE2_PTS;
    Serial.println("HIT! ZONE2");
  }
  if (analogRead(zone3) >= 2000)
  {
    Serial.println(analogRead(zone3));
    hit = 1;
    pointsToEarn = ZONE3_PTS;
    Serial.println("HIT! ZONE3");
  }
  if (analogRead(zone4) >= 2000)
  {
    Serial.println(analogRead(zone4));
    hit = 1;
    pointsToEarn = ZONE4_PTS;
    Serial.println("HIT! ZONE4");
  }
  if (analogRead(zone5) >= 2000)
  {
    Serial.println(analogRead(zone5));
    hit = 1;
    pointsToEarn = ZONE5_PTS;
    Serial.println("HIT! ZONE5");
  }
  if (analogRead(zone6) >= 2000)
  {
    Serial.println(analogRead(zone6));
    hit = 1;
    pointsToEarn = ZONE6_PTS;
    Serial.println("HIT! ZONE6");
  }
  if (analogRead(zone7) >= 2000)
  {
    Serial.println(analogRead(zone7));
    hit = 1;
    pointsToEarn = ZONE7_PTS;
    Serial.println("HIT! ZONE7");
  }
  if (analogRead(zone8) >= 2000)
  {
    Serial.println(analogRead(zone8));
    hit = 1;
    pointsToEarn = ZONE8_PTS;
    Serial.println("HIT! ZONE8");
  }

  if (hit == 1)
  {
    switch(playerTurn)
    {
      case 1:
        p1pts += pointsToEarn;
      break;

      case 2:
        p2pts += pointsToEarn;
      break;

      case 3:
        p3pts += pointsToEarn;
      break;

      case 4:
        p4pts += pointsToEarn;
      break;

      default:
      break;
    }
    
    hit = 0;

    Serial.println("P1 Points:");
    Serial.println(p1pts);
    Serial.println("P2 Points:");
    Serial.println(p2pts);
    Serial.println("P3 Points:");
    Serial.println(p3pts);
    Serial.println("P4 Points:");
    Serial.println(p4pts);
    delay(1000);
  }

  delay(100);
}