import subprocess
import os
import time

# Directorio principal
project_dir = os.path.dirname(os.path.abspath(__file__))

# Directorios de backend y front
backend_dir = os.path.join(project_dir, "back")
front_dir = os.path.join(project_dir, "front")

# Obtener las rutas completas a los archivos
backend_script = os.path.join(backend_dir, "backend.py")
front_script = os.path.join(front_dir, "planoRounda.py")

# Cambiar al directorio de backend y ejecutar backend.py
os.chdir(backend_dir)
backend_process = subprocess.Popen(["python", "backend.py"])

time.sleep(3)

# Cambiar al directorio de front y ejecutar planoRounda.py
os.chdir(front_dir)
front_process = subprocess.Popen(["python", "planoRounda.py"])

# Esperar a que planoRounda.py finalice
front_process.wait()

# Cuando planoRounda.py termine, el proceso de backend.py también finalizará
backend_process.terminate()
