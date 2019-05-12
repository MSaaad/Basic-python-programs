import turtle

game=turtle.Turtle()
game.speed(10)
game.color('black')
def square(length,angle):
    for i in range(4):
        game.forward(length)
        game.right(angle)


for circle in range(100):
    square(100,90)
    game.right(11)

