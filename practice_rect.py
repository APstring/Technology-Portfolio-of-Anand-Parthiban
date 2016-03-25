from graphics import *

class Box():
    def __init__(self, point1, point2):
        self.rect = Rectangle(point1, point2)

    def draw(self, win):
        self.rect.draw(win)

    def move(self, dx, dy):
        self.rect.move(dx,dy)

    def set_color(self,rect_color):
        self.rect.setFill(rect_color)

    def undraw(self):
        self.rect.undraw()

    def animate(self, win, dx, dy, n):
        self.move(dx, dy)
        win.after(100, self.animate, win, dx, dy, n-1)
