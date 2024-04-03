# 使用Python图形库（如turtle）实现的基础仪表板，展示动物位置和警报。
import time
import turtle

def setup_dashboard():
    # 设置画布
    screen = turtle.Screen()
    screen.title("Animal Dashboard")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # 画布边界
    turtle.penup()
    turtle.goto(-250, -250)
    turtle.pendown()
    turtle.goto(-250, 250)
    turtle.goto(250, 250)
    turtle.goto(250, -250)
    turtle.goto(-250, -250)
    turtle.penup()

    # 创建动物图标
    animal = turtle.Turtle()
    animal.shape("turtle")
    animal.penup()

    # 创建温度显示
    temperature_display = turtle.Turtle()
    temperature_display.penup()
    temperature_display.hideturtle()
    temperature_display.goto(-200, 250)
    
    return animal, temperature_display

def update_dashboard(animal, temperature_display, position, temperature):
    # 更新动物位置
    animal.goto(position)
    
    # 更新温度显示
    temperature_display.clear()
    temperature_display.write(f"Temperature: {temperature} °C", font=("Arial", 12, "normal"))

def main():
    # 初始化仪表板
    animal, temperature_display = setup_dashboard()
    
    while True:
        # 模拟获取位置和温度数据
        # 这里假设位置数据是一个二元元组 (x, y)，温度数据是一个整数
        
        # 更新仪表板
        update_dashboard(animal, temperature_display, animal_position, temperature)
        
        # 延迟一段时间
        time.sleep(10)  # 这里的时间延迟应与Arduino代码中发送数据的频率相匹配

if __name__ == "__main__":
    main()