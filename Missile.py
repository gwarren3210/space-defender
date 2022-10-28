from tkinter import *
import time,random

class Missile:
     
       #### to complete

    # methods are similar to explosion class, look there for comments if missing
    def __init__(self, canvas,  ceiling=0, increment=5, color='orange', width=8, height=25):
        self.can = canvas
        self.ceiling = ceiling  # used for firewoks file to change where the missiles explode
        self.inc = increment    # speed of the missile
        self.col = color
        # missile dimensions
        self.width = width
        self.height = height
        self.__active = False

    def activate(self, x, y):
        self.__active = True
        self.x = x
        self.y = y        
        dx = self.width/2           # what to add to each side of x (to clean up the rectangle creation)
        self.rocket = self.can.create_rectangle(self.x+dx, self.y+self.height, self.x-dx, self.y, fill=self.col)  # drawing the missile on the canvas
        

    def deactivate(self):
        self.__active = False
        self.can.delete(self.rocket)
    
    def is_active(self): 
        return self.__active

    def next(self):
        if self.__active == True:
            self.can.move(self.rocket, 0, -self.inc)        # moving the missile in the y direction by the increment
            self.y -= self.inc                              # changing the missiles y-value as canvas.move() doesn't
            if (self.y+self.height)<0:      # if the missile gets too high...
                self.deactivate()               # say bye bye!
            
    # same as add_explosion from Explosion but without the supplement
    @staticmethod
    def add_missile(canvas, missiles, x,y, ceiling=0, increment=5, color='orange'):
        # same technique as in missiles to get rid of excess missiles
        for m in missiles:
            if m.is_active() == False:
                missiles.pop(missiles.index(m))
        
        new = Missile(canvas, ceiling, increment, color)
        missiles.append(new)
        new.activate(x,y)
        


###################################################
###################################################

        
def main(): 
       
        ##### create a window, canvas and ball object
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Missiles
        missiles=[]
        
        
        ############################################
        ####### start simulation
        ############################################
        t=0                # initialize time clock       
        while True:

         ##### To complete
            if t%50==0:     # sending a missile ever .5 seconds
                #print(missiles)
                colors = ['blue', 'yellow', 'green', 'purple', 'red', 'orange']     # dif options for the color of the rocket
                canvas_w = 800          # canvas width
                canvas_h = 1000         # canvas height
                x=random.randint(0,canvas_w)        # random x value
                ceiling = random.randint(0,canvas_h/2)      # random ceiling ( doesn't matter but wtvr)
                increment = random.randint(2,7)     # random speed
                color = random.choice(colors)       # random color
                Missile.add_missile(canvas, missiles, x,canvas_h, ceiling, increment, color)        # adding missile
            
            # making the missiles flyyyyyy
            for missile in missiles:
                missile.next()


            # check active status of list of booms (for debugging)
            for m in missiles:
                print(m.is_active(),end=" ")
            print()
            
            # update the graphic and wait time        
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1      # increment time
       
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()