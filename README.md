# Defense-project-InMoov-Animate-body-parts
Le projet vise à fournir une interface graphique pour contrôler les fonctionnalités robotiques, telles que les mouvements des mains, les jeux et les commandes vocales. 
Il intègre le matériel (Arduino) avec le logiciel pour créer une expérience interactive.
## Caractéristiques principales
### Gestion des fenêtres et navigation 
L’application utilise une classe Mediator pour gérer plusieurs fenêtres (frames) et leurs transitions :
<ul>
  <li>Welcome Frame : Écran d’accueil.</li>
  <li>Main Frame : Hub central pour ouvrir/fermer la main, arrêter les mouvements ou accéder aux jeux.</li>
  <li>Games Frame : Accès à des jeux interactifs (Pierre-Papier-Ciseaux, compter en binaire, langue des signes...).</li>
  <li>PPC Frame : Jeu Pierre-Papier-Ciseaux.</li>
  <li>Voice Command Frame : Contrôle vocal et mouvements personnalisés.</li>
</ul>

### Hardware et Arduino

<ul>
  <li>Carte utilisée : Arduino Uno R3, basée sur le microcontrôleur ATmega328P.</li>
  <li>Connexion : Liaison série USB (détection automatique du port, gestion multi-plateforme).</li>
  <li>Contrôle matériel : 6 servomoteurs (5 doigts + 1 poignet), chaque mouvement est transmis sous forme de liste de positions (degrés).</li>
  <li>Firmware : Le code Arduino (ServoMotor.ino) reçoit les commandes JSON, contrôle les servos, et renvoie l’état d’exécution.</li>
  <li>Timeout : Un délai d’attente (timeout, typiquement 2 à 5 secondes) est utilisé lors de la communication série pour éviter les blocages si la carte ne répond pas.</li>
</ul>

### Transfert de signaux et gestions des erreurs

<ol>
  <li>Transfert : Les mouvements sont envoyés sous forme de messages JSON via la liaison série. Chaque commande contient les positions des doigts et du poignet.</li>
  <li>Timeout : Si la carte Arduino ne répond pas dans le délai imparti, l’application affiche un message d’erreur et interrompt la tentative.</li>
  <li>Synchronisation : L’état de la connexion Arduino est affiché en temps réel sur l’interface graphique (bandeau vert/rouge).</li>
  <li>Robustesse : Utilisation de threads et de sémaphores pour éviter les blocages lors de la connexion ou de l’envoi de commandes.</li>
</ol>

### Messages affichés à l'utilisateur

L’application affiche différents messages pour informer l’utilisateur de l’état du système ou des erreurs rencontrées :
<ul>
  <li>Carte connectée : « Carte connectée. » (bandeau vert)</li>
  <li>Carte non connectée : « Carte non connectée. » (bandeau rouge)</li>
  <li>Erreur de port série : « Connexion avec la carte Arduino : [détail de l’erreur] »</li>
  <li>Erreur de mouvement : « Erreur au niveau de Movement : [détail] »</li>
  <li>Erreur de frame : « Erreur lors de l’exécution : [détail] »</li>
  <li>Timeout de communication : « Tâche non exécutée. Le temps d’attente d’exécution du mouvement a été dépassé ! »</li>
  <li>Aucune fenêtre précédente : « Désolé ! Aucune fenêtre ne précède celle-là. »</li>
  <li>Erreur de saisie : Messages spécifiques lors d’une saisie invalide (ex : angle hors limites, valeur non numérique, etc.)</li>
  <li>Informations sur les mouvements : Une boîte de dialogue affiche le bilan du dernier mouvement (succès, positions, infos de debug).</li>
</ul>

### Interface graphique personnalisable
<ol>
  <li>Technologie : CustomTkinter pour une interface moderne et responsive.</li>
  <li>Composants : Boutons, labels, frames, boîtes de dialogue, images, etc.</li>
  <li>Mise à jour dynamique : L’état de la connexion Arduino et les retours d’exécution sont mis à jour en temps réel.</li>
</ol>



