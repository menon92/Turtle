'''
Created on Sep 11, 2016
@author: Mehadi Hasan Menon
'''
import turtle

minar = turtle.Turtle() # create a turtle object

minar.pensize(2); minar.color('#B193B1') # set turtle size & color

minar.left(90); minar.fd(300); minar.fd(-600) # draw two perpendicular line 
minar.right(90); minar.fd(600); minar.fd(-1200) 

y1 = -250; x2 = 600; x3 = -550 # set initial position 

for i in range(24): # draw our national monument :)
    minar.goto(0, y1)
    minar.goto(x2, -300)
    minar.goto(x3, -300)
    y1 = y1 + 25
    x2 = x2 - 25
    x3 = x3 + 25
       
turtle.done()
