## DrawShapeMain

#import DrawShapeClass       ## imports my DrawShapeClass module
#import CheckDB      ## imports my CheckDB module
#import DrawShapeSave

import DrawObjectBuilding

fileName = 'shapes.db'

def SpaceBuild():       ## opens a routine

    import pygame, sys, sqlite3         ##imports the pygame, sys and sqlite3 modules
    
    db = sqlite3.connect(fileName)       ## initialises sqlite

    cursor = db.cursor()        ##creates a cursor for sqlite
    cursor.execute ('''
         DROP TABLE shapes;
    ''')
    cursor.execute ('''
        CREATE TABLE shapes (
        shapeX INTEGER,
        shapeY INTEGER,
        buildL INTEGER)
    ''')        ## deletes an existing table and creates a new one under the same name with 2 values

    done = False        ## sets a flag value to false
    
    screen = pygame.display.set_mode((1356, 720))       ## draws the window, assings to screen
    create = DrawObjectBuilding.BuildingTemplate(screen)    ## initialises BuildingTemplate Class assigns to create
    

    screen.fill((255,255,255)) ## makes the window background colour green


    refresh = pygame.time.Clock()       ## initialises pygame's clock function, assigns to refresh
    pygame.display.flip()       ## flips the display - idk what this pygame command actually does
    refresh.tick(60)        ## refresh the screen 60times per milisecond?
    pygame.event.set_grab(0)

    while not done:     ## while the flag is false
        for event in pygame.event.get():        ## for every event pygame detects
            if event.type == pygame.QUIT:       ## if the event is trying to close the window
                done = True     ## sets flag to true 

            if event.type == pygame.KEYDOWN:        ## if the detected event type is a key press
                if event.key == pygame.K_SPACE:     ## if the key pressed is the space-bar
                    ##
                while event.key == pygame.K_SPACE:
                    ##
                    pygame.display.flip()       ## refresh the screen
                    refresh.tick(60)
                else:           ## if the space key wasnt pressed but another key was
                    print("Key Not Valid")      ## inform user
                
SpaceBuild()        ## run