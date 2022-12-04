const int ledPin=13;
String nom = "Arduino";
String msg;
void setup() {
   Serial.begin(9600);
   pinMode(ledPin,OUTPUT); //règle la borne numérique numéro 1 de la carte Arduino en mode sortie
}

void loop() {
  readSerialPort();
  if (msg == "data") {
      sendData();
  }else if(msg=="led0"){
      digitalWrite(ledPin,LOW);
      Serial.print(" Arduino set led to LOW");
  }else if(msg=="led1"){
      digitalWrite(ledPin,HIGH);
      Serial.print(" Arduino set led to HIGH");
  }
  delay(500);
}

void readSerialPort() {
  msg = "";
  if (Serial.available()) {
      delay(10);
      while (Serial.available() > 0) {
          msg += (char)Serial.read();
      }
      Serial.flush();
  }
}

void sendData() {
  //write data ledState x sensor1 x sensor2
  Serial.print(digitalRead(ledPin));
  Serial.print("x");
  Serial.print(analogRead(A0));
  Serial.print("x");
  Serial.print(analogRead(A1));
}
