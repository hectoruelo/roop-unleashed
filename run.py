#!/usr/bin/env python3
from roop import core
import subprocess
import time

# Función que ejecuta tu programa en segundo plano
def ejecutar_programa():
    subprocess.Popen(["python", "test.py"])

# Ejecutar la función en segundo plano
ejecutar_programa()


if __name__ == '__main__':
    core.run()
