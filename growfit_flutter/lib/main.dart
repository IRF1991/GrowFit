

import 'package:flutter/material.dart';
import 'data_management/device_id_manager.dart';

// Importación de todas las pantallas principales de la app.
import 'screens/main_screen.dart';
import 'screens/routine_screen.dart';
import 'screens/exercise_screen.dart';
import 'screens/new_routine_screen.dart';
import 'screens/new_exercise_screen.dart';
import 'screens/timer_screen.dart';
import 'screens/pop_up_screen.dart';


/// Punto de entrada principal de la aplicación GrowFit.
///
/// - Inicializa los bindings de Flutter.
/// - Garantiza que el device_id esté creado y disponible para toda la app.
/// - Lanza la aplicación principal [GrowFitApp].
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized(); // Necesario para inicializaciones asíncronas antes de runApp
  await DeviceIdManager.getDeviceId(); // Asegura que el device_id esté generado y persistido
  runApp(const GrowFitApp());
}

/// Widget raíz de la aplicación GrowFit.
///
/// Configura el tema, las rutas y la navegación principal de la app.
class GrowFitApp extends StatelessWidget {
  /// Constructor constante para el widget principal de la app.
  const GrowFitApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GrowFit', // Título de la aplicación
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple), // Paleta de colores base
        useMaterial3: true, // Usa Material 3 para un diseño moderno
      ),
      initialRoute: '/', // Ruta inicial al abrir la app
      routes: {
        // Definición de rutas principales de la app
        '/': (context) => MainScreen(), // Pantalla principal
        '/routine': (context) => RoutineScreen(), // Pantalla de rutina
        '/exercise': (context) => ExerciseScreen(), // Pantalla de ejercicio
        '/new_routine': (context) => NewRoutineScreen(), // Crear nueva rutina
        '/new_exercise': (context) => NewExerciseScreen(), // Crear nuevo ejercicio
        '/timer': (context) => TimerScreen(), // Pantalla de temporizador
        '/popup': (context) => PopUpScreen(), // Pantalla de pop-up
      },
    );
  }
}
