#include <WiFi.h>
#include <IRremote.h>
#include <HTTPClient.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

const char* ssid = "InnovationForumGuests";
const char* password = "";
const char* serverAddress = "";

//i2c pins used to control lcd display
#define I2C_SDA 21
#define I2C_SCL 20

int lcdColumns = 16;
int lcdRows = 2;

LiquidCrystal_I2C lcd(0x27, lcdColumns, lcdRows);  

//ir object bound to gpio19
IRrecv IR(19);

//IR CODES TABLE
#define IR0 0xFFFFFFFF
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

//player throws
int p1throws = 0;
int p2throws = 0;
int p3throws = 0;
int p4throws = 0;

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
  Wire.begin(I2C_SDA, I2C_SCL);
  lcd.init();
  lcd.backlight();
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

  sendData();

  lcd.setCursor(0, 0);
  // print message
  lcd.print("kak sa statane");
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
        p1throws++;
      break;

      case 2:
        p2pts += pointsToEarn;
        p2throws++;
      break;

      case 3:
        p3pts += pointsToEarn;
        p3throws++;
      break;

      case 4:
        p4pts += pointsToEarn;
        p4throws++;
      break;

      default:
      break;
    }
    
    hit = 0;
    //player points display
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

  //player lcd display
  switch(playerTurn)
    {
      case 1:
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Player 1: " + String(p1pts));
        lcd.setCursor(0, 1);
        lcd.print("Throws: " + String(p1throws));
      break;
      case 2:
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Player 2: " + String(p2pts));
        lcd.setCursor(0, 1);
        lcd.print("Throws: " + String(p2throws));
      break;
      case 3:
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Player 3: " + String(p3pts));
        lcd.setCursor(0, 1);
        lcd.print("Throws: " + String(p3throws));
      break;
      case 4:
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Player 4: " + String(p4pts));
        lcd.setCursor(0, 1);
        lcd.print("Throws: " + String(p4throws));
      break;
    }
  delay(100);
}

void sendData() {
  
  HTTPClient http;
  
  if (WiFi.status() == WL_CONNECTED) // Check if WiFi is connected
  {
    http.begin(serverAddress); // Your Flask server endpoint
    http.addHeader("Content-Type", "application/json"); // Specify content type
    
    String jsonData = "{\'player\' : 1; \'zone\' : 1}"; // Create JSON payload
    int httpResponseCode = http.POST(jsonData); // Send the POST request
    

    if (httpResponseCode > 0) // Check for errors
    {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("HTTP Error: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("WiFi not connected. Skipping HTTP request.");
  }
}