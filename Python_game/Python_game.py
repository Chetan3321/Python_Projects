import tkinter as tk
import random

# Configurable Grid Size
GRID_SIZE = 20  # Space size per block
DEFAULT_WIDTH = 20  # 20 blocks wide
DEFAULT_HEIGHT = 20  # 20 blocks tall

SPEED = 100  # Lower = faster
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BG_COLOR = "#000000"

direction = "down"
score = 0

class Snake:
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = []

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)

class Food:
    def __init__(self, canvas, width, height):
        x = random.randint(0, (width // GRID_SIZE) - 1) * GRID_SIZE
        y = random.randint(0, (height // GRID_SIZE) - 1) * GRID_SIZE
        self.coordinates = [x, y]
        self.food = canvas.create_oval(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=FOOD_COLOR)

def start_game():
    global snake, food, direction, score
    canvas.delete("all")
    direction = "down"
    score = 0
    label.config(text=f"Score: {score}")
    canvas.update()  # Get actual width and height
    snake = Snake(canvas)
    food = Food(canvas, canvas.winfo_width(), canvas.winfo_height())
    next_turn()

def next_turn():
    global direction, score, food

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= GRID_SIZE
    elif direction == "down":
        y += GRID_SIZE
    elif direction == "left":
        x -= GRID_SIZE
    elif direction == "right":
        x += GRID_SIZE

    new_head = [x, y]
    snake.coordinates.insert(0, new_head)

    square = canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete(food.food)
        food = Food(canvas, canvas.winfo_width(), canvas.winfo_height())
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(canvas):
        game_over()
    else:
        window.after(SPEED, next_turn)

def change_direction(new_direction):
    global direction
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if new_direction != opposites.get(direction):
        direction = new_direction

def check_collision(canvas):
    x, y = snake.coordinates[0]
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    if x < 0 or x >= width or y < 0 or y >= height:
        return True
    if [x, y] in snake.coordinates[1:]:
        return True
    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2 - 30,
                       text="GAME OVER", fill="red", font=('Arial', 24))
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       text=f"Final Score: {score}", fill="white", font=('Arial', 16))

    restart_btn = tk.Button(window, text="Play Again", font=('Arial', 14), command=start_game)
    canvas.create_window(canvas.winfo_width() / 2, canvas.winfo_height() / 2 + 40, window=restart_btn)

# UI Setup
window = tk.Tk()
window.title("Snake Game")
window.geometry(f"{DEFAULT_WIDTH * GRID_SIZE + 20}x{DEFAULT_HEIGHT * GRID_SIZE + 120}")
window.minsize(300, 300)

label = tk.Label(window, text="Score: 0", font=('Arial', 14))
label.pack(pady=(10, 0))

start_button = tk.Button(window, text="Start Game", command=start_game, font=('Arial', 14))
start_button.pack(pady=(5, 10))

canvas = tk.Canvas(window, bg=BG_COLOR, height=DEFAULT_HEIGHT * GRID_SIZE, width=DEFAULT_WIDTH * GRID_SIZE)
canvas.pack(expand=True, fill="both")

# Direction Buttons
controls = tk.Frame(window)
controls.pack(pady=10)

tk.Button(controls, text="↑", command=lambda: change_direction("up"), width=5).grid(row=0, column=1)
tk.Button(controls, text="←", command=lambda: change_direction("left"), width=5).grid(row=1, column=0)
tk.Button(controls, text="→", command=lambda: change_direction("right"), width=5).grid(row=1, column=2)
tk.Button(controls, text="↓", command=lambda: change_direction("down"), width=5).grid(row=2, column=1)

# Keyboard support
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))

window.mainloop()
