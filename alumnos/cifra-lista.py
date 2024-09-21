#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Cifra la lista de alumnos
"""

import os


def cifra(cadena: str):
    """Función que cifra una cadena"""
    return cadena.title()


def cifra_archivo(archivo: str):
    """Función que cifra un archivo"""

    with open(archivo, encoding="utf-8") as csv_file:
        for line in csv_file:
            line = line.strip()
            campos = line.split(",")

            if campos[0] == "No":
                print(line)
                continue

            campos[1] = cifra(campos[1])
            campos[2] = cifra(campos[2])
            campos[3] = cifra(campos[3])

            linea = ",".join(campos)
            print(linea)


def main():
    """
    Función principal para cifrar un archivo csv
    """
    archivo = input("Ingresa el nombre el archivo CSV: ")

    if not os.path.exists(archivo):
        print(f"El archivo: {archivo}, no existe")
        return

    # password = getpass("Ingresa password: ")
    # sal = getpass("Ingresa la sal del algoritmo: ")

    cifra_archivo(archivo)


if __name__ == "__main__":
    main()
