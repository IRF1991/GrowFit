# GrowFit

**Smart fitness app that grows with you - AI-powered workout recommendations and adaptive progression tracking**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Kivy](https://img.shields.io/badge/Kivy-UI%20Framework-orange.svg)](https://kivy.org)
[![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)](https://github.com)

## Vision

GrowFit is an intelligent fitness application designed to create personalized workout experiences through advanced data analytics and machine learning. The app learns from user behavior patterns and collaborative data to recommend optimal workout routines and guide progressive improvement.

### Key Features (Planned)

- **AI-Powered Recommendations**: Personalized workout suggestions based on user data and community insights
- **Advanced Analytics**: Comprehensive tracking of workout performance, adherence, and progression
- **Adaptive Progression**: Smart exercise difficulty adjustment based on user performance
- **Cross-Platform**: Built with mobile-first approach using Python and Kivy
- **Goal-Oriented Training**: Customizable fitness goals with intelligent progression paths

## Current Status

### Completed
- Core counter functionality for reps/sets/time tracking
- Multi-screen navigation system (Kivy-based)
- Data management system with CSV-based storage
- User/Testing mode distinction for data integrity
- Device identification system for user tracking

### In Development
- Timer functionality for rest periods and hold exercises
- Exercise database with categorization and difficulty levels
- Routine creation and management system

### Planned Features
- Machine learning recommendation engine
- Nutrition tracking and calculation system
- Progress analytics and visualization
- Community-based collaborative filtering
- Export/import functionality for workout data

## Technology Stack

- **Backend**: Python 3.13+ (backward compatible to 3.8+)
- **UI Framework**: Kivy (cross-platform GUI)
- **Data Processing**: Pandas (CSV handling)
- **Threading**: Built-in threading for device ID generation
- **Future ML**: Scikit-learn (planned)
- **Data Storage**: CSV-based (SQLite migration planned)
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

1. **Phase 1**: Core functionality (Exercise tracking, Timers) ✅
2. **Phase 2**: Enhanced UI and routine management 🚧
3. **Phase 3**: Data analytics and basic recommendations
4. **Phase 4**: Machine learning integration
5. **Phase 5**: Mobile deployment and advanced features

## License

This project is for educational and portfolio purposes.

## Author

**Ismael** - [GitHub](https://github.com/IRF1991)

