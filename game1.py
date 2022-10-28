import re
from tkinter import *
import time
from winreg import REG_QWORD

from numpy import record
from Explosion import Explosion
from Counter import Counter
from Alien import *


########## global variable
game_over=False

######### Functions

def stop_game():
    global game_over
    game_over=True
    
def shoot(canvas, aliens, booms, counter, rec, x,y):
    ####### to complete
    temp=0
    for a in aliens:
        if a.is_shot(x,y)==True and a.is_active()==True:
            temp+=1
            counter.increment(a.p)
            a.deactivate()
            Explosion.add_explosion(canvas, booms, x,y, a.col, Explosion, 30)
            rec[str(a.col)] += 1
    if temp==0:
            Explosion.add_explosion(canvas, booms, x,y, 'white', Explosion, 30)
            counter.increment(-3)


################
    
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space1.png")
        #my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas)
        
        
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Aliens
        aliens=[]
        #Initialize counter ammunition
        amunition=Counter(canvas,10)

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(canvas,aliens,booms,amunition,rec, e.x,e.y))
        root.bind("<Escape>",lambda e:stop_game())

        
        ############################################
        ####### start simulation
        ############################################

        # init stat var
        rec = {'red':0, 'green':0, 'blue':0, 'gray':0}      # init dictionary of aliens shot
        rec_list = []               # init list of tuples to export as .txt file


        #To complete (time sleep is 0.01s)
        t=0     # init time
        while game_over==False:
            
            # adding alien every .5 seconds
            if t%50 == 10:
                Alien.add_alien(canvas, aliens)
                aliens[-1].activate()

            # updating aliens shot every second (tuple of numbers added to a list)
            if t%100 == 0:
                rec_list.append((rec['red'], rec['green'], rec['blue'], rec['gray']))

            # making the aliens and explosins alive
            for a in aliens:
                a.next()
            for b in booms:
                b.next()

            # stopping game if run out of bullets
            if amunition.v <= 0:
                stop_game()

            # update the graphic and wait time
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t+=1      # increment time

        # if the game is over
        if game_over==True:
            print(rec)  # print record of aliens shot
            
            # writing text file
            f = open("game1.txt", 'w')
            for rec in rec_list:
                for num in rec:
                    f.writelines(str(num)+' ')
                f.writelines('\n')
            f.close()
            
            # writing "game over" in the middle of the screen
            canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, text='GAME OVER', font=('Courier','25'), fill='orange')
           
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()