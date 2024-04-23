// Code exécuté sur une carte Arduino MKRWAN pour simuler le mouvement d'un animal, 
// envoyant des données de localisation (et des données de santé facultatives) toutes les 10 secondes.
#include <MKRWAN.h>

LoRaModem modem;

String appEui = "";
String appKey = "";

void setup() {
  Serial.begin(9600);
  while (!Serial);
  if (!modem.begin(EU868)) {
    Serial.println("Failed to start module");
    while (1) {}   // if lora failed, it will stop the execution 
  };
  Serial.print("Your module version is: ");
  Serial.println(modem.version());
  Serial.print("Your device EUI is: ");
  Serial.println(modem.deviceEUI());

  int connected = modem.joinOTAA(appEui, appKey);
  if (!connected) {
    Serial.println("Something went wrong; are you indoor? Move near a window and retry");
    while (1) {}
  }
  modem.minPollInterval(60);
}

void loop() {
  // simulate position and temperature
  int x = random(-250, 250);  
  int y = random(-250, 250); 
  float temperature = random(18, 35) + random(0, 100) / 100.0; 
  
  // create string of msg
  String message = "Panda:" + String(x) + ":" + String(y) + ":T=" + String(temperature);
  Serial.print("Sending: " + topic + message + " - ");
  
  // send msg
  int err;
  modem.beginPacket();
  modem.print(message);
  err = modem.endPacket(true);
  if (err > 0) {
    Serial.println("Message sent correctly!");
  } else {
    Serial.println("Error sending message :(");
  }
  
  delay(10000); // wait 10s
}