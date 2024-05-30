# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:19:44 2024

@author: soufiane
"""

import serial

# Paramètres du port série
port = 'COM8'  # Modifier selon le port COM utilisé sur votre PC
baudrate = 115200  # Modifier selon le débit en bauds de votre périphérique

# Ouvrir la connexion avec le port série
ser = serial.Serial(port, baudrate)

# Nom du fichier de sortie
output_file = 'donnees_port_serie2_pile12.txt'

try:
    # Ouvrir le fichier en mode écriture
    with open(output_file, 'w') as file:
        # Lire les données du port série indéfiniment
        while True:
            # Lire une ligne de données du port série
            data = ser.readline().decode().strip()
            # Afficher les données lues
            print(data)
            # Écrire les données dans le fichier
            file.write(data + '\n')

except KeyboardInterrupt:
    # Arrêt du programme si l'utilisateur appuie sur Ctrl+C
    print("Arrêt du programme.")
    ser.close()  # Fermer la connexion série
