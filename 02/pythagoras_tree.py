import turtle
import platform
import sys


def draw_pifagor_tree(turtle, size, order):
    angle = 45
    if order == 0:
        return
    else:
        turtle.forward(size)
        turtle.right(angle)
        draw_pifagor_tree(turtle, size * 0.7, order - 1)
        turtle.left(2 * angle)
        draw_pifagor_tree(turtle, size * 0.7, order - 1)
        turtle.right(angle)
        turtle.backward(size)


def drawing(order):
    # Set up the turtle
    t = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("white")
    t.speed(0)
    t.left(90)
    t.penup()
    t.pendown()
    # Draw the Pythagoras tree
    draw_pifagor_tree(t, size=100, order=order)
    # Close the turtle graphics window on click
    turtle.exitonclick()


def main():
    # Turtle does not work on Python > 3.8 on Mac
    if (
        platform.system() == "Darwin"
        and sys.version_info[0] >= 3
        and sys.version_info[1] > 8
    ):
        print("Use Python 3.x < 3.9")
        exit()
    # Waiting integer number input
    while True:
        try:
            steps = int(input("Set Pythagoras tree complexity >>>"))
            break
        except ValueError:
            print("Please type number!")
    drawing(order=steps)


if __name__ == "__main__":
    main()
