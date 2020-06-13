const int S = 7;

int prev;
int now;

void setup() {
  Serial.begin(9600);
  pinMode(S, INPUT_PULLUP);
  prev = HIGH;
  now = HIGH;
}

void loop() {
  now = digitalRead(S);

  if(prev == HIGH && now == LOW){
    Serial.println("Pressed");
    delay(10);
  }

  prev = now;
  delay(10);
}
