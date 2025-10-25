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

GrowFit está dividido en dos partes independientes:

- **Backend**: Python + FastAPI
  - Expone una API REST para toda la lógica, gestión de datos y modelos ML.
  - Accede a los datos (CSV, modelos, etc.) y expone endpoints para la app.
  - Se ejecuta en local para desarrollo o en la nube para producción.

- **Frontend**: Flutter (Dart)
  - UI moderna y multiplataforma (Android/iOS).
  - Solo consume la API REST del backend, nunca accede a datos ni lógica interna directamente.
  - Configuración de la URL base en `lib/config.dart`.

## Despliegue y desarrollo

### Requisitos previos
- Python 3.8+
- pip
- Flutter 3.x+
- (Opcional) Android Studio/Emulador

### Backend (FastAPI)
1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Lanza el backend:
   ```bash
   uvicorn growfit.main:app --reload
   ```
3. Accede a la documentación interactiva en [http://localhost:8000/docs](http://localhost:8000/docs)

### Frontend (Flutter)
1. Entra en la carpeta:
   ```bash
   cd growfit_flutter
   ```
2. Instala dependencias:
   ```bash
   flutter pub get
   ```
3. Configura la URL base en `lib/config.dart` según el entorno:
   - Emulador Android: `http://10.0.2.2:8000/api/v1/data`
   - Dispositivo físico: `http://<IP_PC>:8000/api/v1/data`
   - Producción: `https://api.tuapp.com/api/v1/data`
4. Lanza la app:
   ```bash
   flutter run
   ```

## Project Structure

```
GrowFit/
├── growfit/                # Backend (FastAPI, lógica, datos)
│   ├── main.py             # FastAPI app entrypoint
│   ├── api/                # Endpoints REST
│   ├── core/               # Lógica y utilidades
│   ├── models/             # Modelos de datos
│   └── ...
├── growfit_flutter/        # Frontend (Flutter UI)
│   ├── lib/
│   │   ├── screens/        # Pantallas
│   │   ├── services/       # Servicios para consumir la API
│   │   └── config.dart     # Configuración de la URL base
├── data/                   # Datos (CSV, modelos ML, etc.)
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Notas importantes
- La app Flutter nunca accede directamente a los datos ni ejecuta lógica de backend.
- Toda la comunicación es vía API REST.
- Para modo offline, la lógica y datos deben migrarse a Flutter (ver documentación interna).

## Tecnología
- **Backend**: Python 3.8+, FastAPI, Pandas, ML (futuro)
- **Frontend**: Flutter (Dart)
- **Data**: CSV, modelos ML

## Funcionamiento y filosofía

GrowFit es una app de entrenamiento inteligente que adapta la progresión de ejercicios a tu ritmo, usando analítica de datos y recomendaciones personalizadas. Consulta la documentación interna y los comentarios en el código para detalles sobre la lógica de progresión, gestión de rutinas y funcionamiento general.

