from tkinter import *
import time
from Alien import *
from Explosion import Explosion
from SpaceShip import SpaceShip
from Counter import Counter
from Missile import Missile


        
########## global variable
game_over=False

######### Function
def stop_game():
    global game_over
    game_over=True
    

    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)





    #### to complete
    # initializing var
    counter = Counter(canvas, 10)
    lives = Counter(canvas, None, 3)
    t = 0       # init time
    booms = []
    missiles = []
    aliens = []
    ship_boom = []  # seperating explosion for when ship explodes
    rec = {'red':0, 'green':0, 'blue':0, 'gray':0}      # record dictionary
    rec_list = []       # init list of tuples

    
    # instantiatinng and activating the ship
    ship = SpaceShip(canvas)
    ship.activate()
    # Binding key strokes
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())
    #root.bind("<Up>",lambda e:Missile.add_missile(canvas, missiles, ship.x, 0) )
    root.bind("<Up>",lambda e:Missile.add_missile(canvas, missiles, ship.x, ship.y-ship.image.height()/2) )
    root.bind("<Escape>",lambda e:stop_game())

    while game_over==False and lives.l>0:

        # updating aliens shot every second (tuple of numbers added to a list)    
        if t%100==10:
            Alien.add_alien(canvas, aliens)
            aliens[-1].activate()
            rec_list.append((rec['red'], rec['green'], rec['blue'], rec['gray']))

        # making the game alive!!!!
        for b in ship_boom:
            b.next()
        for b in booms:
            b.next()
        for m in missiles:
            m.next()
        for al in aliens:
            al.next()
            
            # checking collision of m and al
            for m in missiles:
                if al.is_shot(m.x,m.y) and m.is_active()==True:
                    rec[str(al.col)] += 1       # adding to record dictionary
                    Explosion.add_explosion(canvas, booms, m.x, m.y, al.col, Explosion, 30)
                    counter.increment(al.p)     # adding score to score counter
                    m.deactivate()          # missile disappears
                    al.deactivate()         # alien disappears
                    aliens.pop(aliens.index(al))        # cleaning list of aliens
            
            # checking if ship is shot
            if ship.is_shot(al.x, al.y) and al.is_active()==True:
                al.deactivate()     # bye bye alien
                Explosion.add_explosion(canvas, ship_boom, ship.x, ship.y, 'white', Explosion, 30)
                ship.deactivate()   # cant shoot
                canvas.delete(ship.ship)     # bye bye ship
                lives.life_lost()       # deleting a life
                if lives.l <= 0:    # ending game if lives are 0
                    stop_game()
            
            # ship explosion
            if len(ship_boom)>0:     # if the list exists..
                if ship_boom[-1].is_active() == False:  # and the explosion isnt active...
                    ship.x = w/2    # init ship in the middle of the screen
                    ship.activate()     # activating ship
                    ship_boom.pop(-1)   # cleaning list
            
            # enabling/disabling shooting if ship is alive/dead
            if ship.is_active()==False:
                root.bind("<Up>",lambda e:None)
            elif ship.is_active()==True:
                root.bind("<Up>",lambda e:Missile.add_missile(canvas, missiles, ship.x, ship.y-ship.image.height()/2) )

        
        #if counter.v <= 0:
        #   game_over=True

        root.update()
        time.sleep(.01)
        t += 1

    if game_over==True:
        print(rec)

        f = open("game2.txt", 'w')
        for rec in rec_list:
            for num in rec:
                f.writelines(str(num)+' ')
            f.writelines('\n')
        f.close()

        while True:
            # finishing the active explosionsto look nice
            for b in ship_boom:
                b.next()

            # wrinting "Game Over" in the middle of the screen (twice to make it pop)
            canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, text='Game Over', font=('Courier','25'),fill='black')
            canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2+5, text='Game Over', font=('Courier','25'),fill='orange')
            ship.deactivate()       # disabling ship movement
            root.bind("<Up>",lambda e:None)     # disabling shooting

            root.update()
            time.sleep(.01)





    root.mainloop() # wait until the window is closed


if __name__=="__main__":
    main()





