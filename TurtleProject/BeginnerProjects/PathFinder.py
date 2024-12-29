import queue
import random
from turtle import Screen, Turtle

turtle_t = Turtle()
turtle_t.turtlesize(0.5)
turtle_t.hideturtle()
turtle_t.speed(0)


def generate_maze(width, height):
    # Define the maze grid
    maze = [[-1 for _ in range(width)] for _ in range(height)]

    # Define movement directions: (dx, dy)
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    # Helper function to carve out the maze
    def carve(x, y):
        maze[y][x] = float("inf")
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

    # maze[1][1] = -2  # Start point
    # maze[height - 2][width - 2] = -3  # End point

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
                if cell == float("inf"):
                    st = st + " "
                else:
                    st = st + str(cell)
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
            if maze[row][x] == -1:
                turtle_t.setpos(x * 10, row * -10)
                turtle_t.color("black")
                turtle_t.pendown()
                draw_square()
            elif row == height - 2 and x == width - 2:
                turtle_t.setpos(x * 10, row * -10)
                turtle_t.pendown()
                turtle_t.color("blue")
                draw_square()
                print("HEY", row, x)
            turtle_t.penup()
            # turtle_t.shape("square")
        turtle_t.penup()


draw_map(maze)


def solve_maze(maze):

    qu = queue.Queue()

    endpos = (width - 2, height - 2)
    qu.put(endpos)

    maze[endpos[1]][endpos[0]] = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while not qu.empty():
        val = qu.get()
        for dx, dy in directions:
            x = val[0] + dx
            y = val[1] + dy

            # print("(", x, ",", y, ")")
            if maze[y][x] == float("inf"):
                qu.put((x, y))
                maze[y][x] = maze[val[1]][val[0]] + 1


solve_maze(maze)

print_maze(maze)

print(maze[height - 2][width - 2])


# Go through the maze using breadth first search
def go_through_maze(maze):
    turtle_t.speed("slowest")
    turtle_t.showturtle()
    turtle_t.penup()
    turtle_t.setpos((1 * 10) + 5, (1 * -10) + 5)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = 1  # (1 * 10) + 5
    y = 1  # (1 * 10) - 5
    endpos = (width - 2, height - 2)

    dis = 0
    q = queue.Queue()
    q.put((x, y))

    while not q.empty():
        if dis == 999:
            break
        val = q.get()
        if val == endpos:
            break
        for dx, dy in directions:
            curX = val[0]
            curY = val[1]
            currentDis = maze[curY][curX]
            if currentDis - 1 == maze[curY + dy][curX + dx]:
                x = x + dx
                y = y + dy
                turtle_t.setpos((x * 10) + 5, (y * -10) - 5)
                q.put((x, y))
        dis = dis + 1


go_through_maze(maze)

screen = Screen()
screen.tracer(0)
screen.exitonclick()
