import turtle as tr

n = 5
pen = tr.Turtle()
pen.left(90)
pen.up()
pen.goto(0, -100)
pen.down()


def draw(Length):
    if Length > 40:
        pen.pensize(Length / 30)
        pen.fd(Length)
        pen.right(40)
        draw(Length - 9)
        pen.left(40)
        draw(Length - 8)
        pen.left(40)
        draw(Length - 9)
        pen.right(40)
        pen.backward(Length)


pen.speed(0)
draw(n * 9 + 41)

tr.done()
