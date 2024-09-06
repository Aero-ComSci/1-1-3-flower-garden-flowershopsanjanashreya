import turtle as trtl

# Global painter variable
painter = None
x = -410  # Initialize x globally

def start():
    global painter
    trtl.bgcolor("light blue")
    painter = trtl.Turtle()
    painter.speed(0)
    painter.color("brown")
    painter.setheading(0)
    painter.fillcolor("brown")
    painter.begin_fill()
    painter.forward(300)
    painter.right(100)
    painter.forward(250)
    painter.right(80)
    painter.forward(600)
    painter.right(100)
    painter.forward(250)
    painter.right(80)
    painter.forward(300)
    painter.end_fill()

def positionreset(g):
    global painter
    painter.penup()
    painter.goto(g, -100)
    painter.pendown()
    painter.setheading(0)

def drawstem():
    global painter, x
    x += 100
    positionreset(x)
    painter.color('green')
    painter.begin_fill()
    painter.forward(20)
    painter.left(90)
    painter.forward(210)
    painter.left(90)
    painter.forward(20)
    painter.left(90)
    painter.forward(210)
    painter.left(90)
    painter.end_fill()
    painter.forward(20)
    painter.left(90)
    painter.forward(210)
    painter.left(180)
    painter.begin_fill()
    painter.forward(150)
    painter.left(120)
    painter.forward(50)
    painter.left(90)
    painter.forward(20)
    painter.left(80)
    painter.forward(55)
    painter.right(120)
    painter.forward(140)
    painter.left(90)
    painter.end_fill()
    painter.forward(20)

def drawtulip():
    global painter
    drawstem()
    painter.setheading(180)
    painter.color("purple")
    painter.penup()
    painter.forward(60)
    painter.pendown()
    painter.begin_fill()
    painter.left(90)
    painter.circle(60, 180)
    painter.forward(30)
    painter.left(125)
    painter.forward(40)
    painter.end_fill()
    painter.begin_fill()
    painter.left(285)
    painter.forward(40)
    painter.left(85)
    painter.forward(40)
    painter.left(-100)
    painter.forward(40)
    painter.setheading(260)
    painter.forward(40)
    painter.end_fill()

def drawsunflower():
    global painter
    painter.tiltangle(180)
    drawstem()
    painter.color('yellow')
    def drawpetal():
        painter.begin_fill()
        painter.circle(100, 60)
        painter.left(120)
        painter.circle(100, 60)
        painter.left(120)
        painter.end_fill()
    for _ in range(12):
        drawpetal()
        painter.left(30)
    painter.forward(-40)
    painter.right(90)
    painter.forward(-2)
    painter.color('brown')
    painter.begin_fill()
    painter.circle(40)
    painter.end_fill()

def drawdaisy():
    global painter
    drawstem()
    painter.color('white')
    def drawpetal():
        painter.begin_fill()
        painter.circle(60, 60)
        painter.left(120)
        painter.circle(60, 60)
        painter.left(120)
        painter.end_fill()
    for _ in range(12):
        drawpetal()
        painter.left(30)
    painter.forward(-10)
    painter.right(90)
    painter.forward(-2)
    painter.color('yellow')
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()

def drawlotus():
    global painter
    drawstem()
    painter.color('pink')
    def drawpetal():
        painter.begin_fill()
        painter.circle(60, 60)
        painter.left(120)
        painter.circle(60, 60)
        painter.left(120)
        painter.end_fill()
    for _ in range(12):
        drawpetal()
        painter.left(30)

def drawmarigold():
    global painter
    drawstem()
    painter.color('orange')
    def drawpetal():
        painter.begin_fill()
        painter.circle(70, 60)
        painter.left(120)
        painter.circle(70, 60)
        painter.left(120)
        painter.end_fill()
    def drawinside():
        painter.color('yellow')
        painter.begin_fill()
        painter.circle(30, 60)
        painter.left(120)
        painter.circle(30, 60)
        painter.left(120)
        painter.end_fill()
    for _ in range(36):
        drawpetal()
        painter.left(10)
    for _ in range(18):
        drawinside()
        painter.left(20)

def draw_flowers(flower_count):
    global painter
    for flower, count in flower_count.items():
        for _ in range(count):
            if flower == 'sunflower':
                drawsunflower()
            elif flower == 'daisy':
                drawdaisy()
            elif flower == 'lotus':
                drawlotus()
            elif flower == 'tulip':
                drawtulip()
            elif flower == 'marigold':
                drawmarigold()
