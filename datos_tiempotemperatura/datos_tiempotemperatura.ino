#include <OneWire.h>
#include <DallasTemperature.h>

const int pinDatosDQ = 2;
OneWire oneWireObjeto(pinDatosDQ);
DallasTemperature sensorDS18B20(&oneWireObjeto);

void setup() {
  Serial.begin(9600);
  sensorDS18B20.begin();
}

void loop() {
  unsigned long currentMillis = millis();  // Obtener el tiempo actual en milisegundos

  sensorDS18B20.requestTemperatures();
  float temperatura = sensorDS18B20.getTempCByIndex(0);

  // Imprimir el tiempo de medición, la temperatura y un salto de línea
  Serial.print(currentMillis);
  Serial.print(", ");
  Serial.println(temperatura);

  delay(1000);
}
