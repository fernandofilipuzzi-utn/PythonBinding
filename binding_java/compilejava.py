import subprocess

# Ruta al directorio que contiene tus archivos .java
java_source_directory = "src/ejemplo/"

# Compila todas las clases Java en ese directorio
subprocess.run(["javac", "*.java"], cwd=java_source_directory)
