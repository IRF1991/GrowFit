# GrowFit

**Smart fitness app that grows with you - AI-powered workout recommendations and adaptive progression tracking**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Flutter](https://img.shields.io/badge/Flutter-UI%20Framework-blue.svg)](https://flutter.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)](https://fastapi.tiangolo.com)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)](https://github.com)

## Vision

GrowFit is your personal training companion that grows with you. More than a fitness tracker, it's an intelligent assistant that learns from your performance and guides your progression journey with adaptive recommendations.

The app combines data analytics and machine learning to act as your gym buddy - tracking your workouts, recognizing when you're ready for the next challenge, and motivating you to push your limits at your own pace.

### Core Philosophy

**Progressive Overload Made Smart**: Instead of generic workout plans, GrowFit analyzes YOUR performance patterns and recommends the next difficulty step when you're consistently ready for it.

**Example**: Master knee push-ups for 3 sessions? GrowFit suggests moving to full push-ups. Crushing diamond push-ups? Time for archer variations. The system adapts to your unique progression speed.

### Key Features (Planned)

- **Adaptive Progression System**: Exercise difficulty progressions (1-10 scale) with prerequisite tracking
- **Performance-Based Recommendations**: ML model analyzes your consistency and suggests next-level exercises when you're ready
- **Motivation & Gamification**: Unlock achievements, track streaks, celebrate milestones
- **Exercise Progression Database**: Curated exercise chains from beginner to advanced (e.g., Push-up variations, L-Sit progressions, etc.)
- **Smart Analytics**: Track not just what you did, but how you're improving over time
- **Cross-Platform**: Mobile-first approach using Python (backend) and Flutter (frontend)

## Architecture (2025+)

GrowFit is divided into two independent parts:

- **Backend**: Python + FastAPI
  - Exposes a REST API for all logic, data management, and ML models.
  - Accesses data (CSV, models, etc.) and exposes endpoints for the app.
  - Runs locally for development or in the cloud for production.

- **Frontend**: Flutter (Dart)
  - Modern, cross-platform UI (Android/iOS).
  - Only consumes the backend REST API, never accesses data or internal logic directly.
  - Base URL configuration in `lib/config.dart`.

## Data Management and Synchronization

Data management is at the core of GrowFit's architecture. The backend leverages pandas for robust, efficient, and scalable data handling, while the API ensures seamless communication with the frontend. This approach is designed for clarity, maintainability, and future extensibility—key aspects for any data science portfolio project.

- Each data model (user, session, routine, etc.) has its own file in `models/` (e.g., `user.py`, `session.py`).
- Each model handles its own data flow:
  - Receives data in JSON format from Flutter via the REST API.
  - Converts JSON to pandas DataFrame, validates, cleans, and saves/updates the corresponding CSV file.
  - Reads data from CSV with pandas, processes as needed, and exports to JSON for the REST API.
- All validation, cleaning, and persistence logic is centralized in the backend using pandas and CSV files.
- Data exchange between Flutter and the backend is always in JSON (API REST standard), while internal storage and processing is in CSV.
- This design keeps the code modular, maintainable, and ready for future migrations or enhancements.

## Deployment and Development

### Prerequisites
- Python 3.8+
- pip
- Flutter 3.x+
- (Optional) Android Studio/Emulator

### Backend (FastAPI)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the backend:
   ```bash
   uvicorn growfit.main:app --reload
   ```
3. Access the interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs)

### Frontend (Flutter)
1. Enter the folder:
   ```bash
   cd growfit_flutter
   ```
2. Install dependencies:
   ```bash
   flutter pub get
   ```
3. Set the base URL in `lib/config.dart` according to your environment:
   - Android emulator: `http://10.0.2.2:8000/api/v1/data`
   - Physical device: `http://<PC_IP>:8000/api/v1/data`
   - Production: `https://api.yourapp.com/api/v1/data`
4. Run the app:
   ```bash
   flutter run
   ```

## Project Structure

```
GrowFit/
├── growfit/                # Backend (FastAPI, logic, data)
│   ├── main.py             # FastAPI app entrypoint
│   ├── api/                # REST endpoints
│   ├── core/               # Logic and utilities
│   ├── models/             # Data models
│   └── ...
├── growfit_flutter/        # Frontend (Flutter UI)
│   ├── lib/
│   │   ├── screens/        # Screens
│   │   ├── services/       # Services to consume the API
│   │   └── config.dart     # Base URL configuration
├── data/                   # Data (CSV, ML models, etc.)
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Important notes
- The Flutter app never accesses backend data or logic directly.
- All communication is via the REST API.
- For offline mode, logic and data must be migrated to Flutter (see internal docs).

### Device identification system (`device_id`)

GrowFit uses a unique device identifier (`device_id`) to associate local data and synchronize it with the backend. The behavior is as follows:

- When the backend starts, if the file `data/device_id.txt` does not exist, the console will prompt whether the environment is for testing:
  - If you answer `y` or `Y`, a `device_id` with the prefix `te_` (testing) is generated.
  - If you answer anything else (or just press Enter), a `device_id` with the prefix `us_` (end user) is generated.
- The `device_id` is saved in `data/device_id.txt` and reused in future sessions.
- If you do not answer in the console and perform an action from the UI (e.g., create a new routine), a `device_id` with the prefix `us_` is generated automatically.
- The system guarantees that a valid `device_id` always exists, even after migrations or accidental file deletions.
- The `/device_id` endpoint of the REST API exposes the current identifier for frontend queries.

This mechanism is fundamental for data management and synchronization between devices, without requiring user authentication.

## Technology
- **Backend**: Python 3.8+, FastAPI, Pandas, ML (future)
- **Frontend**: Flutter (Dart)
- **Data**: CSV, ML models

## Operation and Philosophy

GrowFit is an intelligent training app that adapts exercise progression to your pace, using data analytics and personalized recommendations. See the internal documentation and code comments for details on progression logic, routine management, and general operation.

