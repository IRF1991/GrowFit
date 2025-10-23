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

- **Backend**: Python 3.8+
- **UI Framework**: Kivy
- **Data Processing**: Pandas
- **Future ML**: Scikit-learn (planned)
- **Data Storage**: CSV-based (SQLite migration planned)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
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
python main.py
```

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python tests/test_core/test_data_manager.py

# Run integration tests
python tests/integration/test_app.py
```

## Requirements

```
pandas>=2.0.0
kivy>=2.1.0
```

## Development Setup

### INFORMACIÓN IMPORTANTE PARA DEVS

**El DataManager permite distinguir entre usuarios reales y usuarios de testing para preservar la integridad de los datos y facilitar pruebas por desarrolladores.**

#### Objetivo:
- Permitir que un desarrollador tenga su propia versión de usuario marcada como testing
- Evitar que datos de prueba interfieran con los datos reales del usuario

#### Cómo funciona:
1. Al ejecutar la app en un dispositivo nuevo sin `device_id.txt`, la consola pregunta: **`¿Modo Testing? (y/N):`** para generar un ID único
2. **"y"** genera un device_id de testing con prefijo `te_` (ej. `te_7d95bb60`)
3. **Cualquier otra cosa** genera un device_id de usuario normal con prefijo `us_` (ej. `us_a0d27a7a`)
4. **Si se pulsa el botón "Nueva Rutina"**, se generará automáticamente un device_id de usuario

**El device_id se guarda en `data/device_id.txt` para mantenerlo entre sesiones.**

#### User Types Summary:
- **Real Users**: Device ID prefix `us_` (e.g., `us_a0d27a7a`)
- **Testing Users**: Device ID prefix `te_` (e.g., `te_7d95bb60`)

## Data Architecture

The application uses a comprehensive CSV-based data system designed for future ML implementation:

- **User Profiles**: Physical data and experience levels
- **Routines**: Workout structure and metadata
- **Exercises**: Detailed exercise configurations and tracking
- **Sessions**: Historical workout data for analytics
- **Lifecycle**: App usage patterns and retention analysis

## Contributing

This project is currently in active development as a portfolio piece. Feel free to explore the code and provide feedback!

## Roadmap

1. **Phase 1**: Core functionality (Exercise tracking, Timers)
2. **Phase 2**: Data analytics and basic recommendations
3. **Phase 3**: Machine learning integration
4. **Phase 4**: Mobile deployment and advanced features

## License

This project is for educational and portfolio purposes.

## Author

**Ismael** - *Initial work* - [GitHub Profile](https://github.com/IRF1991)

---

*GrowFit - Where fitness meets intelligence*

