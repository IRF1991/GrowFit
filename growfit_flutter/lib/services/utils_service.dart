import 'dart:convert';
import 'package:http/http.dart' as http;
import '../config.dart'; // Importa la configuración centralizada

/// Servicio para acceder a las utilidades del backend de GrowFit vía API REST.
/// Este servicio solo consume la API, nunca accede a lógica de backend directamente.
/// Cambia la URL base en config.dart según el entorno (ver documentación allí).
class UtilsService {
  static final String baseUrl = apiBaseUrl.replaceFirst('/data', '/utils');

  static Future<int> incrementCounter(int counter) async {
    final response = await http.post(
      Uri.parse('$baseUrl/increment_counter'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'counter': counter}),
    );
    if (response.statusCode == 200) {
      return jsonDecode(response.body)['result'];
    } else {
      throw Exception('Error al incrementar el contador');
    }
  }

  static Future<int> reduceCounter(int counter) async {
    final response = await http.post(
      Uri.parse('$baseUrl/reduce_counter'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'counter': counter}),
    );
    if (response.statusCode == 200) {
      return jsonDecode(response.body)['result'];
    } else {
      throw Exception('Error al reducir el contador');
    }
  }

  static Future<int> countDown(int counter) async {
    final response = await http.post(
      Uri.parse('$baseUrl/count_down'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'counter': counter}),
    );
    if (response.statusCode == 200) {
      return jsonDecode(response.body)['result'];
    } else {
      throw Exception('Error en count_down');
    }
  }
}
