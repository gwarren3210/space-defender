from tkinter import *
import math
import time, random

class Alien:
    ### to complete
    # refer to explosion/missile for missing comments on methods

    # constructor
    def __init__(self, canvas, inc=4, color='yellow', width=50,height=50, point=1):
        self.can = canvas
        self.inc = inc
        self.col = color
        self.w = width
        self.h = height
        self.p = point
        self._active = False

    # method for activating alien (overriden by all child classes)
    def activate(self, x=None,y=None):
        # var to help clean up drawing expression
        self.dx = self.w/2
        self.dy = self.h/2
        self._active = True
        if x==None or y==None:      # if x,y aren't given
            self.x = random.randint(0, self.can.winfo_width())      # random x
            self.y = -self.dy       # top of canvas
        else:           # given x,y
            self.x = x
            self.y = y

        # drawing yellow boxed alien
        self.al= self.can.create_rectangle(self.x+self.dx,self.y+self.dy, self.x-self.dx,self.y-self.dy, fill='yellow') 
        
    def is_active(self):
        return self._active

    def deactivate(self):
        self._active = False
        self.can.delete(self.al)    # erasing alien off canvas

    def next(self):
        if self._active == True:
            self.can.move(self.al, 0, self.inc)
            self.y += self.inc
            if self.y == self.can.winfo_height()+self.dy:   # if alien reaches the bottom of the screen
                self.deactivate()

    # method for finding if the alien is shot returns True or False
    def is_shot(self, x,y):
        if (self.x-self.dx)<x<(self.x+self.dx) and (self.y-self.dy)<y<(self.y+self.dy):     # outlining the box around the alien
            return True
        else:
            return False

    @staticmethod
    def add_alien(canvas, aliens):
        # same logic as in explosion/missile
        for a in aliens:
            if a.is_active() == False:
                aliens.pop(aliens.index(a))

        # adding a random type of alien to the list of aliens (multiple of the same type to increase odds of being called)
        new_al = random.choice([Alien_red(canvas),Alien_red(canvas),Alien_red(canvas), Alien_green(canvas),Alien_green(canvas), Alien_blue(canvas),Alien_blue(canvas), Alien_mine(canvas)])
        aliens.append(new_al)



################################################################
################################################################

class Alien_red(Alien):
    def __init__(self,c):
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        # contstructor to complete
        super().__init__(c, 4, 'red', width, height, 2)     #  calling constructor of parent class

    # to complete

    # method for activating all aliens (same as parent class with a different image)
    def activate(self, x=None, y=None):
        self.dx = self.w/2
        self.dy = self.h/2
        self._active = True
        if x==None or y==None:
            self.x = random.randint(0, self.can.winfo_width())
            self.y = -self.dy
        else:
            self.x = x
            self.y = y
        self.al = self.can.create_image(self.x, self.y, anchor=CENTER, image=self.image)
        


###############################################################
###############################################################

class Alien_green(Alien_red):

    # to complete
    def __init__(self, c):
        self.image=PhotoImage(file="alien_green.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        Alien.__init__(self, c, 4, 'green', width, height, 4)       # calling grandparent constructor

    # method for green alien movement
    def next(self):
        # if active...
        if self._active == True:
            if self.x-5<0:      # if alien reaches left edge
                x = random.randint(0,5)     # only shift right
            elif self.x+5>self.can.winfo_width():       # if alien reaches right edge
                x = random.randint(-5,0)        # only shift left
            else:
                x = random.randint(-5,5)       # shift direction doesnt matter
        
            # moving the alien and adjusting x and y
            self.can.move(self.al, x, self.inc)
            self.y += self.inc
            self.x += x
            
            # deactivating if it reaches the bottom of the screen
            if self.y == self.can.winfo_height()+self.dy:
                self.deactivate()


###############################################################
###############################################################
                


class Alien_blue(Alien_red):


    # to complete
    def __init__(self, c):
        self.image=PhotoImage(file="alien_blue.png")  # keep a reference (avoid garbage collector)
        self.w=self.image.width()
        height=self.image.height()
        self.rad = math.pi*random.randint(-160,-20)/180     # random radian with constraints
        Alien.__init__(self, c, 4, 'blue', self.w, height, 3)   # calling grandparent constructor
        
    # method fot blue alien movement
    def next(self):
        # if active...
        if self._active == True:
            if self.x-self.w/2<0:   # if it hits left edge
                self.rad = math.pi-self.rad     # change direction
            elif self.x+self.w/2>self.can.winfo_width():      # if it hits right edge
                self.rad = -math.pi-self.rad        # change directions

            # moving alien and updating x and y
            self.can.move(self.al, self.inc*math.cos(self.rad), -self.inc*math.sin(self.rad))
            self.y -= self.inc*math.sin(self.rad)
            self.x += self.inc*math.cos(self.rad)

            
            # deactivating if it reaches the bottom of the screen
            if self.y == self.can.winfo_height()+self.dy:
                self.deactivate()




###############################################################
###############################################################
                


class Alien_mine(Alien_red):
    def __init__(self, c):
        self.image=PhotoImage(file="alien_ship.png").subsample(2,2)  # keep a reference (avoid garbage collector)
        self.w=self.image.width()
        self.count = 0
        height=self.image.height()
        self.rad = math.pi*random.randint(-130,-50)/180             # random angle
        Alien.__init__(self, c, 7, 'gray', self.w, height, 5)       # calling grandparent constructor

    # method for mocing alien (to clean up code)
    def move(self, rad):
            self.can.move(self.al, self.inc*math.cos(rad), -self.inc*math.sin(rad))
            self.y -= self.inc*math.sin(rad)
            self.x += self.inc*math.cos(rad)   

    def next(self):
        first = 35

        # if active...
        if self._active == True:
            
            self.count += 1     # counter for directional changes
            if 0<=self.count%50 and self.count%50<first:        # 35/50 it will go
                #print("down")
                self.rad = -abs(self.rad)
                self.move(self.rad)
            elif first<=self.count%50 and self.count%50<49:     # 15/50 it will go
                #print('up')
                self.rad = abs(self.rad)
                self.move(self.rad)

            # changes direction if it hits the wall
            if self.x-self.w/2<0 or self.x+self.w/2>self.can.winfo_width():
                self.rad = -math.pi-self.rad

            # deactivating if it reaches the bottom of the screen
            if self.y >= self.can.winfo_height():
                self.deactivate()




###############################################################
################################################################
def shoot(alien,x,y):
    if alien.is_shot(x,y):
        result="hit!"
    else:
        result="miss!"


    
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (neede to capture w and h for canvas)
        

        #Initialize alien
        #alien=Alien(canvas)
        #alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        #alien=Alien_blue(canvas)
        alien=Alien_mine(canvas)

        alien.activate()
        

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(alien,e.x,e.y))

        
        ############################################
        ####### start simulation
        ############################################
        #t=0               # time clock
        while True:

            if (not alien.is_active()):
                alien.activate()
              
            alien.next() # next time step
                    
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

