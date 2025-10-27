// Pantalla TimerScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Pantalla de temporizador.
/// (Pendiente de implementar lógica y UI).
class TimerScreen extends StatelessWidget {
  const TimerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Timer')), 
      body: const Center(
        child: Text(
          'Timer Screen (to be implemented)',
          style: TextStyle(fontSize: 22),
        ),
      ),
    );
  }
}
