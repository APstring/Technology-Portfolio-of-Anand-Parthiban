from wheel import *
def main():
    # create a window with width = 700 and height = 500
    new_win = GraphWin('Wheel', 1000, 1000) 

    # What we'll need for the wheel...
    wheel_center1 = Point(100, 100) # The wheel center is a Point at (200, 200)
    wheel_center2 = Point(400, 100) # The wheel center is a Point at (200, 200)
    tire_radius1 = 50  # The radius of the outer tire is 100
    tire_radius2 = 50  # The radius of the outer tire is 100
    # Make a wheel object
    new_wheel1 = Wheel(wheel_center1, 0.6*tire_radius1, tire_radius1)
    new_wheel2 = Wheel(wheel_center2, 0.6*tire_radius2, tire_radius2)
    # Set its color
    new_wheel1.set_color('red', 'green')
    new_wheel2.set_color('red', 'green')
    # And finally, draw it 
    new_wheel1.draw(new_win)
    new_wheel2.draw(new_win)
    new_wheel1.animate(new_win, 1, 0, 100)
    new_wheel2.animate(new_win, 1, 0,100)
    # What we'll need for the wheel...
    
    # The radius of the outer tire is 100

    # Make a wheel object
    

    # Set its color
    

    # And finally, draw it 
   
    # Run the window loop (must be the *last* line in your code)
    
    new_win.mainloop()

# Comment this call to main() when you import this code into
#  your car.py file - otherwise the Wheel will pop up when you
#  try to run your car code.
main()
