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
