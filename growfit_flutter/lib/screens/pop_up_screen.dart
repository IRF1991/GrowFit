// Pantalla PopUpScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Pantalla de pop-up.
/// (Pendiente de implementar lógica y UI).
class PopUpScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Pop Up')), 
      body: const Center(
        child: Text(
          'Pop Up Screen (to be implemented)',
          style: TextStyle(fontSize: 22),
        ),
      ),
    );
  }
}
