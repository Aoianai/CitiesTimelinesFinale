## CitiesTimelinesBase

"""
> Creates a building object with attributes like the top left corner
> this will make it easier to store the position of each individual building (as they will be seperate)
> and also allow for size increases while reducing the overall lines of code
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
> comments starting with ## are an explanation
> comments starting with #! denote lines with errors or are notes on what to do next/how to fix an area
> comments starting with #  are lines of code which are being excluded for any reason
"""

## imports the needed modules ##

import pygame, random, sqlite3, sys, time

## lays out various variables for the thing ##

WID = 1000                              ## window width
HIG = 720                               ## window height

b_w = 93                                ## button width
b_h = 57                                ## button height

screen = pygame.display.set_mode((WID,HIG))     ## draws the window
BG = (255,255,255)                              ## sets a background colour
screen.fill(BG)                                 ## fills the window with the background colour

pygame.display.flip()
clock = pygame.time.Clock()                     ## calls pygame's clock function

image_lev_one = pygame.image.load("lev_one.png")        ## loads the image for each building level
image_lev_two = pygame.image.load("lev_two.png")
image_lev_three = pygame.image.load("lev_three.png")
image_lev_four = pygame.image.load("lev_four.png")
image_lev_five = pygame.image.load("lev_five.png")

bg_play = pygame.image.load("bg_play.png").convert_alpha()
bg_pause = pygame.image.load("bg_pause.png").convert_alpha()
bg_blank = pygame.image.load("bg_blank.png").convert_alpha()

rect = pygame.Rect(0, 0, 1000, 720)
screen.blit(bg_play, (0, 0))

pygame.display.flip()

file_name = "coordinates.db"        ## sets the filename for the database

level = 0                           ## sets counter values to zero

## MOVED TO INDIVIDUAL CLASS FILES - KEPT HERE IN CASE - NEED TO CALL PYTHON FILES AND PUT IN THE RIGHT PLACES ##

## the class for the buildings ##
##
##class BuildObject(pygame.sprite.Sprite):
##    """Class to hold Building sprite properties"""
##
##    def __init__(self,x,y,image, size):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = image
##        self.rect = self.image.get_rect()
##        self.rect.x = x
##        self.rect.y = y
##        self.size = size
##        
##    def buildRect(self,x,y,image,size):
##        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.size, self.size)     ## establishes the square for the building
##        print("COORDINATES:", self.rect.x,self.rect.y)      ## returns the coordinates to the shell
##            
##    def blitRect(self,x,y,image,size):
##        screen.blit(image, (self.rect.x, self.rect.y))      ## refreshes the area of the screen where the square is so that it appears
##
##    def checkCollision(self, rect):
##        return self.rect.colliderect(sprite.rect)
##
#### class for the button image atleast ##
##
##class buttonUI(pygame.sprite.Sprite):
##
##    def __init__(self,bg_blank, bg_pause, bg_play, WID, HIG):
##        pygame.sprite.Sprite.__init__(self)
##        self.bg_play = bg_play
##        self.bg_pause = bg_pause
##        self.bg_blank = bg_blank
##        self.rect = self.bg_blank.get_rect()
##        self.rect.x = 0
##        self.rect.y = 0
##        self.wid = WID
##        self.hig = HIG
##
##    def drawPlay(self):
##        self.rect = self.bg_play.get_rect()
##        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.wid, self.hig)
##        screen.blit(self.bg_play, (self.rect.x, self.rect.y))
##
##    def drawPause(self):
##        self.rect = self.bg_pause.get_rect()
##        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.wid, self.hig)
##        screen.blit(self.bg_pause, (self.rect.x, self.rect.y))
##
##class timeUI():
##
##    def __init__(self):
##        pygame.font.init()          ## start font
##        self.y_date = 1990          ## start year
##        self.m_date = 1             ## start month (jan)
##        self.d_date = 1             ## start day (first)
##        self.d_limit = 32           ## number of days in month (starts in jan so 31 days (count from 0 so 32)
##        self.date_array = []        ## an array to display the date in DrawObjectBuild()
##
##        self.t_font = pygame.font.SysFont('Myriad Pro', 45)
##
##    def timeUpdate(self):
##        time.sleep(0.1)                     ## wait 1ms
##        self.d_date += 1                    ## progress to next day
##        if self.d_date == self.d_limit:     ## if it is the last day of the month
##            self.d_date = 1                 ## reset the date back to the first
##            self.m_date += 1                ## progress to next month
##            if self.m_date == 2:            ## if the month is feb
##                self.d_limit == 29          ## reduce limit to 28 days
##            elif self.d_limit == 32:        ## if the last month had 31 days in
##                self.d_limit = 31           ## the next month has 30 days n
##            elif self.d_limit == 31:        ## if the last month had 30 days in
##                self.d_limit = 32           ## the next month has 31 days in
##                
##            if self.m_date == 12:           ## if the month is dec
##                self.m_date = 1             ## reset month to jan
##                self.y_date += 1            ## progress to next year
##                if self.m_date == 2000:     ## if it reaches year 2K
##                    quit()                  ## stop
##
##    def timeDisplay(self):
##        self.date_array = [str(self.d_date), str(self.m_date), str(self.y_date)]
##        self.t_time = '/'.join(self.date_array)
##        time_sur = self.t_font.render(self.t_time, False, (0,0,0))
##        screen.blit(time_sur, (850, 12))
##
##
##
## this bit initialises SQLITE3 and deletes the database if it already exists ##

