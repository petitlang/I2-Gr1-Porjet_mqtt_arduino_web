# 处理从Arduino设备接收的数据，可能包括解析、存储和准备数据以供仪表板使用。
import sqlite3
import paho.mqtt.client as mqtt

# 数据库文件路径
db_path = 'animal_tracking.db'

# 检查并创建表
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
    # 使用REPLACE来更新或插入新记录
    c.execute('REPLACE INTO animal_data (name, x, y, temperature) VALUES (?, ?, ?, ?)',
              (name, x, y, temperature))
    conn.commit()
    conn.close()

# MQTT消息回调
def on_message(client, userdata, msg):
    valeur = msg.payload.decode("utf-8")
    print(msg.topic + " " + valeur)
    
    try:
        elements = valeur.split(":")
        name = elements[0]  # 动物名
        x = int(elements[1])  # X坐标
        y = int(elements[2])  # Y坐标
        temperature = None
        if len(elements) > 3 and elements[3].startswith('T='):
            temperature = float(elements[3][2:])
        
        # 更新数据库
        update_database(name, x, y, temperature)
    except Exception as e:
        print(f"Error processing message - {e}")

def main():
    # 检查并设置数据库
    setup_database()
    
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Panda")
    client.connect("srv-lora.isep.fr")  # 以实际使用的broker地址和端口替换
    client.subscribe("Panda")
    client.on_message = on_message
    client.loop_forever()

if __name__ == "__main__":
    main()
