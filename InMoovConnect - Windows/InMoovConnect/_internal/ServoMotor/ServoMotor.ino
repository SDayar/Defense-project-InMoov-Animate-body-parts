///@author Saifidine Dayar
///@brief ServoMotor est responsable de la partie électronique et mécanique du projet. Ce module reçoit un signal et le traite puis l'intereprète selon son contenu.
///@date 25/03/2025
///@version 10/05/2025
///@file ServoMotor.ino


///@brief Importation des bibliothèques nécessaires

///@see https://www.arduino.cc/reference/en/libraries/servo
#include <Servo.h>
///@see https://arduinojson.org
#include <ArduinoJson.h>

 
///@def NB_FINGERS_AND_WRIST
///@brief Nombre de doigts et de poignet
#define NB_FINGERS_AND_WRIST 6
///@def NB_MAX_SUB_TAB
///@brief Nombre maximum de sous-commandes pouvant être récupérées.
#define NB_MAX_SUB_TAB 31
///@def MAX_SIZE_SIGNAL
///@brief Taille maximale du signal
#define MAX_SIZE_SIGNAL 
///@brief Déclaration des servomoteurs
///@var servoIndex
///@brief Servo pour relié à l'index de la main robotique.
Servo servoIndex;
///@var servoThumb
///@brief Servo pour relié au pouce de la main robotique.
Servo servoThumb;
///@var servoPinky
///@brief Servo pour relié à l'auriculaire de la main robotique. 
Servo servoPinky;
///@var servoRing
///@brief Servo pour relié à l'annulaire de la main robotique.
Servo servoRing;
///@var servoMiddleFinger
///@brief Servo pour relié au majeur de la main robotique.
Servo servoMiddleFinger;
///@var servoWrist
///@brief Servo pour relié au poignet de la main robotique.
Servo servoWrist;
///@var message
///@brief Message reçu par @ref ServoMediator via le port série.
String message;
///@var __heap_start
///@brief Adresse de début de la mémoire dynamique
extern int __heap_start
///@var *__brkval
///@brief Adresse de fin de la mémoire dynamique
extern int *__brkval;
///@struct finger
///@brief Structure représentant un doigt de la main robotique.
///@details Elle contient un servomoteur et le nom du doigt.
typedef struct finger{
  Servo servofinger;
  String name;
} FINGER;
///@struct hand
///@brief Structure représentant la main robotique. 
///@details Elle contient un tableau de 5 doigts et un servomoteur pour le poignet.
typedef struct hand{
  FINGER FINGERS[5];
  Servo servoWrist;
} HAND ;
/// @var hand
/// @brief Instance de la structure hand
HAND hand ;
/// @struct signal
/// @brief Structure représentant le signal reçu.
/// @details Elle contient un tableau de positions. Il s'agit d'un tableau JsonArray.
///@see https://arduinojson.org/v6/doc/array/
typedef struct signal{
 JsonArray positions_buffer;
}SIGNAL;

/// @var S
/// @brief Instance de la structure signal
SIGNAL S;
///@var answer
/// @brief Instance de la structure JsonDocument.
///@details Elle contient le signal à envoyer à la plateforme. La structure est de type StaticJsonDocument<256> afin de ne pas dépasser la taille maximale de 256 octets. Cette taille est suffisante pour contenir le nombre maximal de sous-commandes.@ref NB_MAX_SUB_TAB
StaticJsonDocument<256> answer;
///@var sub_answer_pos
///@brief Instance de la structure JsonArray.
///@details Elle contient le tableau de positions à envoyer comme réponse à @ref ServoMediator. La structure est de type JsonArray afin de pouvoir ajouter des sous-commandes.
JsonArray sub_answer_pos;

