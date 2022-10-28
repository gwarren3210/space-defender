from tkinter import *

class SpaceShip:
    # constructor
    def __init__(self, canvas):
        self.can = canvas
        self.spd = 15
        self.image=PhotoImage(file="ship.png")
        self.x = self.can.winfo_width()/2
        self.y = self.can.winfo_height() - (30+self.image.height())
        #self.ship = self.can.create_image(self.x, self.y, anchor=CENTER, image=self.image)
        self.__active = False

    def activate(self):
        self.__active = True
        self.ship = self.can.create_image(self.x, self.y, anchor=CENTER, image=self.image)  # not in init bc the same ship needs to appear/disappear
    def deactivate(self):
        self.__active = False
    def is_active(self):
        return self.__active

    # moving the ship right/left
    def shift_right(self):
        if self.__active==True:
            room_left = self.can.winfo_width()-self.x-self.image.width()/2      # space between ship and right edge
            if room_left>self.spd:      # if theres room left
                self.can.move(self.ship, self.spd, 0)
                self.x += self.spd
            else:       # if there's no room left
                self.can.move(self.ship, room_left, 0)
                self.x += room_left
    def shift_left(self):
        if self.__active==True:
            room_left = self.x-self.image.width()/2     # space between ship and left edge
            if room_left>self.spd:      # if there is room left
                self.can.move(self.ship, -self.spd, 0)
                self.x -= self.spd
            else:   # if there's no room left
                self.can.move(self.ship, -room_left, 0)
                self.x -= room_left
    # same logic as other is shot methods
    def is_shot(self,x,y):
        self.dx = self.image.width()/2
        self.dy = self.image.height()/2
        if (self.x-self.dx)<x<(self.x+self.dx) and (self.y-self.dy)<y<(self.y+self.dy):
            return True
        else:
            return False
        


def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate()
    
    
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())

    root.mainloop() # wait until the window is closed
    

if __name__=="__main__":
    main()

