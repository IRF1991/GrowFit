
import 'package:flutter/material.dart';
import 'data_management/device_id_manager.dart';

import 'screens/main_screen.dart';
import 'screens/routine_screen.dart';
import 'screens/exercise_screen.dart';
import 'screens/new_routine_screen.dart';
import 'screens/new_exercise_screen.dart';
import 'screens/timer_screen.dart';
import 'screens/pop_up_screen.dart';


void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final deviceId = await DeviceIdManager.getDeviceId();
  // Puedes imprimirlo para debug:
  // print('Device ID: $deviceId');
  runApp(const GrowFitApp());
}

class GrowFitApp extends StatelessWidget {
  const GrowFitApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GrowFit',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => MainScreen(),
        '/routine': (context) => RoutineScreen(),
        '/exercise': (context) => ExerciseScreen(),
        '/new_routine': (context) => NewRoutineScreen(),
        '/new_exercise': (context) => NewExerciseScreen(),
        '/timer': (context) => TimerScreen(),
        '/popup': (context) => PopUpScreen(),

      },
    );
  }
}
