# Behavioral Biometrics in Game Security: Detecting Automated Cheat Clients in Minecraft via Keystroke and Mouse Dynamics

**Student Name:** Kpughur-Tule Tertsegha Moses & Timothy
**Course:** COMP 4980: Behavioral Biometrics  
**Institution:** Thompson Rivers University  
**Date:** March 18th, 2026

---

## 1. Project Overview
This project explores the application of **Behavioral Biometrics**—specifically Keystroke Dynamics (KSD) and Mouse Dynamics (MD)—to enhance game security and anti-cheat systems within the Minecraft environment. Traditional anti-cheat mechanisms often rely on signature-based detection or server-side heuristics that are easily bypassed by sophisticated clients. This research proposes a continuous, non-intrusive authentication layer that identifies the unique "digital gait" of a human player versus an automated or assisted cheat client (e.g., Killaura, Aimbots, and Macros).

### The Objective
To develop a high-performance system capable of:
1.  **Logging** raw mouse and keyboard events with microsecond precision.
2.  **Extracting** features such as Dwell Time (key hold duration), Flight Time (latency between keys), and Mouse Curvature/Acceleration.
3.  **Classifying** behaviors using machine learning models to detect anomalies that signify artificial assistance.

---

## 2. Methodology

### 2.1 Data Collection
Data is collected in real-time while the user is playing. The system uses two primary modules:
-   **`keylogging.py`**: Records `KeyboardEvent` timestamps for every press and release.
-   **`mouselogging.py`**: Captures mouse movement coordinates (X, Y) and click events (Left, Right).

The logger is designed to be lightweight and modular, ensuring it does not impact game performance (FPS).

### 2.2 Feature Engineering
The raw events are processed to extract high-level biometric features:
-   **Keystroke Dynamics**:
    -   **Dwell Time**: Duration a key is held (`T_up - T_down`).
    -   **Flight Time**: Interval between consecutive keystrokes (e.g., moving between 'W' and 'D').
-   **Mouse Dynamics**:
    -   **Angular Velocity**: Consistency of aim turns.
    -   **Path Curvature**: Human-like arcs vs. linear/robotic aimbot paths.
    -   **Clicks Per Second (CPS)**: Regularity analysis to detect auto-clickers.

### 2.3 Machine Learning Classification
The project implements non-parametric classifiers (e.g., Nearest Neighbor, Distance-to-Median) to handle the limited yet highly idiosyncratic nature of individual player data. The model learns a "profile" of a legitimate player and flags deviations as potential security exceptions.

---

## 3. Technical Implementation & Performance

### 3.1 Python 3.14t (Free-Threading)
To ensure the system can handle high-frequency data collection (up to 1,000 polls per second for mouse movement) without causing game stuttering, the project utilizes **Python 3.14t (Free-threading experimental version)**. 

-   **Parallelism**: This version removes the Global Interpreter Lock (GIL), allowing the logger and the ML model to run on separate threads with true parallelism.
-   **Efficiency**: Experimental builds of 3.14t show significant performance gains in real-time data processing tasks on multi-core consumer machines.

---

## 4. Installation and Setup

### 4.1 Prerequisites
1.  Install Python 3.14t (experimental build) via the official terminal command:
    ```bash
    py install 3.14t
    ```
2.  **Interpreter Configuration**:
    -   Open your IDE (PyCharm or VS Code).
    -   Manually set the local interpreter path to:
        `C:\Users\<YourUser>\AppData\Local\Python\pythoncore-3.14t-64\python3.14t.exe`
    -   *Note: Verify the path in File Explorer as installation folders may vary.*

### 4.2 Dependencies
Install the required libraries:
```bash
pip install keyboard mouse pandas scikit-learn
```

---

## 5. Development Roadmap (Phases)
-   **Phase I (Data Preparation)**: Ingestion of secondary datasets and implementation of recursive outlier removal.
-   **Phase II (Feature Engineering)**: Extraction of Dwell Time, Flight Time, and Haptic features.
-   **Phase III (Model Development)**: Implementing non-parametric classifiers and sliding window algorithms for continuous monitoring.
-   **Phase IV (Robustness Testing)**: Evaluating the model against common Minecraft hack clients (e.g. Meteor, Wurst).
-   **Phase V (Final Synthesis)**: Development of a real-time alerting system and BioAPI compliance.

---

## 6. Project Files
| File | Description |
| :--- | :--- |
| `main.py` | Entry point for the real-time detection system. |
| `keylogging.py` | Modular keyboard event capture and CSV generation. |
| `mouselogging.py` | Mouse movement and click frequency tracking. |
| `model.py` | Machine learning model implementation (classification). |
| `preprocessor.py` | Data normalization and feature extraction logic. |

---

## References
1.  **Teh et al. (2016)**: Statistical Keystroke Dynamics System on Mobile Devices.
2.  **Veriff (2025)**: Last-mile delivery: Why identity verification is your secret weapon.
3.  **Tsumperidis et al. (2024)**: IKDD Keystroke Dataset: A benchmark for keystroke dynamics.