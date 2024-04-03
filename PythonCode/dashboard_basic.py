import sqlite3
import turtle
import time

# 数据库文件路径
db_path = 'animal_tracking.db'

def read_animal_data(name):
    """从数据库读取指定动物的数据"""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT x, y, temperature FROM animal_data WHERE name = ?', (name,))
    data = c.fetchone()
    conn.close()
    if data:
        return {'x': data[0], 'y': data[1], 'temperature': data[2]}
    else:
        return None

def setup_dashboard():
    """设置画布和初始图形对象"""
    screen = turtle.Screen()
    screen.title("Animal Dashboard")
    screen.setup(width=600, height=600)
    screen.tracer(0)  # 关闭自动刷新
    
    # 绘制边界
    border = turtle.Turtle()
    border.penup()
    border.goto(-250, -250)
    border.pendown()
    for _ in range(4):
        border.forward(500)
        border.left(90)
    border.hideturtle()
    
    # 创建动物图标
    animal = turtle.Turtle()
    animal.shape("turtle")
    animal.penup()
    
    # 创建温度显示
    temperature_display = turtle.Turtle()
    temperature_display.penup()
    temperature_display.hideturtle()
    temperature_display.goto(-200, 250)
    
    return screen, animal, temperature_display

def update_dashboard(screen, animal, temperature_display, position, temperature):
    """更新仪表板上的动物位置和温度"""
    animal.goto(position)
    temperature_display.clear()
    if temperature is not None:
        temperature_display.write(f"Temperature: {temperature} °C", font=("Arial", 12, "normal"))
    screen.update()  # 手动刷新屏幕

def main():
    screen, animal, temperature_display = setup_dashboard()
    
    while True:
        # 这里我们以"Panda"为例
        animal_data = read_animal_data('Panda')
        if animal_data:
            position = (animal_data['x'], animal_data['y'])
            temperature = animal_data.get('temperature', 'N/A')
            update_dashboard(screen, animal, temperature_display, position, temperature)
        time.sleep(1)  # 根据需要调整延迟时间

if __name__ == "__main__":
    main()
