import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    for _ in range(4):
        t.forward(length)
        t.left(90)

    t.forward(length)
    t.left(45)

    new_length = length / math.sqrt(2)

    draw_pythagoras_tree(t, new_length, level - 1)

    t.right(45)
    t.backward(length)

    t.left(90)
    t.forward(length)
    t.right(45)

    draw_pythagoras_tree(t, new_length, level - 1)

    t.left(45)
    t.backward(length)
    t.right(90)

def main():
    level = int(input("Введіть рівень рекурсії (рекомендовано від 1 до 10): "))

    screen = turtle.Screen()
    screen.title("Дерево Піфагора")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed("fastest")
    t.color("green")
    t.left(90) 
    t.up()
    t.goto(0, -200)
    t.down()

    length = 100

    draw_pythagoras_tree(t, length, level)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
