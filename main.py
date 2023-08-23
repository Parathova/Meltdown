import pygame as pyg

WIDTH = 900
HEIGHT = 600
FPS = 60
WIN = pyg.display.set_mode((WIDTH, HEIGHT))
pyg.display.set_caption("Meltdown")

def imgImport(name, w, h, rot=0):
    return pyg.transform.rotate(pyg.transform.scale(pyg.image.load("assets/img/" + name), (w, h)), rot)

BACKIMG = imgImport("background_img.png", WIDTH, HEIGHT)
WORLD = imgImport("world.png", int(WIDTH*0.8), int(HEIGHT/2))

def draw():
    #WIN.fill((0, 0, 0))
    WIN.blit(BACKIMG, (0, 0)) #putting images at coordinates (origin top left)
    WIN.blit(WORLD, (WIDTH*0.08, HEIGHT*0.05))
    pyg.display.update()

def main():
    clock = pyg.time.Clock() #controlls fps and whatnot

    run = True
    # game loop. this will be active to run the game
    while run:
        clock.tick(FPS) #again, controls fps 
        
        for event in pyg.event.get():
            if event.type == pyg.QUIT: run = False
        
        keys_pressed = pyg.key.get_pressed()
        



        draw()
        #updates display. display wont change if this isnt here
        pyg.display.update()
    pyg.quit()

# dont touch this; if u have question abt it dm jaden
if __name__ == "__main__":
    main()