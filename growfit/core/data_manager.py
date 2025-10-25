import pandas as pd
import os
import uuid
import threading

class DataManager:
    """
    Central data management system for GrowFit backend (FastAPI).
    - Loads and manages CSV data for the API REST endpoints.
    - Generates a unique device_id if not present.
    - Provides flexible methods to load and save data for backend logic.

    Usage:
    - Used exclusively by backend endpoints (not by UI/frontend).
    - All data access for the API is centralized here.
    - No direct access from Flutter or any frontend code.

    Methods:
    - __init__: Initializes the manager, loads CSVs, prepares dataframes.
    - get_csv(name): Returns the DataFrame for the given CSV name.
    - get_device_id(): Returns the unique device_id for the device.
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