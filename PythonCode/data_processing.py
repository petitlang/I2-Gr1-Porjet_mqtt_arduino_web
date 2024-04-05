'''
Traitement des données reçues des dispositifs Arduino, ce qui peut inclure l'analyse,
le stockage et la préparation des données en vue de leur utilisation dans les tableaux de bord.
'''
import sqlite3
import paho.mqtt.client as mqtt

# path database
db_path = 'animal_tracking.db'

# verifier et creer la tableau
def setup_database():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS animal_data (
            name TEXT PRIMARY KEY,
            x INTEGER,
            y INTEGER,
            temperature REAL
        )
    ''')
    conn.commit()
    conn.close()

def update_database(name, x, y, temperature):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # update data par REPLACE
    c.execute('REPLACE INTO animal_data (name, x, y, temperature) VALUES (?, ?, ?, ?)',
              (name, x, y, temperature))
    conn.commit()
    conn.close()

# MQTT_ON_MSG
def on_message(client, userdata, msg):
    valeur = msg.payload.decode("utf-8")
    print(msg.topic + " " + valeur)
    
    try:
        elements = valeur.split(":")
        name = elements[0]  # nom animal
        x = int(elements[1])  # X coordoneé
        y = int(elements[2])  # Y coordoneé
        temperature = None
        if len(elements) > 3 and elements[3].startswith('T='):
            temperature = float(elements[3][2:])
        
        # update database
        update_database(name, x, y, temperature)
    except Exception as e:
        print(f"Error processing message - {e}")

def main():
    #  Vérification et configuration de la base de données
    setup_database()
    
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Panda")
    client.connect("srv-lora.isep.fr")
    client.subscribe("Panda")
    client.on_message = on_message
    client.loop_forever()

if __name__ == "__main__":
    main()
