import queue
import random
from turtle import Screen, Turtle

turtle_t = Turtle()
turtle_t.speed(0)


def generate_maze(width, height):
    # Define the maze grid
    maze = [[-1 for _ in range(width)] for _ in range(height)]

    # Define movement directions: (dx, dy)
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    # Helper function to carve out the maze
    def carve(x, y):
        maze[y][x] = 0
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == -1:
                maze[y + dy // 2][x + dx // 2] = float(
                    "inf"
                )  # Remove wall between cells
                carve(nx, ny)

    # Start carving from a random point
    start_x, start_y = (
        1,
        1,
    )  # random.randrange(1, width, 2), random.randrange(1, height, 2)
    carve(start_x, start_y)

    maze[1][1] = -2  # Start point
    maze[height - 2][width - 2] = -3  # End point

    return maze


def print_maze(maze):
    for row in maze:
        st = ""
        for cell in row:
            if cell == -1:
                st = st + "X"
            elif cell == -2:
                st = st + "S"
            elif cell == -3:
                st = st + "E"
            else:
                st = st + " "
        print(st)


# Example usage
width = 21  # Maze width (must be odd)
height = 21  # Maze height (must be odd)
maze = generate_maze(width, height)
print_maze(maze)


def draw_square():
    # Draw square
    turtle_t.forward(10)
    turtle_t.right(90)
    turtle_t.forward(10)
    turtle_t.right(90)
    turtle_t.forward(10)
    turtle_t.right(90)
    turtle_t.forward(10)
    turtle_t.right(90)


def draw_map(maze):
    for row in range(len(maze)):
        for x in range(len(maze[row])):
            if maze[row][x] == 1:
                turtle_t.setpos(x * 10, row * 10)
                turtle_t.pendown()
                draw_square()
            turtle_t.penup()
            # turtle_t.shape("square")
        turtle_t.penup()


draw_map(maze)


def solve_maze(maze):

    qu = queue.Queue()
    qu.put((1,1))

    while not qu.empty():
        


screen = Screen()
screen.exitonclick()
