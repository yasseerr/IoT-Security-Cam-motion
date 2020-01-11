
#include "ESP8266WiFi.h"
int const PIR_PIN = 13 ;  //D7
int const LED_PIN = 12 ; //D6

int isThereMotion = 0;

const char *ssid = "paubua new guiyana";
const char *password = "11111111";

void setup()
{

    // Connect to Wi-Fi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi..");
    }
    // Print ESP32 Local IP Address
    pinMode(LED_PIN, OUTPUT);
    pinMode(PIR_PIN, INPUT);
    Serial.begin(115200);
}

void loop()
{
   if (digitalRead(PIR_PIN) == 1)
   {
       digitalWrite(LED_PIN, HIGH);
   }
   else
   {
       digitalWrite(LED_PIN, LOW);
   }
   
   
}