import random
from turtle import Screen, Turtle

turtle_t = Turtle()


def generate_maze(width, height):
    # Define the maze grid
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # Define movement directions: (dx, dy)
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    # Helper function to carve out the maze
    def carve(x, y):
        maze[y][x] = 0
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == 1:
                maze[y + dy // 2][x + dx // 2] = 0  # Remove wall between cells
                carve(nx, ny)

    # Start carving from a random point
    start_x, start_y = random.randrange(1, width, 2), random.randrange(1, height, 2)
    carve(start_x, start_y)


def print_maze(maze):
    for row in maze:
        print("".join("#" if cell == 1 else " " for cell in row))


# Example usage
width = 21  # Maze width (must be odd)
height = 21  # Maze height (must be odd)
maze = generate_maze(width, height)
print_maze(maze)


screen = Screen()
screen.exitonclick()