void setup() {
  ///@param None
  ///@brief Initialisation de la communication série
  ///@details La vitesse de communication est de 9600 bauds.
  ///@see https://www.arduino.cc/reference/en/libraries/serial
  ///@see https://www.arduino.cc/reference/en/libraries/serial-begin/
  ///@return void
  Serial.begin(9600);
  for(int i = 2; i< 8; i++){
    //Initialisation des LED
    pinMode(i,OUTPUT);
    //Initialisation des servomteurs
    pinMode(i+5,OUTPUT);
  }
  //On éteind les LEDs
  shut_down_LEDs();
  
  ///@brief Initialisation des variables que l'on va envoyer à la plateforme
  ///@details positions est un tableau JsonArray qui contient les positions des doigts et du poignet. state est une chaîne de caractères qui contient l'état de la main. info est une chaîne de caractères qui contient des informations sur la main.
  ///@see https://arduinojson.org/v6/doc/array/
  answer["positions"] = JsonArray();
  answer["state"]="";
  answer["info"]="";
  ///@brief Initialisation de la main et de ses doigts 
  hand.FINGERS[0].servofinger = servoThumb;
  hand.FINGERS[0].name = "Pouce";
  hand.FINGERS[0].servofinger.attach(8);
  hand.FINGERS[1].servofinger = servoIndex;
  hand.FINGERS[1].name = "Index";
  hand.FINGERS[1].servofinger.attach(9);
  hand.FINGERS[2].servofinger = servoMiddleFinger;
  hand.FINGERS[2].name = "Majeur";
  hand.FINGERS[2].servofinger.attach(10);
  hand.FINGERS[3].servofinger = servoRing;
  hand.FINGERS[3].name = "Auriculaire";
  hand.FINGERS[3].servofinger.attach(11);
  hand.FINGERS[4].servofinger = servoPinky;
  hand.FINGERS[4].name = "Annulaire";
  hand.FINGERS[4].servofinger.attach(12);
  hand.servoWrist= servoWrist;
  hand.servoWrist.attach(13);

} 
void loop() {
  ///@param None
  ///@brief Boucle principale du programme
  ///@details Elle attend un message de la plateforme et le traite. Si le message est valide, il est traité et la main est déplacée. Sinon, un message d'erreur est envoyé à la plateforme.
  ///@see https://www.arduino.cc/reference/en/libraries/serial-readstringuntil/
  ///@see https://www.arduino.cc/reference/en/libraries/serial-readstringuntil/
  ///@return void
        // Lecture des données depuis le flux Serial
        // where_am_i("SRAM (Avant la récupération des données):" + String(available_memory())+"o"); :: POUR DEBUG 
        message = Serial.readStringUntil('\n');
        if(message.length()>0){
          // Si un message est bien reçu
              // where_am_i("SRAM (Après la récupération des données): " + String(available_memory())+"o"); : : POUR DEBUG
              // whereAmI("Avant concat "+message);
              treat_signal(message,S);
        }
        else{
           //On étéint les LEDs
          shut_down_LEDs();   
          // where_am_i("Aucun message n'a été détecté"); : POUR DEBUG
        }
}
bool contain_key(JsonDocument doc){
  ///@brief Vérifie si le signal reçu contient les clés "positions" et "state".
  ///@param doc Le signal reçu sous forme de JsonDocument.
  ///@return bool. true si les clés sont présentes et que la taille des positions est inférieur à @ref NB_MAX_SUB_TAB, false sinon.
 
  if(!doc["positions"].is<JsonArray>()){
    where_am_i("Les clés ne sont pas trouvés dans le signal.");
    return false;
  }
  else if(doc["positions"].size() > NB_MAX_SUB_TAB){
    where_am_i("La taille des listes des degrés en entrée est invalide. 31 positions maximales peuvent êtres entrés.");
    return false;
  }
  // where_am_i("Les clés sont trouvés dans le signal. Le format de votre commande est reconnu."); : : POUR DEBUG
  return true;
}

void treat_signal(String m,SIGNAL  S){
  ///@brief Traite le signal reçu et l'interprète.
  ///@param m Le signal reçu sous forme de chaîne de caractères.
  ///@param S Le signal reçu sous forme de structure SIGNAL.
  ///@return void
  ///@see https://arduinojson.org/v6/doc/array/
          JsonDocument doc;
          DeserializationError error_deserialization = deserializeJson(doc, m);
          
            if (error_deserialization) {
                where_am_i("Erreur lors de la désérialisation dans treatSignal");
                error();
                return;
              }
              if(!contain_key(doc)){
                where_am_i("Erreur lors de la vérification du clé JSON");
                error();
                return;
              }       
              // Récupère le nombre de tableau
             S.positions_buffer = doc["positions"];
           execute_command(&S); 
}

void move_finger_to_position(int idFinger, float deg){
  ///@brief Déplace le doigt à la position spécifiée.
  ///@param idFinger L'identifiant du doigt à déplacer.
  ///@param deg La position à atteindre.
  ///@return void
  if(deg==-1){
    where_am_i(String(hand.FINGERS[idFinger-1].name)+" n'a pas bougé.");
    digitalWrite(idFinger+1, LOW);// Les LED sont connectés aux pin 2 à 7.
    return ;
  } 
  hand.FINGERS[idFinger].servofinger.write(deg);
  where_am_i(hand.FINGERS[idFinger-1].name+" a bougé. Son degré est égal à "+String(deg));
  digitalWrite(idFinger+1, HIGH);// Les LED sont connectés aux pin 2 à 7.
 
}
void move_wrist_to_position(float deg){
  ///@brief Déplace le poignet à la position spécifiée.
  ///@param deg La position à atteindre.
  ///@return void
  if(deg==-1){
    where_am_i("Le poignet n'a pas bougé.");
    digitalWrite(7, LOW);// Les LED sont connectés aux pin 2 à 7.
    return ;
  } 
  hand.servoWrist.write(deg);
  where_am_i("Le poignet a bougé. Son degré est égal à "+String(deg));
  digitalWrite(7, HIGH);// Les LED sont connectés aux pin 2 à 7.
}


