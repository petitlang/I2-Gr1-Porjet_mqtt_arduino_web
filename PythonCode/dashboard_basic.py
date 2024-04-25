import sqlite3
import turtle
import time
import tkinter as tk

## Chemin du fichier de base de données
db_path = 'animal_tracking.db'

def read_animal_data(name):
    """Lire les données de l'animal spécifié dans la base de données"""
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
    """Configurer le canevas et les objets graphiques initiaux"""
    screen = turtle.Screen()
    screen.title("Animal Dashboard")
    screen.setup(width=600, height=600)
    screen.tracer(0)  # Désactiver l'actualisation automatique
    
    # tracer des frontières
    border = turtle.Turtle()
    border.penup()
    border.goto(-250, -250)
    border.pendown()
    for _ in range(4):
        border.forward(500)
        border.left(90)
    border.hideturtle()
    
    # Créer une icône d'animal
    animal = turtle.Turtle()
    animal.shape("turtle")
    # animal.penup()
    animal.pendown()
    
    # Créer un affichage de la température
    temperature_display = turtle.Turtle()
    temperature_display.penup()
    temperature_display.hideturtle()
    temperature_display.goto(-200, 250)
    
    return screen, animal, temperature_display

def update_dashboard(screen, animal, temperature_display, position, temperature):
    """update dashboard"""
    animal.goto(position)
    temperature_display.clear()
    if temperature is not None:
        temperature_display.write(f"Temperature: {temperature} °C", font=("Arial", 12, "normal"))
    screen.update()  # Actualiser manuellement l'écran

def check_position_warning(position):
    """détection de position pour l'alarm"""
    min_x, min_y = -200, -200
    max_x, max_y = 200, 200
    if position[0] < min_x or position[0] > max_x or position[1] < min_y or position[1] > max_y:
        # send alarm
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showwarning("Warning", "Animal position is out of bounds!")
        root.destroy()

def main():
    screen, animal, temperature_display = setup_dashboard()
    
    while True:
        # we use panda
        animal_data = read_animal_data('Panda')
        if animal_data:
            position = (animal_data['x'], animal_data['y'])
            temperature = animal_data.get('temperature', 'N/A')
            update_dashboard(screen, animal, temperature_display, position, temperature)
            check_position_warning(position)  # 检查位置并发出警告消息
        time.sleep(1)  # Ajustez le temps de retard si nécessaire

if __name__ == "__main__":
    main()
