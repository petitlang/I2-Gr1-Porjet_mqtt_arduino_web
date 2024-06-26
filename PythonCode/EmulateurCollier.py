import paho.mqtt.client as mqtt
import time
import random
import json


def genere_msg(id):
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    t = random.randrange(38,50)
    temp = f"T={t}"
    return f"{id}:{x}:{y}:{temp}"


def ajoute_json(msg):
    msg_dico = {"object":{"message":msg}}
    return json.dumps(msg_dico)

def publie_msg(msg_json):
    print(f"Publie : \"{msg_json}\"...")
    client.publish(msg_topic, msg_json)

# Programme principal

colliers = ["Panda"] # "Marguerite", "Medor", "Felix"

msg_topic = "Panda" # "emulateur_colliers"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "hal")
client.connect("srv-lora.isep.fr")

while True:
    for collier in colliers:
        msg = genere_msg(collier)
        msg_json = ajoute_json(msg)
        publie_msg(msg_json)
        time.sleep(3)
        