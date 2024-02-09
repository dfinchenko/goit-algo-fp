import turtle
import math

def draw_tree(branch_length, level):
    if level <= 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(45)

        draw_tree(branch_length / math.sqrt(2), level - 1)

        turtle.right(90)
        draw_tree(branch_length / math.sqrt(2), level - 1)

        turtle.left(45)
        turtle.backward(branch_length)

def main():
    turtle.speed('fastest')
    turtle.left(90)

    # Запитуємо рівень рекурсії у користувача
    level = int(input("Введіть рівень рекурсії: "))  
    draw_tree(70, level)
    turtle.done()

if __name__ == "__main__":
    main()