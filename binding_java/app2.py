
##- copiando al .venv la clase compilada

import shutil
import subprocess
import os

venv_directory = '.venv'
target_directory = os.path.join(venv_directory, 'src/ejemplo')
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

java_file_path = 'src/ejemplo/MiClase.java'
venv_directory = '.venv/'
destination_directory = os.path.join(venv_directory, 'src/ejemplo/')
shutil.copy(java_file_path, destination_directory)

try:
    subprocess.run(['javac', 'MiClase.java'], cwd=destination_directory)
except subprocess.CalledProcessError as e:
    print(f'Error al compilar: {e}')

java_home='C:\Program Files\Java\jdk-17.0.8'
os.environ["JAVA_HOME"] = java_home    

##-- 

from jnius import autoclass

MiClase = autoclass('src.ejemplo.MiClase')
mi_clase = MiClase()
mensaje = mi_clase.obtenerMensaje()
print(mensaje)
