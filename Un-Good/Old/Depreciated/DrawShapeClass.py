## DrawShapeClass

import random, pygame       ## imports random module and pygame module

pygame.init()       ## initiates pygame module

class BuildingTemplate:     ## opens class
    def __init__(self, screen):     ## establishes variables
        self.x = 0
        self.y = 0
        self.colorIn = (0, 0, 0)
        self.colorOut = (0, 0, 0)
        self.screen = screen
        self.xStore = 0
        self.yStore = 0
        self.directionArray = []
        self.dirChoiceStore = []
        self.u = 0      ## this value and self.j are testing flags to see when a shape goes out of bounds or has to chose a different direction
        self.j = 0
        self.colorRand = (0, 0, 0)
        self.OutSize = 10
        self.InSize = 8
        
    def getScreen(self):        
        return True     

    def getCoorXOrigin(self):           ## generates a random x coordinate for the origin rectangle
        self.x = random.randrange(0, 1356, self.OutSize)
        self.xStore = self.x
        return (self.x)

    def getCoorYOrigin(self):
        self.y = random.randrange(0, 720, self.OutSize)          ## generates a random y coordinate for the origin rectanle
        self.yStore = self.y
        return (self.y)

    def getColors(self):            ## establishes the colours to be used by rectangles
        self.colorIn = (211, 211, 211)
        self.colorOut = (15, 5, 15)
        return (self.colorIn, self.colorOut)

    def drawTemplate(self):         ## draws the origin rectangle
        pygame.draw.rect(self.screen, self.colorOut, pygame.Rect(self.xStore-1, self.yStore-1, self.OutSize, self.OutSize))
        pygame.draw.rect(self.screen, self.colorIn, pygame.Rect(self.xStore, self.yStore, self.InSize, self.InSize))

    def directChoice(self):         ## chooses a direction for the subsequent rectangle to be drawn to
        self.directionArray = ['up','down','left','right']


        
        self.dirChoice = random.choice(self.directionArray)
        if self.dirChoice == 'up' and self.dirChoiceStore != 'up':      ##as long as the new direction isnt the same as the last one
            #self.xStore = self.xStore
            self.yStore = self.yStore - self.OutSize      ## moves the y coordinate a square up
            #xStoreDSS = self.xStore
            #yStoreDSS = self.yStore
            if self.xStore <= 0 or self.xStore >= 1356 or self.yStore <= 0 or self.yStore >= 720:
                self.xStore = random.randrange(0, 1356, self.OutSize)      ## checks to see if the new coordinates are within the window
                self.yStore = random.randrange(0,720,self.OutSize)       ## if they arent it randomly generates a new building within the window (becomes a new origin rectangle)
                self.u += 1
                print("out-of-bounds",self.u)
                xStoreDSS = self.xStore
                yStoreDSS = self.yStore
                
            else:       ## if everything else is fine just draw the building where it should be
                pygame.draw.rect(self.screen, self.colorOut, pygame.Rect(self.xStore-1, self.yStore-1, self.OutSize, self.OutSize))
                pygame.draw.rect(self.screen, self.colorIn, pygame.Rect(self.xStore, self.yStore, self.InSize, self.InSize))
                self.dirChoiceStore = 'up'      ## set the last used direction to up
                xStoreDSS = self.xStore
                yStoreDSS = self.yStore
        elif self.dirChoice == 'up' and self.dirChoiceStore == 'up':        ## if the last direction was up chose a new direction at random from the list
            self.dirChoice = random.choice(self.directionArray)
            self.j += 1
            print(self.j,"new choice made going",self.dirChoice)



        ## this is repeated for the other three directions (down, left, right),        



        if self.dirChoice == 'down' and self.dirChoiceStore != 'down':
            self.xStore = self.xStore
            self.yStore = self.yStore + self.OutSize
            xStoreDSS = self.xStore
            yStoreDSS = self.yStore
            if self.xStore <= 0 or self.xStore >= 1356 or self.yStore <= 0 or self.yStore >= 720:
                self.xStore = random.randrange(0, 1356, self.OutSize)
                self.yStore = random.randrange(0,720, self.OutSize)
                xStoreDSS = self.xStore
                yStoreDSS = self.yStore
                self.u += 1
                print("out-of-bounds",self.u)
            else:
                pygame.draw.rect(self.screen, self.colorOut, pygame.Rect(self.xStore-1, self.yStore-1, self.OutSize, self.OutSize))
                pygame.draw.rect(self.screen, self.colorIn, pygame.Rect(self.xStore, self.yStore, self.InSize, self.InSize))
                xStoreDSS = self.xStore
                yStoreDSS = self.yStore
                self.dirChoiceStore = 'down'
        elif self.dirChoice == 'down' and self.dirChoiceStore == 'down':
            self.dirChoice = random.choice(self.directionArray)
            self.j += 1
            print(self.j,"new choice made going",self.dirChoice)
            self.dirChoiceStore = self.dirChoice



                
            
        if self.dirChoice == 'left' and self.dirChoiceStore != 'left':
            self.xStore = self.xStore - self.OutSize
            self.yStore = self.yStore
            xStoreDSS = self.xStore
            yStoreDSS = self.yStore

            if self.xStore <= 0 or self.xStore >= 1356 or self.yStore <= 0 or self.yStore >= 720:
                self.xStore = random.randrange(0,1356,self.OutSize)
                self.yStore = random.randrange(0,720,self.OutSize)
                xStoreDSS = self.xStore
                yStoreDSS = self.yStore
                self.u += 1
                print("out-of-bounds",self.u)
            else:
                pygame.draw.rect(self.screen, self.colorOut, pygame.Rect(self.xStore-1, self.yStore-1, self.OutSize, self.OutSize))
                pygame.draw.rect(self.screen, self.colorIn, pygame.Rect(self.xStore, self.yStore, self.InSize, self.InSize))
                self.dirChoiceStore = 'left'
                xStoreDSS = self.xStore
                yStoreDSS = self.yStore
        elif self.dirChoice == 'left' and self.dirChoiceStore == 'left':
            self.dirChoice = random.choice(self.directionArray)
            self.j += 1
            print(self.j,"new choice made going",self.dirChoice)
            self.dirChoiceStore = self.dirChoice


            
            
                
        if self.dirChoice == 'right' and self.dirChoiceStore != 'right':
            self.xStore = self.xStore + self.OutSize
            self.yStore = self.yStore
            xStoreDSS = self.xStore
            yStoreDSS = self.yStore

            if self.xStore <= 0 or self.xStore >= 1356 or self.yStore <= 0 or self.yStore >= 720:
                self.xStore = random.randrange(0,1356,self.OutSize)
                self.yStore = random.randrange(0,720,self.OutSize)
                xStoreDSS = self.xStore
                yStoreDSS = self.yStore
                self.u += 1
                print("out-of-bounds",self.u)
            else:
                pygame.draw.rect(self.screen, self.colorOut, pygame.Rect(self.xStore-1, self.yStore-1, self.OutSize, self.OutSize))
                pygame.draw.rect(self.screen, self.colorIn, pygame.Rect(self.xStore, self.yStore, self.InSize, self.InSize))
                self.dirChoiceStore = 'right'
                xStoreDSS = self.xStore
                yStoreDSS = self.yStore
        elif self.dirChoice == 'right' and self.dirChoiceStore == 'right':
            self.dirChoice = random.choice(self.directionArray)
            self.j += 1
            print(self.j,"new choice made going",self.dirChoice)
            self.dirChoiceStore = self.dirChoice
