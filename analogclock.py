
from graphics import *
import time
from math import *
class AnalogClock(CanvasFrame):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.x_coor = CanvasFrame.getWidth(new_win)
        self.y_coor = CanvasFrame.getHeight(new_win)
        self.center = Point((self.x_coor)/2, (self.y_coor)/2)
        self.radius = (self.x_coor - 60)/2
        self.face = Circle(self.center,self.radius)
        self.face.setFill('purple1')
        self.time()
    
    def time(self):
        self.line1 = Line(self.center, Point(self.radius/3*cos((self.hour*pi/6)-pi/2)+ self.x_coor/2, self.radius/3*sin((self.hour*pi/6)-pi/2)+self.y_coor/2))
        self.line2 = Line(self.center, Point(self.radius*cos((self.minute*pi/30)-pi/2)+ self.x_coor/2, self.radius*sin((self.minute*pi/30)-pi/2)+self.y_coor/2))
        self.line3 = Line(self.center, Point(self.radius*0.9*cos((self.second*pi/30)-pi/2)+ self.x_coor/2, self.radius*0.9*sin((self.second*pi/30)-pi/2)+self.y_coor/2))
        self.line2.setArrow('last')
        self.line1.setArrow('last')
        self.line3.setArrow('last')
        
    def undraw(self):
        self.line1.undraw()
        self.line2.undraw()
        self.line3.undraw()

    def realdraw(self,win):
        self.line1.draw(win)
        self.line2.draw(win)
        self.line3.draw(win)
        
    def moveit(self, win):
        self.undraw()
        self.total = self.hour*3600 + self.minute*60 + self.second
        self.total += 1
        self.hour = self.total//3600
        self.minute = (self.total%3600)//60
        self.second = (self.total%3600)%60
        self.time()
        self.realdraw(win)
        win.after(1000, self.moveit, win)
        
    def draw(self, win):
            self.face.draw(win)                      
            self.line1.draw(win)
            self.line2.draw(win)
            self.line3.draw(win)
            self.moveit(win)
            
new_win = GraphWin("Analog Clock", 500, 500)
clock = AnalogClock(10, 49, 59)
clock.draw(new_win)
new_win.mainloop() 
