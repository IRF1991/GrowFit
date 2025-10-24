# GrowFit

**Smart fitness app that grows with you - AI-powered workout recommendations and adaptive progression tracking**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Kivy](https://img.shields.io/badge/Kivy-UI%20Framework-orange.svg)](https://kivy.org)
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
- **Cross-Platform**: Built with mobile-first approach using Python and Kivy

## Current Status

### Completed
- Core counter functionality for reps/sets/time tracking
- Multi-screen navigation system (Kivy-based)
- Data management system with CSV-based storage
- User/Testing mode distinction for data integrity
- Device identification system for user tracking

### In Development
- Exercise progression database with difficulty levels and prerequisites
- Performance tracking for progression triggers
- Timer functionality for rest periods and hold exercises
- Routine creation and management system

### Planned Features
- ML recommendation engine for progression suggestions
- Motivation system (streaks, achievements, milestones)
- Progress visualization and analytics dashboard (Power BI integration)
- Exercise tutorial/demo system for new progressions
- Community-driven exercise database expansion

## Technology Stack

- **Backend**: Python 3.13+ (backward compatible to 3.8+)
- **UI Framework**: Kivy (cross-platform GUI)
- **Data Processing**: Pandas (CSV handling)
- **Analytics**: Power BI (visualization and feature engineering)
- **Machine Learning**: Scikit-learn (progression recommendation models)
- **Threading**: Built-in threading for device ID generation
- **Data Storage**: CSV-based (historical data for ML training)
- **Package Management**: setuptools (pip installable)

## Project Structure

```
GrowFit/
├── growfit/                    # Main package
│   ├── __init__.py
│   ├── app.py                  # Main application entry point
│   ├── config/                 # Configuration files
│   │   ├── __init__.py
│   │   └── settings.py         # App settings and constants
│   ├── core/                   # Core functionality
│   │   ├── __init__.py
│   │   ├── data_manager.py     # Data management and device ID
│   │   └── utils.py            # Utility functions (counters)
│   ├── models/                 # Data models
│   │   ├── __init__.py
│   │   ├── exercise.py         # Exercise model (original: excercise.py)
│   │   └── routine.py          # Routine model
│   ├── services/               # Business logic services
│   │   ├── __init__.py
│   │   ├── routine_manager.py  # Routine management (original: routines/manager.py)
│   │   ├── series.py           # Series management (original: routines/series.py)
│   │   └── timer.py            # Timer functionality (original: timer/timer.py)
│   └── ui/                     # User interface (reserved for future)
│       └── __init__.py
├── tests/                      # Test suite
│   ├── test_core/             # Core functionality tests
│   ├── test_models/           # Model tests
│   ├── integration/           # Integration tests
│   └── __pycache__/
├── data/                      # Data files (CSV storage)
│   ├── app_lifecycle_data.csv
│   ├── device_id.txt
│   ├── exercise_data.csv
│   ├── routines_data.csv
│   ├── session_data.csv
│   └── user_profile.csv
├── requirements.txt           # Production dependencies
├── setup.py                   # Package installation
└── README.md                  # This file
```

## Installation

### Prerequisites
- Python 3.13+ (recommended) or 3.8+
- pip package manager

### Quick Start
```bash
# Clone the repository
git clone https://github.com/IRF1991/GrowFit.git
cd GrowFit

# Create virtual environment (recommended)
python -m venv venv
./venv/Scripts/activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .

# Run the application
python growfit/app.py
```


## Data Storage

The application uses CSV files for data persistence:

### Dynamic Data (Active Configuration)
- **`user_profile.csv`**: User demographics and fitness experience levels
- **`routines.csv`**: Workout routine definitions and metadata  
- **`device_id.txt`**: Unique device identifier for user/testing distinction

### Historical Data (ML Training Data)
Files with `_data.csv` suffix collect historical records for machine learning model training:
- **`exercise_data.csv`**: Detailed exercise tracking and performance data
- **`session_data.csv`**: Workout session timestamps and completion status
- **`routines_data.csv`**: Routine execution history and statistics
- **`app_lifecycle_data.csv`**: App usage patterns and user retention analytics

### Data Handling Approaches

#### Dynamic CSVs
- **Purpose:** Store temporary or real-time data that does not require advanced analysis.
- **Implementation:** Use `with` along with `**kwargs` to handle these files in a lightweight and customized way.
- **Advantages:**
  - Lightweight and straightforward.
  - Ideal for quick operations like saving or reading small data fragments.
  - Full control over how data is handled.

**Example:**
```python
# Save data to a dynamic CSV
def save_to_csv(file_path, data, **kwargs):
    with open(file_path, 'w') as file:
        for row in data:
            file.write(','.join(str(row[key]) for key in kwargs.keys()) + '\n')
```

#### Historical CSVs
- **Purpose:** Store accumulated or historical data that requires advanced analysis.
- **Implementation:** Use the Pandas library to efficiently handle these files and perform complex analyses.
- **Advantages:**
  - Optimized for large volumes of data.
  - Advanced tools for filtering, grouping, and transforming data.
  - Simplifies the handling of tabular data.

**Example:**
```python
import pandas as pd

# Analyze historical data
def analyze_history(file_path, **kwargs):
    df = pd.read_csv(file_path)
    for key, value in kwargs.items():
        df = df[df[key] == value]  # Filter based on kwargs
    return df.describe()  # Example: descriptive statistics
```

#### Workflow
1. **Save dynamic data:** Use `with` to write data to dynamic CSVs quickly and efficiently.
2. **Read and analyze historical data:** Use Pandas to load historical CSVs, filter relevant data, and perform advanced analyses.
3. **Integration:** Combine both approaches depending on the type of data being handled:
   - **Real-time or temporary data:** `with` + `**kwargs`.
   - **Accumulated or historical data:** Pandas.
```

## Development Setup

### INFORMACIÓN IMPORTANTE PARA DEVS

**The DataManager (located in `growfit/core/data_manager.py`) distinguishes between real users and testing users to preserve data integrity and facilitate developer testing.**

#### Purpose:
- Allow developers to have their own testing user version
- Prevent test data from interfering with real user data

#### How it works:
1. When running the app on a new device without `device_id.txt`, the console asks: **`¿Modo Testing? (y/N):`** to generate a unique ID
2. **"y"** generates a testing device_id with prefix `te_` (e.g., `te_7d95bb60`)
3. **Any other input** generates a normal user device_id with prefix `us_` (e.g., `us_a0d27a7a`)
4. **If the "Nueva Rutina" button is pressed**, a user device_id will be automatically generated

**The device_id is saved in `data/device_id.txt` to maintain it between sessions.**


#### User Types Summary:
- **Real Users**: Device ID prefix `us_` (e.g., `us_a0d27a7a`)
- **Testing Users**: Device ID prefix `te_` (e.g., `te_7d95bb60`)





## Branches

- **`main`**: Stable code
- **`testing`**: Development

## Roadmap

### Phase 1: Foundation ✅
- Core tracking functionality (reps, sets, time)
- Data management and storage system
- Basic UI navigation

### Phase 2: Progression System 🚧
- Exercise database with difficulty levels (1-10)
- Progression chains (prerequisite → current → next)
- Performance tracking and history

### Phase 3: Intelligence Layer
- ML model for progression recommendations
- Trigger detection (consistency → ready for next level)
- Power BI analytics dashboard

### Phase 4: Motivation & Engagement
- Gamification (achievements, streaks, unlocks)
- Progress visualization
- Milestone celebrations

### Phase 5: Expansion
- Exercise database validation with fitness professionals
- Community contributions
- Advanced features and mobile optimization

## License

This project is for educational and portfolio purposes.

## Author

**Ismael** - [GitHub](https://github.com/IRF1991)

