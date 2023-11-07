import warnings
warnings.filterwarnings("ignore")
import os

path=os.environ["PATH"]
java_home='C:\Program Files\Java\jdk-17.0.8'
os.environ["PATH"] = java_home+';path'
os.environ["JAVA_HOME"] = java_home

##-----

from jnius import autoclass

MiClase = autoclass('src.ejemplo.MiClase')
mi_clase = MiClase()
mensaje = mi_clase.obtenerMensaje()

# Imprimir el resultado
print(mensaje)