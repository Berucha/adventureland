##########################################################################
# Author: Berucha Cintron and Bethanie Williams
# Username: cintronb williamsbe
#
# Program Name Fireworks
#
# Cited Source: https://trinket.io/python/a5fa7b17c2
# Programmer Acknowledgements - Harry Ingram
#
########################################################################

import random
import turtle


class Fireworks:                 #fireworks code that we imported from someone else
    def __init__(self):
        '''
        turtles draw fireworks
        '''
        self.tina = turtle.Turtle()
        self.tina.speed(0)
        self.sky('black')
        while True:
            self.firework(50)
            self.pen('red')

            self.move()
            self.pen('yellow')
            self.firework(75)
            self.move()

            self.pen('orange')
            self.firework(199)
            self.firework(50)
            self.move()

            self.pen('blue')
            self.firework(75)
            self.move()

            self.pen('pink')
            self.firework(199)
            self.firework(50)
            self.move()

            self.pen('yellow')
            self.firework(75)
            self.move()

            self.pen('orange')
            self.firework(199)
            self.firework(50)
            self.move()

            self.pen('blue')
            self.firework(75)
            self.move()

            self.pen('pink')
            self.firework(199)
            self.firework(50)
            self.move()

            self.pen('yellow')
            self.firework(75)
            self.move()

            self.pen('orange')
            self.firework(199)
            self.firework(50)
            self.move()
            self.pen('blue')
            self.firework(75)
            self.move()

            self.pen('pink')
            self.firework(199)
            self.firework(50)
            self.move()

            self.pen('yellow')
            self.firework(75)
            self.move()

            self.pen('orange')
            self.firework(199)
            self.firework(50)
            self.move()

            self.pen('blue')
            self.firework(75)
            self.move()

            self.pen('pink')
            self.firework(199)

    # firework color
    def pen(self, colour):
        self.tina.color(colour)

    # move to a new place on screen
    def move(self):
        self.tina.pu()
        x = random.randint(-165, 165)
        y = random.randint(-165, 165)
        self.tina.goto(x, y)
        self.tina.pd()

    # set the sky black
    def sky(self, colour):
        wn = turtle.Screen()
        wn.bgcolor(colour)

    # draw a firework
    def firework(self, size):
        for num in range(20):
            self.tina.fd(size)
            self.tina.rt(180 - (360 / 20))

# Fireworks()
