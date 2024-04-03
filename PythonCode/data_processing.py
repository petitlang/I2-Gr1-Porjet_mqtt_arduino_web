# 处理从Arduino设备接收的数据，可能包括解析、存储和准备数据以供仪表板使用。
import paho.mqtt.client as mqtt

# 定义用于存储动物数据的字典
animal_data = {}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc)) # 函数参数rc（result code）是一个表示连接结果的代码，0表示连接成功，其他值则表示连接出现了问题。
    # 在这里订阅以确保连接建立后立即订阅
    client.subscribe("Panda")

def on_message(client, userdata, msg):
    # 解析收到的消息
    valeur = msg.payload.decode("utf-8")
    print(msg.topic + " " + valeur)
    
    # 解析动物信息
    try:
        elements = valeur.split(":")
        name = elements[0]  # 动物名
        x = int(elements[1])  # X坐标
        y = int(elements[2])  # Y坐标
        # 检查是否有温度数据
        temperature = None
        if len(elements) > 3 and elements[3].startswith('T='):
            temperature = float(elements[3][2:])
        
        # 更新动物数据
        animal_data[name] = {'x': x, 'y': y, 'temperature': temperature}
        print(f"Updated data for {name}: {animal_data[name]}")
    except Exception as e:
        print(f"Error processing message - {e}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Panda")
client.on_connect = on_connect
client.on_message = on_message

# 使用了isep的broker
client.connect("srv-lora.isep.fr")

# 开始MQTT客户端循环，以便持续监听消息
client.loop_forever()
