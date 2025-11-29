import turtle
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Recursively draw a Koch snowflake using turtle graphics"
    )

    parser.add_argument(
        "-o", "--order",
        type=int,
        default=3,
        help="Depth of recursion (default=3)"
    )

    parser.add_argument(
        "-s", "--size",
        type=int,
        default=600,
        help="Size of snowflake (default=600)"
    )
    return parser.parse_args()


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def main(order=3, size=600):

    window = turtle.Screen()
    window.setup(1000, 1000)
    window.bgcolor("black")
    window.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")
    t.penup()
    t.goto(-size / 2, -(size * (3**0.5) / 6))
    t.setheading(60)
    t.pendown()

    koch_snowflake(t, order, size)

    t.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    args = parse_args()
    main(args.order, args.size)
