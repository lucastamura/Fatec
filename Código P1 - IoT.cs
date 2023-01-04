//Declaração de variáveis

const float pi = 3.14159265;     //Número de pi
int tempo = 5000;                //Tempo de medida(miliseconds)
int intervalo = 2000;            //Invervalo entre as amostras (miliseconds)
int raio = 147;                  //Raio do anemometro(mm)

unsigned int guarda  = 0;         //Armazena o número de amostras
unsigned int contador = 0;        //Contador para o sensor
unsigned int RPM = 0;             //Rotações por minuto
float velocidade = 0;              //Velocidade do vento (km/h)


// -- definir o setup
void setup() {
  pinMode(2, INPUT);        //indica a entrada 2
  digitalWrite(2, HIGH);    //ativa a entrada 2

  Serial.begin(9600);       //inicia serial em 9600 baud rate
}

// -- definir o loop
void loop() {

  // indica a quantidade de leituras
  guarda++;
  Serial.print(guarda);
  Serial.print("- Inicia Leitura...");

  // indica a quantidade de RPM
  windvelocity();
  Serial.println("   Finalizado.");
  Serial.print("Contador: ");
  Serial.print(contador);
  Serial.print(";  RPM: ");
  RPMcalc();
  Serial.print(RPM);
  Serial.print(";  Vel. Vento: ");

  //Indica a velocidade em km/h
  SpeedWind();
  Serial.print(velocidade);
  Serial.print(" [km/h] ");
  Serial.println();

  delay(intervalo); 
} 



//Função para medir velocidade do vento
void windvelocity() {

  velocidade = 0;

  contador = 0;
  attachInterrupt(0, addcount, RISING);
  unsigned long millis();
  long startTime = millis();
  while (millis() < startTime + tempo) {}
}

//Função para calcular o RPM
void RPMcalc() {
  RPM = ((contador) * 60) / (tempo / 1000); // Calcular as rotações por minuto (RPM)
}

//Velocidade do vento em km/h
void SpeedWind() {
  velocidade = (((4 * pi * raio * RPM) / 60) / 1000) * 3.6; //Calcula velocidade do vento em km/h
} 

//Incrementa contador
void addcount() {
  contador++;
}
