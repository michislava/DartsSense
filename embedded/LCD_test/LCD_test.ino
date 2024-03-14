#include <LiquidCrystal.h>

const int rs = 14, en = 13, d4 = 12, d5 = 11, d6 = 10, d7 = 9;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("P1: 100p");
}

void loop() {
}
