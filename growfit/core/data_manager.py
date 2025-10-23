import pandas as pd
import os
import uuid
import threading

class DataManager:
    """
    Sistema de gestión centralizado para CSVs del proyecto.
    - Carga los CSVs DINÁMICOS necesarios al iniciar la app, otros CSVs se cargarán bajo demanda.
    - Genera un device_id único si no existe.
    - Ofrece métodos flexibles para cargar y guardar datos dinámicamente.
    
    - función: __init__: Constructor de clase. Inicializa el objeto DataManager y prepara la estructura de datos para toda la app.
        
        - self.data_dir: define la carpeta donde se almacenan los CSVs. Por defecto, "data/".
        - os.makedirs(self,data_dir,exist_ok=True): crea la carpeta data/ si no existe, si ya existe no hace nada.
        - self.device_id = self._load_or_create_device_id(): llama a la función que carga o genera un device_id único.
        - self.csv_map{}: define los CSV que se cargarán al inicio. Estos CSV serán: user_profile.csv, routines.csv y session_data.csv.
        - self.dataframes{}: prepara un diccionario para almacenar los DataFrames cargados de cada CSV.
        - _load_csv(path): función interna que carga un CSV existente dado su path y devuelve un DataFrame. Si el CSV no existe, lanza una excepción.
        
    - función: _load_or_create_device_id(self): Carga el device_id único desde el dispositivo o lo genera si no existe.
    
        - Comprueba si existe un archivo device_id.txt en la carpeta data/.
        - Si existe, lee el device_id desde el archivo.
        - Si no existe, solicita al usuario que seleccione el tipo de usuario y genera un device_id basado en el tipo de usuario y un UUID.
        - Si la respuesta no es válida, asigna "Usuario" por defecto.
        - Genera un ID único con el prefijo según tipo y un UUID acortado (por ejemplo, "us_ab12cd34" para usuarios; "te_ab12cd34" para testing).
        - Guarda el device_id en device_id.txt para futuros usos, este txt es persistente y local al dispositivo, útil para respaldos y migraciones.
        - Retorna el device_id generado o leído.
        
    - función: _load_csv(self, path): Carga un CSV desde el path dado y devuelve un DataFrame.
    
        - Comprueba si el archivo existe, en caso contrario lanza una excepción. Esto evita que la app cree nuevos archivos vacíos.
        - Intenta cargar el CSV usando pd.read_csv().
        - En caso de error durante la carga, imprime un mensaje y devuelve un DataFrame vacío.
        
    - función: get_csv(self, name): Devuelve el DataFrame correspondiente al nombre dado.
    
        - Comprueba si name existe en self.dataframes.
        - Si no existe, lanza una excepción KeyError.
        - Si existe, devuelve el DataFrame correspondiente.
        - Forma de acceder a los datos cargados, para centralizar el acceso y evitar errores de path o nombres incorrectos.
        
    - función: get_device_id(self): Devuelve el device_id único del dispositivo.
    
    """

    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

        # --- Atributos base ---
        self.is_testing = False
        self.device_id = None

        # --- NUEVO: ruta para guardar el ID del dispositivo ---
        self.device_id_path = os.path.join(self.data_dir, "device_id.txt")

        # --- Rutas CSV ---
        self.csv_map = {
            "user_profile": os.path.join(self.data_dir, "user_profile.csv"),
            "routines": os.path.join(self.data_dir, "routines.csv"),
            "session_data": os.path.join(self.data_dir, "session_data.csv")
        }

        # --- Carga inicial ---
        self.dataframes = {}
        for name, path in self.csv_map.items():
            self.dataframes[name] = self._load_csv(path)

    
    def _ask_testing_option(self):
        """
        Solicita por entrada estándar el tipo de usuario y genera device_id correspondiente.
        
        Ejecuta en hilo separado para evitar bloquear la interfaz gráfica durante la inicialización.
        Genera device_id con prefijo 'te_' para testing o 'us_' para usuario final.
        Persiste el ID generado en archivo device_id.txt para reutilización en sesiones futuras.
        
        Returns:
            None: Modifica self.device_id y persiste en disco como efecto lateral.
        """
        import time
        if os.path.exists(self.device_id_path):
            with open(self.device_id_path, "r") as f:
                self.device_id = f.read().strip()
            print(f"Device ID existente: {self.device_id}")
            return

        # Espera medio segundo para que los prints previos terminen
        time.sleep(0.5)
        resp = input("Is Testing? (y/N): ").strip().lower()
        self.is_testing = resp == "y"
        prefix = "te" if self.is_testing else "us"
        self.device_id = f"{prefix}_{uuid.uuid4().hex[:8]}"

        with open(self.device_id_path, "w") as f:
            f.write(self.device_id)

        print(f"[INFO] Device ID generado: {self.device_id}")

    def create_user_if_needed(self):
        """
        Genera device_id de usuario final si no existe ninguno previamente.
        
        Implementa patrón fallback para casos donde el hilo de consulta no ha completado
        o el usuario no respondió al prompt de consola. Garantiza que siempre exista
        un device_id válido antes de operaciones que requieren identificación de usuario.
        
        Returns:
            None: Modifica self.device_id y persiste en disco si es necesario.
        """
        if self.device_id is None:
            self.is_testing = False
            self.device_id = f"us_{uuid.uuid4().hex[:8]}"
            with open(self.device_id_path, "w") as f:
                f.write(self.device_id)
            print(f"[INFO] Device ID generado por botón: {self.device_id}")

            # Si es desde hilo de consola, NO genera nada todavía
            return None
        
    def start_device_id_thread(self):
        """
        Inicia hilo daemon para generación asíncrona de device_id mediante consulta de consola.
        
        Permite que la aplicación continue su inicialización normal mientras solicita
        en paralelo la preferencia del usuario sobre el tipo de ID (testing vs producción).
        El hilo daemon termina automáticamente al finalizar el proceso principal.
        
        Returns:
            None: Efecto lateral de crear hilo en threading.Thread pool.
        """
        threading.Thread(target=self._ask_testing_option, daemon=True).start()

    def _load_csv(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"CSV no encontrado: {path}")
        try:
            df = pd.read_csv(path)
            return df
        except Exception as e:
            print(f"Error al cargar {path}: {e}")
            return pd.DataFrame()

    def get_csv(self, name):
        if name not in self.dataframes:
            raise KeyError(f"No se encuentra el DataFrame con nombre: {name}")
        return self.dataframes[name]

    def get_device_id(self):
        """
        Retorna el identificador único del dispositivo actual.
        
        Returns:
            str: Device ID con formato '{prefijo}_{uuid8}' donde prefijo es 'us' para 
                 usuarios finales o 'te' para entornos de testing. None si no se ha 
                 generado aún (estado de inicialización).
        """
        return self.device_id