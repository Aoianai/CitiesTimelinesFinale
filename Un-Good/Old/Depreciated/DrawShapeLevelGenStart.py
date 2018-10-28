## DrawShapeLevelGenStart
"""
## Instead of all buildings starting at level one this code will
## generate some buildings at a level 2 3 4 or 5 at the start instead
## this can be implemented in to the main generation class later when
## the data base has begun to work
"""

import random
import pygame

pygame.init()

class BuildingLevelTemplate:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.colorIn1 = (211, 211, 211)
        self.colorIn2 = (211, 100, 100)
        self.colorIn3 = (100, 211, 100)
        self.colorIn4 = (100, 100, 211)
        self.colorIn5 = (36, 211, 36)
        self.colorOutAll = (15, 5, 15)
        self.directionArray = []
        self.dirChoiceStore = []
        self.u = 0
        self.j = 0
        self.outSize1 = 10
        self.outSize2 = 20
        self.outSize3 = 30
        self.outSize4 = 40
        self.outSize5 = 50
        self.inSize1 = 8
        self.inSize2 = 18
        self.inSize3 = 28
        self.inSize4 = 38
        self.inSize5 = 48
        self.sizeArray = ['1','1','1','1', '2', '2', '2', '3', '3', '4', '5']
        self.sizeChoice = []
        self.sizeChoiceStore = 0
        self.directionArray = ['u', 'd,' 'l', 'r']
        self.dirChoiceStore = []

    def getCoorOriginX(self):
        self.sizeChoice = random.choice(self.sizeArray)
        self.sizeChoiceStore = self.sizeChoice
        if self.sizeChoice == '1':
            self.x = random.randrange(0, 1356, self.outSize1)
            return(self.x)
        elif self.sizeChoice == '2':
            self.x = random.randrange(0, 1356, self.outSize2)
            return(self.x)
        elif self.sizeChoice == '3':
            self.x = random.randrange(0, 1356, self.outSize3)
            return(self.x)
        elif self.sizeChoice == '4':
            self.x = random.randrange(0, 1356, self.outSize4)
            return(self.x)
        elif self.sizeChoice == '5':
            self.x = random.randrange(0, 1356, self.outSize5)
            return(self.x)

    def getCoorOriginY(self):
        if self.sizeChoice == '1':
            self.y = random.randrange(0, 720, self.outSize1)
            return(self.y)
        elif self.sizeChoice == '2':
            self.y = random.randrange(0, 720, self.outSize2)
            return(self.y)
        elif self.sizeChoice == '3':
            self.y = random.randrange(0, 720, self.outSize3)
            return(self.y)
        elif self.sizeChoice == '4':
            self.y = random.randrange(0, 720, self.outSize4)
            return(self.y)
        elif self.sizeChoice == '5':
            self.y = random.randrange(0, 720, self.outSize5)
            return(self.y)

    def drawOrigin(self):
        if self.sizeChoice == '1':
            pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize1, self.outSize1))
            pygame.draw.rect(self.screen, self.colorIn1, pygame.Rect(self.x, self.y, self.inSize1, self.inSize1))
        elif self.sizeChoice == '2':
            pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize2, self.outSize2))
            pygame.draw.rect(self.screen, self.colorIn2, pygame.Rect(self.x, self.y, self.inSize2, self.inSize2))
        elif self.sizeChoice == '3':
            pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize3, self.outSize3))
            pygame.draw.rect(self.screen, self.colorIn3, pygame.Rect(self.x, self.y, self.inSize3, self.inSize3))
        elif self.sizeChoice == '4':
            pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize4, self.outSize4))
            pygame.draw.rect(self.screen, self.colorIn4, pygame.Rect(self.x, self.y, self.inSize4, self.inSize4))
        elif self.sizeChoice == '5':
            pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize5, self.outSize5))
            pygame.draw.rect(self.screen, self.colorIn5, pygame.Rect(self.x, self.y, self.inSize5, self.inSize5))
            
    def directionChoice(self):
        #self.dirChoice = random.choice(self.directionArray)
        self.dirChoice = "d"
        

        if self.dirChoice == 'u' and self.dirChoiceStore != 'u':
            self.sizeChoice = random.choice(self.sizeArray)

            if self.sizeChoice == '1':
                self.x = self.x
                self.y = self.y - self.outSize1
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize1, self.outSize1))
                    pygame.draw.rect(self.screen, self.colorIn1, pygame.Rect(self.x, self.y, self.inSize1, self.inSize1))

            if self.sizeChoice == '2':
                self.x = self.x
                self.y = self.y - self.outSize2
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize2, self.outSize2))
                    pygame.draw.rect(self.screen, self.colorIn2, pygame.Rect(self.x, self.y, self.inSize2, self.inSize2))
            if self.sizeChoice == '3':
                self.x = self.x
                self.y = self.y - self.outSize3
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize3, self.outSize3))
                    pygame.draw.rect(self.screen, self.colorIn3, pygame.Rect(self.x, self.y, self.inSize3, self.inSize3))
            if self.sizeChoice == '4':
                self.x = self.x
                self.y = self.y - self.outSize4
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize4, self.outSize4))
                    pygame.draw.rect(self.screen, self.colorIn4, pygame.Rect(self.x, self.y, self.inSize4, self.inSize4))
            if self.sizeChoice == '5':
                self.x = self.x
                self.y = self.y - self.outSize5
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize5, self.outSize5))
                    pygame.draw.rect(self.screen, self.colorIn5, pygame.Rect(self.x, self.y, self.inSize5, self.inSize5))

        elif self.dirChoice == 'u' and self.dirChoiceStore == 'u':
            self.dirchoice = random.choice(self.directionArray)
            self.j += 1
            print("newdirection",self.j, self.dirChoice)
            
