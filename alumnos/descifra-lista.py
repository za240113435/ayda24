#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Descifra la lista de alumnos
"""

import base64
import os
from getpass import getpass
from hashlib import sha256

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def descifra(cadena: str, f: Fernet):
    """Función que descifra una cadena"""

    token = f.decrypt(cadena.encode())
    return token.decode()


def calcula_cifrado(password: str, sal: str):
    """Función que calcula el algoritmo de descifrado"""

    bpassword = password.encode()

    # Obtenemos los primeros 16 bytes
    # salt = os.urandom(16)
    bsal = sha256(sal.encode()).digest()[:16]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bsal,
        iterations=1_000_000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(bpassword))

    f = Fernet(key)

    return f


def descifra_archivo(archivo: str, password: str, sal: str):
    """Función que descifra un archivo"""

    # Cadena usada para guardar el descifrado del archivo
    descifrado = ""

    # Algoritmos de Fernet
    f = calcula_cifrado(password, sal)

    with open(archivo, encoding="utf-8") as csv_file:
        for line in csv_file:
            campos = line.split(",")

            if campos[0] == "No":
                descifrado = line
                continue

            campos[1] = descifra(campos[1], f)
            campos[2] = descifra(campos[2], f)
            # Quitamos el salto de linea con strip
            campos[3] = descifra(campos[3].strip(), f)

            linea = ",".join(campos)
            descifrado += linea + "\n"

    with open("descifrado.csv", "w", encoding="utf-8") as csv_file:
        csv_file.write(descifrado)


def main():
    """
    Función principal para descifrar un archivo csv
    """
    archivo = input("Ingresa el nombre el archivo CSV: ")

    if not os.path.exists(archivo):
        print(f"El archivo: {archivo}, no existe")
        return

    password = getpass("Ingresa password: ")
    sal = getpass("Ingresa la sal del algoritmo: ")

    descifra_archivo(archivo, password, sal)


if __name__ == "__main__":
    main()
