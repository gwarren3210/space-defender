########################
## Team Members
## Name1: Gavriel Warren
## Name2: Dominick Silva
#########################

from tkinter import *
import random


class Dot:
    ##### TO COMPLETE
    
    def __init__(self, canvas, x, y, color, boolean=False):
        if boolean == True:     # if the dot method should be activated
            self.x = x          # init x
            self.y = y          # init y
        if color == "rainbow":  # defining ranbow
            colors = ['red', 'green', 'blue', 'yellow', 'white', 'orange', 'purple']        # choice of colors for rainbow
            self.color = random.choice(colors)                                              # randomly choosing a color from the list
        else:
            self.color = color      # if rainbow isn't selected make the dot the preselected color
        self.dot = canvas.create_oval(self.x-1,self.y-1,self.x+1,self.y+1,fill=self.color, outline="")      # init the dot to the class (need in order to delete dot later)
        
        # only printing x,y and color under Dot.py so it doesnt clutter other programs
        if __name__=="__main__":
            print(self.x, self.y, self.color)











        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Dot(canvas,e.x,e.y,"rainbow",True))
        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

