from tkinter import *
import time,random
from turtle import update
from Explosion import Explosion
from Missile import Missile

        
       
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        
        my_image=PhotoImage(file="umass_campus.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h) # create a canvas width*height

        canvas.create_image(10,10,anchor=NW,image=my_image)
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Explosions
        booms=[]
        #Initialize list of Missiles
        missiles=[]
        

        
        ############################################
        ####### start simulation
        ############################################
      






        ### To complete
        colors = ['red', 'green', 'blue', 'yellow', 'white', 'orange', 'purple',  'rainbow',  'rainbow',  'rainbow',  'rainbow']                # random list of colors
        t=0             # init time
        while True:
                t += 1  # inc time
                # launching a missile
                if t%25 == 0:         # every .5 seconds...
                        x = random.randint(0,w)         # random x position
                        ceiling = random.randint(h//4, 3*h//4)          # rand ceiling height
                        r = random.randint(100,300)             # random radius
                        #r = random.randint(10,30)               # for testing size
                        Missile.add_missile(canvas, missiles, x, h, ceiling)    # adding missile
                
                # deactivating to boom and calling next method
                for m in missiles:
                        # m to boom
                        if m.ceiling >= m.y:            # if the m reaches ceiling height
                                m.deactivate()                  # bye bye...
                                #print(m.x,",",m.y)
                                col = random.choice(colors)     # random color
                                Explosion.add_explosion(canvas, booms, m.x, m.y, col, Explosion, r)        # but hello boom!!!
                                missiles.pop(missiles.index(m))         # cleaning up missile list
                                #print(m.is_active(), end=" ")          # check if deactivate worked
                        
                        # if it gets here m is active and inc the position
                        m.next()
                
                # calling next layer of each boom
                for b in booms:
                        b.next()
                        #print(b.is_active(), end=" ")          # checking active status

                root.update()
                time.sleep(.02)
                        




        

if __name__=="__main__":
    main()

