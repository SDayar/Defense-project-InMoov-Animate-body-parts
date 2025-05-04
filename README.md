# Defense-project-InMoov-Animate-body-parts
The project aims to provide a graphical interface for controlling robotic functionalities, such as hand movements, games, and voice commands. It integrates hardware (Arduino) with software to create an interactive experience.
## Key futures
### Frame Management
The application uses a Mediator class to manage multiple frames (windows) and their transitions.
  #### Frame include : 
  <ol>
<li>Welcome Frame: The starting screen of the application.</li>
<li>Main Frame: Central hub for accessing functionalities.</li>
<li>Games Frame: Includes games like Rock-Paper-Scissors and binary counting.</li>
<li>PPC Frame: Dedicated to Rock-Paper-Scissors.</li>
<li>Voice Command Frame: For voice-based interactions or other personalized movements.</li>
  </ol>
  
  #### Arduino Integration:
  The application interacts with an Arduino board to control hardware components.
  Real-time status updates of the Arduino board are displayed on the GUI
  #### Customizable GUI:
  Built using customtkinter for a modern and     customizable interface.
Includes buttons, labels, and frames with custom fonts, colors, and styles.
#### Error Handling : 
The Mediator class handles errors during frame transitions and displays error messages using tkinter.messagebox.
## Materials and Libraries Used:


