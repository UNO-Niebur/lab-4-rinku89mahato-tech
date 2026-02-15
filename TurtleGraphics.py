
#TurtleGraphics.py
#Name: Rinku Mahato
#Date: 02/15/2026
#Assignment:Turtle Graphics , show pentagon, Octogon, cornerfilled,Sqaure in sqauare 

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):  
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):     
    for s in range(sides):
        bob.forward(70)
        bob.left(360/sides)

def fillCorner(shonn,corner):
    drawSquare(shonn,100)
    if corner == 1:
        shonn.begin_fill()
        drawSquare(shonn, 50)
        shonn.end_fill()
    elif corner == 2: 
        shonn.forward(50) 
        shonn.begin_fill() 
        drawSquare(shonn, 50) 
        shonn.end_fill()
    elif corner == 3:
        shonn.right(90)
        shonn.forward(50)
        shonn.left(90)
        shonn.begin_fill()
        drawSquare(shonn, 50)
        shonn.end_fill()
        
def squaresInSquares(Sami,num):
    size = 150   
    for i in range(num):
        drawSquare(Sami, size)   
        size -= 20            
        Sami.up()
        Sami.forward(10)
        Sami.right(90)
        Sami.forward(10)
        Sami.left(90)
        Sami.down()

     

def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares
   


main()
