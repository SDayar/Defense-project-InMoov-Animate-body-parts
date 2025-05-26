# <span style="color:#1976D2">L2L1 Robotic Hand Control Platform</span>

---


## <span style="color:#1976D2">Project Overview</span>

The **L2L1 project** is a sophisticated software and hardware platform for controlling a robotic hand through a Python-based graphical interface. It supports multiple interaction modes—voice commands, educational games, and custom finger movements—while ensuring robust communication with an Arduino microcontroller that actuates the hand’s servomotors.

The platform is designed for educational, research, and demonstration purposes, providing a modular and extensible foundation for human-robot interaction.

---

## <span style="color:#1976D2">Objectives</span>

- <span style="color:#388E3C">**Educational Engagement:**</span> Provide interactive games and activities to teach binary counting, sign language, and classic games like Rock-Paper-Scissors using the robotic hand.
- <span style="color:#388E3C">**Accessibility:**</span> Enable intuitive control via both graphical and voice interfaces, making the system approachable for users of varying technical backgrounds.
- <span style="color:#388E3C">**Customization:**</span> Allow users to define and execute personalized hand gestures, supporting experimentation and creative applications.
- <span style="color:#388E3C">**Robust Communication:**</span> Ensure reliable, asynchronous communication between the Python application and the Arduino hardware, with clear feedback and error handling.

---

## <span style="color:#1976D2">Technical Architecture</span>

### <span style="color:#FBC02D">1. Graphical User Interface (GUI)</span>

- **Frameworks:** `customtkinter`, `tkinter`, `PIL.Image`
- **Structure:** Modular GUI with distinct frames for each major function (main menu, games, voice control, custom movements).
- **Navigation:** Managed by the `Mediator` class, orchestrating transitions and maintaining application state.
- **Visual Feedback:** Uses icons, color cues, and status bars to inform the user of system state and errors.

### <span style="color:#FBC02D">2. Voice Command Module</span>

- **Library:** `speech_recognition`
- **Functionality:** Users issue natural language commands to control the hand or launch games. The system provides real-time feedback and error handling.
- **Integration:** Voice commands are parsed and translated into movement instructions or navigation actions.
- **Error Handling:** Notifies the user if speech is not recognized or if a command is invalid.

### <span style="color:#FBC02D">3. Interactive Games</span>

- **Location:** `/Game/` directory
- **Implemented Games:**
  - <span style="color:#1976D2">**Rock-Paper-Scissors (`GamePPC.py`):**</span> The robotic hand plays against the user, with random or user-selected gestures. The game logic ensures fair play and provides visual feedback on the outcome.
  - <span style="color:#1976D2">**Binary Counting (`CountBinary.py`):**</span> The hand displays numbers in binary using finger positions, reinforcing binary concepts visually and interactively.
  - <span style="color:#1976D2">**Sign Language (`SignLanguage.py`):**</span> The hand spells out words or phrases in sign language, supporting educational and accessibility goals.

### <span style="color:#FBC02D">4. Custom Movement Module</span>

- **File:** `PersonalizedMovement.py`
- **Purpose:** Users manually specify finger positions to create and execute custom gestures. The interface allows saving, editing, and replaying custom movements.

### <span style="color:#FBC02D">5. Movement Abstraction</span>

- **File:** `Movement.py`
- **Role:** Centralizes logic for generating and validating movement commands, ensuring consistency across all input methods. Handles edge cases and prevents invalid or unsafe movements.

### <span style="color:#FBC02D">6. Arduino Communication Layer</span>

- **File:** `ServoMediator.py`
- **Mechanism:** File-based communication (`send_command.txt`, `executed_command.txt`) and multi-threading for asynchronous command exchange.
- **Error Handling:** Provides user feedback on connection status and command execution. Detects and reports communication failures or hardware issues.

### <span style="color:#FBC02D">7. Arduino Firmware</span>

- **File:** `ServoMotor.ino`
- **Function:** Receives JSON-formatted commands, interprets them, and actuates servomotors accordingly.
- **Libraries:** Uses `ArduinoJson` and `Servo.h`.
- **Safety:** Includes checks to prevent servo overextension and ensures smooth transitions between gestures.

---

## <span style="color:#1976D2">Key Features</span>

- <span style="color:#388E3C">**Multi-modal Control:**</span> Seamless switching between GUI, voice, and game-based control.
- <span style="color:#388E3C">**Educational Tools:**</span> Interactive modules for learning binary, sign language, and logic games.
- <span style="color:#388E3C">**User Feedback:**</span> Real-time status updates, error messages, and visual cues.
- <span style="color:#388E3C">**Extensibility:**</span> Modular codebase for easy addition of new features, games, or gesture libraries.
- <span style="color:#388E3C">**Threaded Communication:**</span> Responsive GUI during hardware interactions.
- <span style="color:#388E3C">**Cross-platform Support:**</span> Designed to run on Windows and Linux (Debian-based) systems.

---

## <span style="color:#1976D2">File Organization</span>

```
/__internal/
│
├── Main.py
├── Mediator.py
├── CommandeVocale.py
├── PersonalizedMovement.py
├── Movement.py
├── ServoMediator.py
├── /Game/
│   ├── CountBinary.py
│   ├── GamePPC.py
│   └── SignLanguage.py
├── /images/
│   └── [GUI assets]
├── /commands/
│   ├── send_command.txt
│   └── executed_command.txt
└── /ServoMotor/
    └── ServoMotor.ino
```

---

## <span style="color:#1976D2">Technologies Used</span>

- **Python 3** (core application)
- **Tkinter / CustomTkinter** (GUI)
- **Pillow (PIL)** (image handling)
- **speech_recognition** (voice input)
- **Arduino (C++)** (hardware control)
- **ArduinoJson** (command parsing)
- **Threading** (asynchronous operations)
- **Serial Communication** (PC ↔ Arduino)

---

## <span style="color:#1976D2">Disclaimer</span>

<span style="color:#D32F2F; font-weight:bold;">
⚠️ If you are running this project on a Debian-based Linux distribution, you may need to enable access to your serial (development) port for Arduino communication.  
To do so, execute the following command in your terminal (replace <code>$USER</code> with your actual username):
</span>

```bash
sudo usermod -aG dialout $USER
```

<span style="color:#D32F2F; font-weight:bold;">
You must log out and log back in for the changes to take effect.  
Failure to do this may result in permission errors when attempting to communicate with the Arduino.
</span>

---

## <span style="color:#1976D2">Conclusion</span>

The **L2L1 project** demonstrates a comprehensive, modular, and extensible approach to human-robot interaction. By combining advanced software design with robust hardware integration, it serves as both an educational tool and a platform for experimentation in robotics, accessibility, and user interface design. The architecture supports future enhancements, such as additional games, gesture libraries, or alternative input modalities, making it a valuable foundation for ongoing research and development in interactive robotics.

---

