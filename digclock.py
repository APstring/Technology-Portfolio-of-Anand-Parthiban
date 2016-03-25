from graphics import *
import time
class DigitalClock(CanvasFrame):
    def __init__(self, hour, minute, second):
        self.hour = hour
        if self.hour > 12:
            self.hour -= 12
            self.daynight = 'PM'
        else:
            self.daynight = 'AM'
        self.minute = minute
        self.second = second
        self.x = CanvasFrame.getWidth(new_win)
        self.y = CanvasFrame.getHeight(new_win)
        self.pos = Point((self.x)/2, (self.y)/2)
        self.face = Rectangle(Point(30, self.y-30),Point(self.x- 30 , 30))
        self.face.setFill('red')
        self.t = Text(self.pos, str(self.hour)+':'+str(self.minute)+':'+str(self.second)+' '+str(self.daynight))
        
        
        
    def new_time(self, win):
        self.total = self.hour*3600 + self.minute*60 + self.second
        self.total += 1
        self.hour = self.total//3600
        self.minute = (self.total%3600)//60
        self.second = (self.total%3600)%60
        if self.hour > 12:
            self.hour -= 12
            self.daynight = 'PM'
        else:
            self.daynight = 'AM'
        self.stringit()
        win.after(1000, self.new_time, win) 
        
        
    def stringit(self):   
        self.t.setText(str(self.hour)+':'+str(self.minute)+':'+str(self.second)+' '+str(self.daynight))
        self.t.setSize(20)
        self.t.setStyle('italic')
        self.t.setTextColor('green')
        
        
    def draw(self, win):
            self.face.draw(win)                      
            self.t.draw(win)
            self.new_time(win)
            
            
new_win = GraphWin("Digital Clock", 300, 300)
clock = DigitalClock(15, 30, 23)
clock.draw(new_win)
new_win.mainloop()
