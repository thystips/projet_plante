#!/usr/bin/python3
import random
import threading
import time
import mysql.connector


def releves():
    threading.Timer(10.0, releves).start()
    temperature = random.randint(-50, 50)
    humidite = random.randint(0, 100)
    luminosite = random.randint(0, 100)

    plant_uf = mysql.connector.connect(
        host="localhost", user="emmadrd912", password="manonemma33", database="plant_uf"
    )

    curseur = plant_uf.cursor()

    curseur.execute(
        """
        UPDATE datas
        SET data_humidity=%s, data_luminosity=%s, data_temperature=%s
        WHERE uplant_id=%s
        """,
        (humidite, luminosite, temperature, 1),
    )

    plant_uf.commit()
    plant_uf.close()


releves()
