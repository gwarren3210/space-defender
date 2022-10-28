from msilib.schema import PatchPackage
from tkinter import *

class Counter:


    # to complete
    # constructor
    def __init__(self, canvas, initial_value=0, lives=None):
        self.can = canvas
        self.png=PhotoImage(file="ship.png").subsample(3,3)         # making image smaller
        self.v = initial_value
        self.l = lives
        
        # if counter is the score
        if self.v != None:
            self.disp = self.can.create_text(self.can.winfo_width()-50, 20, text=str(self.v), font=('Courier','20'), fill='orange')
        
        # if the counter is the lives
        elif self.l!=None:
            self.disp=[]    # array of ship (lives) showing
            for i in range(self.l):
                self.disp.append(self.can.create_image((self.png.width()*(i+1)+5),10,anchor=NE,image=self.png))

    def increment(self, increment):
        self.v += increment     # adding to the counter by the inc
        self.can.itemconfig(self.disp, text=str(self.v))        # changing number shown
        
    def life_lost(self):
        if len(self.disp)>0:                    # if lives can be taken away...
            self.can.delete(self.disp[-1])      # deletes from the end of the array
            self.disp.pop(-1)                   # deletes an image of the ship
            self.l -= 1                         # takes a life away
    
        

#########################




def main(): 



    # to complete
        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=500,500
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic

        # init score counter right is +1 left is -1
        num = Counter(canvas, 10)
        root.bind("<Right>",lambda e:num.increment(1))
        root.bind("<Left>",lambda e:num.increment(-1))

        # init life counter down is losing a life
        mini_ship = Counter(canvas, None, 3)
        root.bind("<Down>",lambda e:mini_ship.life_lost())

        root.mainloop() # wait until the window is closed




if __name__=="__main__":
    main()



        
