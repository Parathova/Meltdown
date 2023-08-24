



import pygame as pyg

WIDTH = 900
HEIGHT = 600
FPS = 60

tab = 0 #count for which tab we are currently on (0-3)
WIN = pyg.display.set_mode((WIDTH, HEIGHT))
pyg.display.set_caption("Meltdown")

# Tab buttons (x, y, width, height)
tab1_rect = pyg.Rect(0, 0.675 * HEIGHT, WIDTH*0.25, HEIGHT/24)
tab2_rect = pyg.Rect(WIDTH*0.25, 0.675 * HEIGHT, WIDTH*0.25, HEIGHT/24)
tab3_rect = pyg.Rect(WIDTH*0.5, 0.675 * HEIGHT, WIDTH*0.25, HEIGHT/24)
tab4_rect = pyg.Rect(WIDTH*0.75, 0.675 * HEIGHT, WIDTH*0.25, HEIGHT/24)


def imgImport(name, w, h, rot=0):
    return pyg.transform.rotate(pyg.transform.scale(pyg.image.load("assets/img/" + name), (w, h)), rot)

BACKIMG = imgImport("background_img.png", WIDTH, HEIGHT)
WORLD = imgImport("world.png", int(WIDTH*0.8), int(HEIGHT*0.58))
TAB1 = imgImport("tab1.png", WIDTH, 0.35*HEIGHT)
TAB2 = imgImport("tab2.png", WIDTH, 0.35*HEIGHT)
TAB3 = imgImport("tab3.png", WIDTH, 0.35*HEIGHT)
TAB4 = imgImport("tab4.png", WIDTH, 0.35*HEIGHT)

def draw():
    
    #WIN.fill((0, 0, 0))
    WIN.blit(BACKIMG, (0, 0)) #putting images at coordinates (origin top left)
    WIN.blit(WORLD, (WIDTH*0.08, HEIGHT*0.05))
    
    """ pyg.draw.rect(WIN, (50, 50, 50), tab1_rect)
    pyg.draw.rect(WIN, (100, 100, 100), tab2_rect)
    pyg.draw.rect(WIN, (150, 150, 150), tab3_rect)
    pyg.draw.rect(WIN, (200, 200, 200), tab4_rect) """

    #tabs
    match tab:
        case 0:
            WIN.blit(TAB1, (0, HEIGHT*0.65))

            #print("1")
        case 1:
            WIN.blit(TAB2, (0, HEIGHT*0.65))
        
        case 2:
            WIN.blit(TAB3, (0, HEIGHT*0.65))
        
        case 3:
            WIN.blit(TAB4, (0, HEIGHT*0.65))
            


    pyg.display.update()

def main():
    global tab
    clock = pyg.time.Clock() #controlls fps and whatnot
    pyg.mouse.set_cursor(pyg.cursors.diamond)

    run = True
    # game loop. this will be active to run the game
    while run:
        clock.tick(FPS) #again, controls fps 
        
        for event in pyg.event.get():
            if event.type == pyg.QUIT: run = False

            if event.type == pyg.MOUSEBUTTONDOWN:
                if event.button == 1: #left/primary click
                    mx, my = pyg.mouse.get_pos()
                    if tab1_rect.collidepoint(mx, my) and tab != 0:
                        print("clicked1")
                        tab = 0
                        print(tab)

                    elif tab2_rect.collidepoint(mx, my) and tab != 1:
                        print("clicked2")
                        tab = 1
                        print(tab)
                    
                    elif tab3_rect.collidepoint(mx, my) and tab != 2:
                        print("clicked3")
                        tab = 2
                        print(tab)
                    
                    elif tab4_rect.collidepoint(mx, my) and tab != 3:
                        print("clicked4")
                        tab = 3
                        print(tab)

        keys_pressed = pyg.key.get_pressed()
        

        print(tab)

        draw()
        #updates display. display wont change if this isnt here
        pyg.display.update()
    pyg.quit()

# dont touch this; if u have question abt it dm jaden
if __name__ == "__main__":
    main()