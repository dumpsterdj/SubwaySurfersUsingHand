# 🕹️ Hand Gesture Game Controller 🎮✋

Control any web-based or keyboard-driven game (like **Subway Surfers Classic**) using only your hand gestures and a webcam — no physical keyboard needed!

This project uses **MediaPipe** to detect hand landmarks and **pyautogui** to simulate arrow key presses based on your hand’s motion.

---

## 📸 Demo

https://www.brightestgames.com/game/subway-surfers-classic  
Use your hand to **jump, duck, or move left/right** as if you're playing with arrow keys!

---

## 🧩 Features

- ✋ Recognizes basic hand motions (up/down/left/right)
- 🎮 Simulates keyboard arrow key presses (`↑ ↓ ← →`)
- 🕵️‍♂️ Cooldown system to avoid accidental double actions
- 👥 Built using **OpenCV**, **MediaPipe**, and **pyautogui**

---

## 🔧 Requirements

Make sure you have Python 3.7+ installed, then run:

```bash
pip install opencv-python mediapipe pyautogui
````

## 🚀 Getting Started

1. **Clone or download this repo**

2. ```bash
   git clone https://github.com/dumpsterdj/SubwaySurfersUsingHand.git
  

3. Save the script as `gesture_game_control.py`

4. Open the command line and run:

   ```bash
   python gesture_game_control.py
   ```

5. Launch the game in your browser:
   [https://www.brightestgames.com/game/subway-surfers-classic](https://www.brightestgames.com/game/subway-surfers-classic)

6. Make sure to **click on the game** so it can receive key inputs.

---

## ✋ Gesture Controls

| Hand Motion         | Keyboard Press | Game Action |
| ------------------- | -------------- | ----------- |
| Move hand **up**    | `Up Arrow`     | Jump        |
| Move hand **down**  | `Down Arrow`   | Duck        |
| Move hand **left**  | `Left Arrow`   | Move Left   |
| Move hand **right** | `Right Arrow`  | Move Right  |

> ✅ Requires good lighting and a visible index finger.

---

## 🧠 Tips

* Adjust the `threshold` in the script to fine-tune gesture sensitivity.
* Adjust the `cooldown` (in seconds) to avoid accidental repeated inputs.
* Make sure your webcam is not mirrored (flip applied inside script).

---

## 📁 Files

| File Name                 | Description                              |
| ------------------------- | ---------------------------------------- |
| `gesture_game_control.py` | Main gesture recognition + control logic |
| `README.md`               | Project guide and setup instructions     |

---

## ✅ TODO / Enhancements

* [ ] Detect custom hand poses (e.g., fist = duck)
* [ ] Add on-screen gesture preview
* [ ] Add gesture calibration wizard
* [ ] Support multi-hand controls

---

## 📜 License

This project is open-sourced under the MIT License. Feel free to modify and distribute with attribution.

---