######################################################################################################################################

        if self.dirChoice == 'd' and self.dirChoiceStore != 'd':
            self.sizeChoice = random.choice(self.sizeArray)

            if self.sizeChoice == '1':
                self.x = self.x
                self.y = self.y + self.outSize1
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize1, self.outSize1))
                    pygame.draw.rect(self.screen, self.colorIn1, pygame.Rect(self.x, self.y, self.inSize1, self.inSize1))

            if self.sizeChoice == '2':
                self.x = self.x
                self.y = self.y + self.outSize2
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize2, self.outSize2))
                    pygame.draw.rect(self.screen, self.colorIn2, pygame.Rect(self.x, self.y, self.inSize2, self.inSize2))
            if self.sizeChoice == '3':
                self.x = self.x
                self.y = self.y + self.outSize3
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize3, self.outSize3))
                    pygame.draw.rect(self.screen, self.colorIn3, pygame.Rect(self.x, self.y, self.inSize3, self.inSize3))
            if self.sizeChoice == '4':
                self.x = self.x
                self.y = self.y + self.outSize4
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize4, self.outSize4))
                    pygame.draw.rect(self.screen, self.colorIn4, pygame.Rect(self.x, self.y, self.inSize4, self.inSize4))
            if self.sizeChoice == '5':
                self.x = self.x
                self.y = self.y + self.outSize5
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize5, self.outSize5))
                    pygame.draw.rect(self.screen, self.colorIn5, pygame.Rect(self.x, self.y, self.inSize5, self.inSize5))

        elif self.dirChoice == 'd' and self.dirChoiceStore == 'd':
            self.dirchoice = random.choice(self.directionArray)
            self.j += 1
            print("newdirection",self.j, self.dirChoice)

######################################################################################################################################

        if self.dirChoice == 'l' and self.dirChoiceStore != 'l':
            self.sizeChoice = random.choice(self.sizeArray)

            if self.sizeChoice == '1':
                self.x = self.x - self.outSize1
                self.y = self.y
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize1, self.outSize1))
                    pygame.draw.rect(self.screen, self.colorIn1, pygame.Rect(self.x, self.y, self.inSize1, self.inSize1))

            if self.sizeChoice == '2':
                self.x = self.x - self.outSize2
                self.y = self.y
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize2, self.outSize2))
                    pygame.draw.rect(self.screen, self.colorIn2, pygame.Rect(self.x, self.y, self.inSize2, self.inSize2))
            if self.sizeChoice == '3':
                self.x = self.x - self.outSize3
                self.y = self.y
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize3, self.outSize3))
                    pygame.draw.rect(self.screen, self.colorIn3, pygame.Rect(self.x, self.y, self.inSize3, self.inSize3))
            if self.sizeChoice == '4':
                self.x = self.x - self.outSize4
                self.y = self.y 
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize4, self.outSize4))
                    pygame.draw.rect(self.screen, self.colorIn4, pygame.Rect(self.x, self.y, self.inSize4, self.inSize4))
            if self.sizeChoice == '5':
                self.x = self.x - self.outSize5
                self.y = self.y 
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize5, self.outSize5))
                    pygame.draw.rect(self.screen, self.colorIn5, pygame.Rect(self.x, self.y, self.inSize5, self.inSize5))

        elif self.dirChoice == 'l' and self.dirChoiceStore == 'l':
            self.dirchoice = random.choice(self.directionArray)
            self.j += 1
            print("newdirection",self.j, self.dirChoice)
            
######################################################################################################################################

        if self.dirChoice == 'r' and self.dirChoiceStore != 'r':
            self.sizeChoice = random.choice(self.sizeArray)

            if self.sizeChoice == '1':
                self.x = self.x + self.outSize1
                self.y = self.y
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize1, self.outSize1))
                    pygame.draw.rect(self.screen, self.colorIn1, pygame.Rect(self.x, self.y, self.inSize1, self.inSize1))

            if self.sizeChoice == '2':
                self.x = self.x + self.outSize2
                self.y = self.y
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize2, self.outSize2))
                    pygame.draw.rect(self.screen, self.colorIn2, pygame.Rect(self.x, self.y, self.inSize2, self.inSize2))
            if self.sizeChoice == '3':
                self.x = self.x + self.outSize3
                self.y = self.y
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize3, self.outSize3))
                    pygame.draw.rect(self.screen, self.colorIn3, pygame.Rect(self.x, self.y, self.inSize3, self.inSize3))
            if self.sizeChoice == '4':
                self.x = self.x + self.outSize4
                self.y = self.y 
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize4, self.outSize4))
                    pygame.draw.rect(self.screen, self.colorIn4, pygame.Rect(self.x, self.y, self.inSize4, self.inSize4))
            if self.sizeChoice == '5':
                self.x = self.x + self.outSize5
                self.y = self.y 
                if self.x <= 0 or self.y <=0 or self.x >=1356 or self.y >=720:
                    self.x = random.randrange(0, 1356, self.outSize1)
                    self.y = random.randrange(0, 720, self.outSize1)
                    self.u += 1
                    print("outofbounds",self.u)
                else:
                    pygame.draw.rect(self.screen, self.colorOutAll, pygame.Rect(self.x-1, self.y-1, self.outSize5, self.outSize5))
                    pygame.draw.rect(self.screen, self.colorIn5, pygame.Rect(self.x, self.y, self.inSize5, self.inSize5))

        elif self.dirChoice == 'r' and self.dirChoiceStore == 'r':
            self.dirchoice = random.choice(self.directionArray)
            self.j += 1
            print("newdirection",self.j, self.dirChoice)

######################################################################################################################################
        
            
