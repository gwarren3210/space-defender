from cmath import exp
from decimal import Clamped
from tkinter import *
import math,time,random
from Dot import Dot
import numpy as np


class Explosion:

    #### to complete
    def __init__(self, canvas, max_radius=80, color='rainbow'):
        self.num_dots = 15              # number of dots per row
        self.can = canvas            # to refer to canvas later
        self.max_radius = max_radius
        self.dots = []          # init list of dots
        self._active = False
        self.col = color
        #print(self.dots)


    # method for activating  the explosion at given x,y
    def activate(self, x, y):
        self._active = True
        self.x = x
        self.y = y
        self.r = 0      # init radius of the explosion (used w self.max_radius)

    # method for getting rid of the explosion
    def deactivate(self):
        self._active = False
        for dot in self.dots:       # iterating though the list of Dots
            self.can.delete(dot.dot)        # deleting each dot using the class's self.dot=creat_oval... (dot dot dot hehehe)

    # getter method for active status
    def is_active(self): 
        return self._active

    # method for adding another layer to each explosion
    def next(self):
        if self._active == True:        # if the explosion is set off...
            self.r += 1             # incrementing the radius
            for i in range(self.num_dots):  # adding (sel.num_dots) number of dots
                theta = random.randint(0,359)/(2*math.pi)   # random angle in radians 0<=theta<2pi
                self.dots.append(Dot(self.can, self.x+self.r*math.cos(theta), self.y+self.r*math.sin(theta), self.col, self._active))   # callind Dot class
            
            if self.r >= self.max_radius: # if the explosion is too big and causing too many casualties     
                self.deactivate()       # we gott call the fire department and get rid of that bad boy

    # method for adding more explosions (both types!)      
    @staticmethod
    def add_explosion(canvas, explosions, x, y, color, type, max_radius=80):
        # cleaning up the list of explosions
        for e in explosions:    # iter through those bad boys
            if e.is_active() == False:      # if it went bye bye...
                explosions.pop(explosions.index(e))     # it cant be in the list anymore!!!
        
        new_e = type(canvas, max_radius, color)       # inits and specifies which explosion class to call
        explosions.append(new_e)      # adding an e to explosions 
        new_e.activate(x,y)     # activating the e


#####################################
####### Supplement 1
#####################################

class Explosion_gravity(Explosion):

    def __init__(self, canvas, max_radius=80, color='rainbow'):
        super().__init__(canvas, max_radius, color)     # calling init of Explosion(...)
        self.theta = np.deg2rad(np.random.choice(359,self.num_dots))       # better way of randomly generating theta...
        self.spd = np.random.choice(-np.arange(1,6),self.num_dots)         # random speed [1,5]

    # method for adding another layer to each explosion
    def next(self):
        if self._active == True:
            g = -0.06        # setting the gravity [i like .1 better.. :(]
            self.r += 1         # incrementing time (as radius is no longer the same for each layer)
            
            #adding the next layer
            for i in range(self.num_dots):      # for each dot...
                x = self.x + self.r*math.cos(self.theta[i])*self.spd[i]     # new x value from given equation
                y = self.y + self.r*math.sin(self.theta[i])*self.spd[i] - self.r**2*g/2     # new y value from given equation
                self.dots.append(Dot(self.can, x, y, self.col, self._active))       # calling the Dot class (self._active can also be True as it will always be true in this loop) 
            
            # calling damage control
            if self.r >= self.max_radius:
                self.deactivate()       # bye bye







        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        #Initialize list of Explosions
        booms=[]
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y, 'rainbow', Explosion_gravity, 30) )
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                print(b.is_active(),end=" ")
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()