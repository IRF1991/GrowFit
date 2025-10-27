import 'dart:convert';
import 'package:http/http.dart' as http;
import '../config.dart'; // Importa la configuración centralizada

/// Servicio para acceder a los datos del backend de GrowFit vía API REST.
/// Este servicio solo consume la API, nunca accede a datos ni lógica de backend directamente.
/// Cambia la URL base en config.dart según el entorno (ver documentación allí).
class DataService {
  static const String baseUrl = apiBaseUrl;

  static Future<List<dynamic>> getUserProfile() async {
    final response = await http.get(Uri.parse('$baseUrl/user_profile'));
    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Error al obtener user_profile');
    }
  }

  static Future<List<dynamic>> getRoutines() async {
    final response = await http.get(Uri.parse('$baseUrl/routines'));
    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Error al obtener routines');
    }
  }

  static Future<List<dynamic>> getSessionData() async {
    final response = await http.get(Uri.parse('$baseUrl/session_data'));
    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Error al obtener session_data');
    }
  }

  static Future<String> getDeviceId() async {
    final response = await http.get(Uri.parse('$baseUrl/device_id'));
    if (response.statusCode == 200) {
      return jsonDecode(response.body)['device_id'];
    } else {
      throw Exception('Error al obtener device_id');
    }
  }
}