db = sqlite3.connect(file_name)                 ## connects to a database

cursor = db.cursor()

try:                                            ## tries to insert data into the database
    cursor.execute('''INSERT INTO coordinates(x_coor, y_coor, b_level) values(?,?,?)'''(0,0,0))
except:
    cursor.execute('''DROP TABLE coordinates;''')       ## if it can delete the table (thats what it is supposed to do anyway)

    
cursor.execute('''
CREATE TABLE coordinates(
x_coor INTEGER,
y_coor INTEGER,
b_level INTEGER)
''')
db.commit()                                     ## creates a database called coordnates with 3 values - x_coor, y_coor, and b_level
        
## this is the game loop - it does all the hard work and heavy lifting ##

def main():

    build_count = 0
    col_count = 0
    images = [image_lev_one, image_lev_two, image_lev_three, image_lev_four, image_lev_five]        ## list of images to use
    flag = 0                                        ## different flag value for the game loop

    building_group = pygame.sprite.Group()          ## sets a group of sprites to buildings

    rect = bg_play.get_rect()
    button = pygame.Rect(17, 13, b_w, b_h)

    drawUI =  buttonUI(bg_blank, bg_pause, bg_play, WID, HIG)       ## calls the class for the ui
    drawTime = timeUI()

    #pygame.time.set_timer(pygame.USEREVENT + 1, 100)

    done = False                                    ## flag value for the game loop

    while not done:                                     ## begins game loop
        for event in pygame.event.get():                ## for every event check
            if event.type == pygame.QUIT:               ## if the event is to quit
                pygame.quit()                           ## set flag to true to kill the game loop
                break
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:        ## if a button on the mouse is clicked
                if event.button == 1:                       ## and the button is the left mouse button
                    if button.collidepoint(event.pos):      ## and it is inside the button area
                        flag = 0

                        while flag == 0:                 ## this loop will always run unless broken

                            drawUI.drawPause()
                            drawTime.timeUpdate()
                            drawTime.timeDisplay()
                            pygame.display.flip()
                            clock.tick(60)
                    
                            
                            for event in pygame.event.get():
                                while event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button == 1:
                                        if button.collidepoint(event.pos):
                                            drawUI.drawPlay()
                                            drawTime.timeDisplay()
                                            pygame.display.flip()
                                            clock.tick(60)
                                            flag = 1
                                            print("PAUSE")
                                            print("")
                                            break


                            image = random.choice(images)       ## randomly choose an image from the list above
                            if image == image_lev_one:          ## if it is this image
                                size = 20                       ## set the size of the square
                                level = 1                       ## and the building level
                            if image == image_lev_two:          ## repeat for all building levels
                                size = 40
                                level = 2
                            if image == image_lev_three:
                                size = 60
                                level = 3
                            if image == image_lev_four:
                                size = 80
                                level = 4
                            if image == image_lev_five:
                                size = 100
                                level = 5
                            
                            x = x1 = random.randrange(0,WID,size)       ## generate an x coordinate within the window area
                            y = y1 = random.randrange(0,HIG,size)       ## generate a  y coordinate within the window area

                            build1 = BuildObject(x,y,image,size)        ## draws a first building
                            build1.buildRect(x,y,image,size)
                            build1.blitRect(x,y,image,size)

                            build_group = pygame.sprite.Group()         ## creates a sprite group for buildings
                            build_group.add(build1)                     ## adds the first rectangle to a sprite group

                            x = x2 = random.randrange(0,WID,size)       ## draws a second building
                            y = y2 = random.randrange(0,HIG,size)
                            build2 = BuildObject(x,y,image,size)

#                            for build in build_group:
#
#                                collide = pygame.sprite.spritecollide(build1, build_group, False)        ## runs pygame's inbuild spritecollide module - checking the second sprite against the whole of the sprite group
#
#                                if collide:                                             ## if there is a collision between rectangle sprites
#                                    print("Build1 X and Y:", str(x1), " ", str(y1))     ## print the coordinates of the first sprite
#                                    print("Build2 X and Y:", str(x2), " ", str(y2))     ## print the coordinates of the second sprite
#                                    col_count += 1                                      ## increment the sprite count
#                                    print("Collided")                                   ## print Collided
#                                    break                                               ## replacing a return to the start of the loop so it is easier to notice when it works
#                                    #main()
#                                else:
#                                    build_group.add(build2)
#
#                            print("COLLISIONS:",col_count)                          ## return the collision count (atm should only ever get to a value of 1)
#                            print("")                                               ## leave a blank line.

                            build_count += 1                                                ## increase the value of this flag
                            print("BUILDING NUMBER:", build_count)                          ## print the value as a checkpoint
                            print("")
                            
                            cursor.execute('''INSERT INTO coordinates(x_coor, y_coor, b_level) values(?,?,?)''',(x,y,level))
                            db.commit()             ## write the new values into the database

                            pygame.display.flip()   ## refresh the display so that all the new stuff appears
                            clock.tick(60)          ## set the clock to 60 or increase it by 60 idk
                        
main()
