# https://www.malnasuli.hu/oktatas/a-python-programozasi-nyelv-6-a-python-turtle-teknos-konyvtar/
import turtle

ablak = turtle.Screen()
ablak.setup(400, 400)
ablak.bgcolor('black')
ablak.title("program_4")
fred = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
for i in range(180):
    t.pencolor(colors[i % 6])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)
ablak.exitonclick()
