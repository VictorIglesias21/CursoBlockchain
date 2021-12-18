# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:55:39 2021

@author: victor
"""

# Módulo 1 - Crear una Blockchain
# Instalamos Flask, librería (framework) para hacer aplicaciones web, y para distribuir la blockchain en diferentes servers
# pip install Flask==1.1.2
# Utilizaremos Postman para hacer peticiones a nuestra Blockchain (añadir una transacción, etc...), mediante ficheros Json

# Importar librerías
# Librería para trabajar con fechas, ya que los bloques necesitan un timestamp
import datetime

# Librería para crear el hashing de los bloques
import hashlib

# Librería json, objeto para transmitir datos a través de una red
import json

# De la librería Flask vamos a importar dos cosas, el constructor para crear un objeto de la clase Flask,
# Y la función jsonify que devolverá el mensaje que postman utilizará para interactuar con la blockchain
from flask import Flask, jsonify

# Parte 1 - Crear la cadena de bloques (definir variables)
class Blockchain:

    # El Init es el método constructor, que se llama cuando se quiere crear algún objeto de la clase
    def __init__(self):
        # Lista que irá conteniendo todos los bloques a medida que los vayamos minando
        self.chain = []
        # Generamos el bloque Génesis, necesitamos los atributos del número de bloque, y el hash del bloque previo
        self.create_block(proof = 1, previous_hash = '0')
        
        
# Parte 2 - Programar el minado de la blockchain