///@deprecated Version dépréciée de la fonction execute_command. Elle exécute les positions des doigts et pas celle du poignet. Cette fonction n'est pas adaptée pour exécuter des positions composées.
 void executeCommand_deprecated(SIGNAL * s){
///@brief lle exécute les positions des doigts et pas celle du poignet. 
  ///@param s Le signal reçu sous forme d'un pointeur de la structure SIGNAL.
  ///@return void

    for(JsonArray sub_tab_pos : s->positions_buffer){
      whereAmI("Execution de sous-positions"+String(sub_tab_pos));
      moveFingerToPosition(0, sub_tab_pos[0]);
      moveFingerToPosition(1, sub_tab_pos[1]);
      moveFingerToPosition(2, sub_tab_pos[2]);
      moveFingerToPosition(3, sub_tab_pos[3]);
       moveFingerToPosition(4, sub_tab_pos[4]);
      
     }


     success();
 }

void execute_command(SIGNAL *s) {
  ///@brief Exécute les positions des doigts et du poignet.
  ///@details Cette fonction exécute les positions des doigts et du poignet. Elle est adaptée pour exécuter des positions composées.
  ///@param s Le signal reçu sous forme d'un pointeur de la structure SIGNAL.
  ///@return void
  ///@see https://arduinojson.org/v6/doc/array/
    for (size_t i = 0; i < s->positions_buffer.size(); i++) {
        JsonArray sub_tab_pos = s->positions_buffer[i].as<JsonArray>();
        if (!sub_tab_pos.isNull() && sub_tab_pos.size() == 6) {
            move_finger_to_position(1, sub_tab_pos[0]);
            move_finger_to_position(2, sub_tab_pos[1]);
            move_finger_to_position(3, sub_tab_pos[2]);
            move_finger_to_position(4, sub_tab_pos[3]);
            move_finger_to_position(5, sub_tab_pos[4]);
            move_wrist_to_position(sub_tab_pos[5]);
            // On éteint les LEDs
            shut_down_LEDs();
        } else {
            where_am_i("WARNING : sous-tableau invalide ou incomplet.");
        }
    }
    update_current_position(s);
    success();
}
void error() {
  ///@param None
  ///@brief Renvoie un signal d'erreur à la plateforme
  ///@details Cette fonction renvoie un signal d'erreur à la plateforme. Elle est appelée lorsque le signal reçu est invalide ou que la désérialisation échoue. Puis elle réinitialise les variables nécessaires sans redémarrer la carte.
  ///@return void
  answer["state"] = "-1\n";
  serializeJson(answer, Serial);
  delay(100);
  // Réinitialisation des variables nécessaires sans redémarrage
  shut_down_LEDs();
  answer["positions"] = JsonArray(); // Réinitialise les positions
  answer["state"] = "";
  answer["info"] = "";
  message="";
}

void success() {
  ///@param None
  ///@brief Renvoie un signal pour signaler une bonne exécution du mouvement.
  ///@details Cette fonction renvoie un signal pour signaler une bonne exécution du mouvement. Elle est appelée lorsque le mouvement est exécuté avec succès. Puis elle réinitialise les variables nécessaires sans redémarrer la carte.
  ///@return void
  answer["state"] = "0\n";
  shut_down_LEDs();
  serializeJson(answer, Serial);
  delay(100);
  // Réinitialisation des variables nécessaires sans redémarrage
  answer["positions"] = JsonArray(); // Réinitialise les positions
  answer["state"] = "";
  answer["info"] = "";
  message = "";
}
void where_am_i(String e){
  ///@brief Envoie un message de débogage à la plateforme.
  ///@details Cette fonction envoie un message de débogage à la plateforme. Elle est appelée pour afficher des messages de débogage.
  ///@param e Le message à envoyer.
  ///@return void
   answer["info"] = e;
   serializeJson(answer,Serial);
}
int available_memory() {
  ///@param None
  ///@brief Renvoie la mémoire disponible sur la carte.
  ///@details Cette fonction renvoie la mémoire disponible sur la carte. Elle est utilisée pour afficher la mémoire disponible avant et après la récupération des données.
  ///@return int La mémoire disponible en octets.
  int v;
  return (int)&v - (__brkval == 0 ? (int)&__heap_start : (int)__brkval);
}
void update_current_position(SIGNAL *s){
  ///@brief Met à jour la position actuelle des doigts et du poignet.
  ///@details Cette fonction met à jour la position actuelle des doigts et du poignet. Elle est appelée après l'exécution du mouvement.
  ///@param s Le signal reçu sous forme d'un pointeur de la structure SIGNAL.
  ///@return void
  for(size_t i = 0; i<s->positions_buffer.size();i++){
    answer["positions"].add(s->positions_buffer[i]);
  }
}

void shut_down_LEDs(){
  ///@param None
  ///@brief Eteint les LEDs.
  ///@details Cette fonction éteint les LEDs. Elle est appelée lorsque le mouvement est exécuté avec succès ou lorsque le signal reçu est invalide.
  ///@return void
  ///@see https://www.arduino.cc/reference/en/libraries/digitalwrite/
  for(int i =2; i<8;i++){
    digitalWrite(i,LOW);
  }
}