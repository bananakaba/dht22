#include <DHT.h>
#include <DHT_U.h>

// definitions
#define DHTPIN 2          // pin of the arduino where the sensor is connected to
#define DHTTYPE DHT22     // define the type of sensor (DHT11 or DHT22)
       
// create instance of DHT                          
DHT dht(DHTPIN, DHTTYPE, 6);

void setup()
{
  Serial.begin(9600);
  dht.begin();
}

void loop()
{
  // Wait 30 seconds between measurements (2 Seconds minimum required)
  delay(30000);
                                   
  float h = dht.readHumidity();
  float t = dht.readTemperature();
 
  // validate values
  if (isnan(h) || isnan(t)) {      
    Serial.println("Error while reading data!");
    return;
  }

  Serial.print(h);
  Serial.println(t);

}