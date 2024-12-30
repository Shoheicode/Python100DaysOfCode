import queue
import random
import sys
import time
from turtle import Screen, Turtle

turtle_t = Turtle()
turtle_t.turtlesize(0.5)
turtle_t.hideturtle()
turtle_t.speed(0)

sys.setrecursionlimit(2000)


def generate_maze(width, height, start=(1, 1), end=(1, 1)):
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

    maze[start[0]][start[1]] = float("inf")
    maze[end[0]][end[1]] = float("inf")

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
width = 100  # Maze width (must be odd)
height = 100  # Maze height (must be odd)
start = (1, 1)  # Start point
end = (width - 2, height - 2)  # End point
cubeS = 10
maze = generate_maze(width, height, start, end)
maze1 = maze.copy()
maze2 = maze.copy()


def draw_square(size=10):
    # Draw square
    turtle_t.forward(size)
    turtle_t.right(90)
    turtle_t.forward(size)
    turtle_t.right(90)
    turtle_t.forward(size)
    turtle_t.right(90)
    turtle_t.forward(size)
    turtle_t.right(90)


def draw_map(maze, start, end):
    turtle_t.penup()
    for row in range(len(maze)):
        for x in range(len(maze[row])):
            if maze[row][x] == -1:
                turtle_t.setpos((x * cubeS) - 200, (row * -cubeS) + 250)
                turtle_t.color("black")
                turtle_t.pendown()
                draw_square(cubeS)
            turtle_t.penup()
            # turtle_t.shape("square")
        turtle_t.penup()

    turtle_t.setpos((end[0] * cubeS) - 200, (end[1] * -cubeS) + 250)
    turtle_t.pendown()
    turtle_t.color("blue")
    draw_square(cubeS)

    turtle_t.penup()

    turtle_t.setpos((start[0] * cubeS) - 200, (start[1] * -cubeS) + 250)
    turtle_t.pendown()
    turtle_t.color("red")
    draw_square(cubeS)


draw_map(maze, start, end)


def solve_maze_bfs(maze):

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

            if maze[y][x] == float("inf"):
                qu.put((x, y))
                maze[y][x] = maze[val[1]][val[0]] + 1


def solve_maze_dfs(maze):
    # set a list called distance to store the distance being infinity
    stack = []
    stack.append(end)

    maze[end[1]][end[0]] = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while len(stack) > 0:
        val = stack.pop()
        for dx, dy in directions:
            x = val[0] + dx
            y = val[1] + dy

            if maze[y][x] == float("inf"):
                stack.append((x, y))
                maze[y][x] = maze[val[1]][val[0]] + 1


start_time = time.time()
solve_maze_bfs(maze1)
end_time = time.time()

print("Time taken: ", end_time - start_time)

start_time = time.time()
solve_maze_dfs(maze2)
end_time = time.time()

print("Time taken: ", end_time - start_time)


# Go through the maze using breadth first search
def go_through_maze(maze):
    # Set the properties of the turtle
    turtle_t.speed("slowest")
    turtle_t.showturtle()
    turtle_t.penup()

    # Set the starting position of the turtle
    turtle_t.setpos((1 * cubeS) + 10 - 200, (1 * -cubeS) - 10 + 250)

    # Define the directions the turtle can move
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Set the starting position of the turtle in the array and ending position
    x = 1
    y = 1
    endpos = (width - 2, height - 2)

    # Set the distance to 0 and create a queue
    dis = 0
    q = queue.Queue()

    # Put the starting position in the queue
    q.put((x, y))

    # While the queue is not empty, move the turtle to the next position
    while not q.empty():
        # if the distance is 999, break the loop that way if the turle doesn't reach the end, it stops
        if dis == 999:
            break

        # Get the next position from the queue
        val = q.get()

        # If the position is the end position, break the loop
        if val == endpos:
            break

        # Check for each of the direction that the turtle can move to the next position
        for dx, dy in directions:
            # Set the current position of the turtle
            curX = val[0]
            curY = val[1]

            currentDis = maze[curY][curX]
            # Check if the next position is the next distance
            if currentDis - 1 == maze[curY + dy][curX + dx]:
                # set the current position to the next position
                x = x + dx
                y = y + dy
                turtle_t.setpos((x * cubeS) + 10 - 200, (y * -cubeS) - 10 + 250)

                # Put the next position in the queue
                q.put((x, y))
        # Increase the distance
        dis = dis + 1


go_through_maze(maze1)

screen = Screen()
print(screen.screensize())
screen.tracer(0)
screen.exitonclick()
