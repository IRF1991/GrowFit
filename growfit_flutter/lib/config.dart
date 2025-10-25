/// Configuración centralizada de URLs para GrowFit Flutter.
///
/// Cambia el valor de [apiBaseUrl] según el entorno:
/// - Desarrollo local con emulador Android: 'http://10.0.2.2:8000/api/v1/data'
/// - Desarrollo local con dispositivo físico: 'http://<IP_PC>:8000/api/v1/data'
/// - Producción: 'https://api.tuapp.com/api/v1/data'

const String apiBaseUrl = 'http://10.0.2.2:8000/api/v1/data';
