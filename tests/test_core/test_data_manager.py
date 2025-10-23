import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import time
from growfit.core.data_manager import DataManager

dm = DataManager()  # Al iniciar, te pedirá tipo de usuario si no hay device_id.txt
dm.start_device_id_thread()

print("Esperando device_id...")
time.sleep(2)  # Da tiempo al hilo para preguntar

print("device_id:", dm.get_device_id())
print("CSV cargados:", list(dm.dataframes.keys()))
for k, df in dm.dataframes.items():
    print(f" - {k}: filas={len(df)}, columnas={list(df.columns)}")