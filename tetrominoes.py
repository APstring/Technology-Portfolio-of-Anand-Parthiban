

from graphics import *
#from Python_beginnersHW4 import *
class Bloc(Rectangle):
    def __init__(self, coor, color = 'red'):
        self.block = Rectangle(Point((coor.x-1)*30, (coor.y)*30),Point(coor.x*30, (coor.y-1)*30))
        self.block.setFill(color)

    def draw(self,win):
        self.block.draw(win)

    def move(self, dx,dy):
        self.block.move(dx,dy)

    #just added for later use
    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx,dy)
            win.after(100, self.animate, win, dx, dy, n-1)

"""
class Shape(Block):
    def __init__(self, coorlist, color):
        self.block1 = Block(coorlist[0], color)
        self.block2 = Block(coorlist[1], color)
        self.block3 = Block(coorlist[2], color)
        self.block4 = Block(coorlist[3], color)

    def draw(self, win):
        Block.draw(self.block1, win)
        Block.draw(self.block2, win) 
        Block.draw(self.block3, win) 
        Block.draw(self.block4, win) 
            
class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y),
                    Point(center.x - 1, center.y),
                    Point(center.x , center.y),
                    Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "blue")

class J_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x-1, center.y),
                    Point(center.x, center.y),
                    Point(center.x+1 , center.y),
                    Point(center.x + 1, center.y+1)]
        Shape.__init__(self, coords, "orange")

class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                    Point(center.x - 1, center.y),
                    Point(center.x , center.y),
                    Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "black")

class O_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                    Point(center.x - 1, center.y + 1),
                    Point(center.x , center.y),
                    Point(center.x , center.y + 1)]
        Shape.__init__(self, coords, "red")

class S_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                    Point(center.x, center.y + 1),
                    Point(center.x , center.y),
                    Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "green")


class T_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                    Point(center.x, center.y),
                    Point(center.x , center.y + 1),
                    Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "yellow")


class Z_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                    Point(center.x, center.y),
                    Point(center.x , center.y + 1),
                    Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, "purple")
        
win = GraphWin("Tetrominoes", 900, 150)
# a list of shape classes
tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
x = 3
for tetromino in tetrominoes:
    shape = tetromino(Point(x, 1))
    shape.draw(win)
    x += 4
win.mainloop()
"""
