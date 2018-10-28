## CitiesTimelinesBase

"""
> Creates a building object with attributes like the top left corner
> this will make it easier to store the position of each individual building (as they will be seperate)
> and also allow for size increases while reducing the overall lines of code
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
> comments starting with ## are an explanation
> comments starting with #! denote lines with errors or are notes on what to do next/how to fix an area
> comments starting with #  are lines of code which are being excluded for any reason
> comments starting with #~ are notes on why a line of code is there for no reason
"""

## imports the needed modules ##

import pygame, random, sqlite3, time

## lays out various variables for the thing ##

WID = 1000                              ## window width
HIG = 720                               ## window height

b_w = 93                                ## button width
b_h = 57                                ## button height

screen = pygame.display.set_mode((WID,HIG))     ## draws the window
BG = (39,95,42)                              ## sets a background colour
screen.fill(BG)                                 ## fills the window with the background colour

pygame.display.flip()
clock = pygame.time.Clock()                     ## calls pygame's clock function

image_lev_one = pygame.image.load("lev_one.png")        ## loads the image for each buildin level
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

file_name = "coordb.db"        ## sets the filename for the database

db = sqlite3.connect(file_name)
cursor = db.cursor()

level = 0                           ## sets counter values to zero

## the class for the buildings ##

class BuildObject(pygame.sprite.Sprite):
    """Class to hold Building sprite properties"""

    def __init__(self,x,y,image, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = size

    def buildRect(self,x,y,image,size):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.size, self.size)     ## establishes the square for the building
        print("COORDINATES:", self.rect.x,self.rect.y)      ## returns the coordinates to the shell

    def blitRect(self,x,y,image,size):
        screen.blit(image, (self.rect.x, self.rect.y))      ## refreshes the area of the screen where the square is so that it appears

    def checkCollision(self, rect):
        return self.rect.colliderect(sprite.rect)

## class for the button image atleast ##

class buttonUI(pygame.sprite.Sprite):

    def __init__(self, bg_blank, bg_pause, bg_play, WID, HIG):
        pygame.sprite.Sprite.__init__(self)
        self.bg_play = bg_play
        self.bg_pause = bg_pause
        self.bg_blank = bg_blank
        self.rect = self.bg_blank.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.wid = WID
        self.hig = HIG

    def drawPlay(self):
        self.rect = self.bg_play.get_rect()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.wid, self.hig)
        screen.blit(self.bg_play, (self.rect.x, self.rect.y))

    def drawPause(self):
        self.rect = self.bg_pause.get_rect()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.wid, self.hig)
        screen.blit(self.bg_pause, (self.rect.x, self.rect.y))

class timeUI():

    def __init__(self):
        pygame.font.init()          ## start font
        self.y_date = 1990          ## start year
        self.m_date = 1             ## start month (jan)
        self.d_date = 1             ## start day (first)
        self.d_limit = 32           ## number of days in month (starts in jan so 31 days (count from 0 so 32)
        self.base_time = 0
        self.date_array = []        ## an array to display the date in DrawObjectBuild()

        self.t_font = pygame.font.SysFont('Myriad Pro', 45)

    def timeUpdate(self):
        time.sleep(0.1)                     ## wait 1ms
        self.d_date += 1                    ## progress to next day
        self.base_time += 1                 ## this is a base time unit which buildings will refer to instead of the date
        if self.d_date == self.d_limit:     ## if it is the last day of the month
            self.d_date = 1                 ## reset the date back to the first
            self.m_date += 1                ## progress to next month
            if self.m_date == 2:            ## if the month is feb
                self.d_limit == 29          ## reduce limit to 28 days
            elif self.d_limit == 32:        ## if the last month had 31 days in
                self.d_limit = 31           ## the next month has 30 days n
            elif self.d_limit == 31:        ## if the last month had 30 days in
                self.d_limit = 32           ## the next month has 31 days in

            if self.m_date == 12:           ## if the month is dec
                self.m_date = 1             ## reset month to jan
                self.y_date += 1            ## progress to next year
                if self.m_date == 2000:     ## if it reaches yb2K
                    quit()                  ## stop

    def timeDisplay(self):
        self.date_array = [str(self.d_date), str(self.m_date), str(self.y_date)]
        self.t_time = '/'.join(self.date_array)
        time_sur = self.t_font.render(self.t_time, False, (0,0,0))
        screen.blit(time_sur, (850, 12))

    def saveDate(self):
        print(self.t_time)

## a class which creates the database and

class updateData():

    def __init__(self, x, y, size, level, next_level_time, base_time):
        self.x_coor = x
        self.y_coor = y
        self.b_size = size
        self.b_level = level
        self.next_level_time = next_level_time

        self.base_time = base_time

        self.build_array = []
        self.build_string = ""

        self.n = 0
        self.nc = 0
        self.file = open("coordinates.log","w")
        self.value = 1
        self.base_time = int(self.base_time)
        self.increase_time = 0
        self.increase_level = 0

        self.image_array = [image_lev_one, image_lev_two, image_lev_three, image_lev_four, image_lev_five]  ## list of images to use
        self.size = 0



    def create_table(self):
        try:                                            ## tries to insert data into the database
            cursor.execute('''INSERT INTO coordb(x_coor, y_coor, b_level) values(?,?,?)'''(0,0,0))
        except:
            cursor.execute('''DROP TABLE coordb;''')
        cursor.execute('''
        CREATE TABLE coordb(
        b_id INTEGER PRIMARY KEY,
        x_coor INTEGER,
        y_coor INTEGER,
        b_size INTEGER,
        b_level INTEGER,
        next_level_time INTEGER)
        ''')
        db.commit()

    def write_table(self, x, y, size, level, next_level_time, base_time):
        cursor.execute('''INSERT INTO coordb(x_coor, y_coor, b_size, b_level, next_level_time) values(?,?,?,?,?)''', (self.x_coor, self.y_coor, self.b_size, self.b_level, self.next_level_time))
        db.commit()

    def parse_table(self):
        #while self.nc <= self.n:
        cursor.execute("SELECT * FROM coordb")
        data = cursor.fetchall()

        for row in data:
            #print("x",row[0])
            #print("xx",row[4])
            #print("xxx",row[5])
            self.increase_level = (row[4] + 1)
            self.increase_time = (self.base_time + 20)
            self.bu_id = row[0]
            self.next_level_time = row[5]

            if self.next_level_time == self.base_time and row[4] < 5:
                self.base_time = int(self.base_time)
                self.increase_level = int(self.increase_level)
                self.increase_time = int(self.increase_time)

                if self.increase_level == 2:  ## repeat for all building levels
                    self.size = 40
                    self.image = self.image_array[1]
                if self.increase_level == 3:
                    self.size = 60
                    self.image = self.image_array[2]
                if self.increase_level == 4:
                    self.size = 80
                    self.image = self.image_array[3]
                if self.increase_level == 5:
                    self.size = 100
                    self.image = self.image_array[4]

                cursor.execute('''UPDATE coordb SET b_size = ?, b_level = ?, next_level_time = ? WHERE b_id = ? AND next_level_time = ?''', (self.size, self.increase_level, self.increase_time, self.bu_id, self.base_time))

                x = row[1]
                y = row[2]

                build = BuildObject(x,y,self.image,self.size)
                build.buildRect(x, y, self.image, self.size)
                build.blitRect(x, y, self.image, self.size)

## this is the game loop - it does all the hard work and heavy lifting ##

def main():

    build_count = 0
    images = [image_lev_one, image_lev_two, image_lev_three]        ## list of images to use
    flag = 0                                        ## different flag value for the game loop
    db_flag = 0

    #building_group = pygame.sprite.Group()          ## sets a group of sprites to buildings

    rect = bg_play.get_rect()
    button = pygame.Rect(17, 13, b_w, b_h)

    drawUI =  buttonUI(bg_blank, bg_pause, bg_play, WID, HIG)       ## calls the class for the ui
    drawTime = timeUI()

    #pygame.time.set_timer(pygame.USEREVENT + 1, 100)       #~ for when I forget about user defined timed events

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

                        base_time = drawTime.base_time

                        print(base_time)

                        image = random.choice(images)       ## randomly choose an image from the list
                        if image == image_lev_one:          ## if it is this image
                            size = 20                       ## set the size of the square
                            level = 1                       ## and the building level
                            next_level_time = random.randrange(2,3) + base_time
                        if image == image_lev_two:          ## repeat for all building levels
                            size = 40
                            level = 2
                            next_level_time = 15 + random.randrange(20,360) + base_time
                        if image == image_lev_three:
                            size = 60
                            level = 3
                            next_level_time = 25 + random.randrange(20,360) + base_time

                        x = x1 = random.randrange(0,WID,100)       ## generate an x coordinate within the window area
                        y = y1 = random.randrange(0,HIG,100)       ## generate a  y coordinate within the window area

                        build1 = BuildObject(x,y,image,size)        ## draws a first building
                        build1.buildRect(x,y,image,size)
                        build1.blitRect(x,y,image,size)



                        #collide = pygame.sprite.spritecollide(build1, build_group, False)        #~ here because I forgot how to use collide functions

                        build_count += 1                                                ## increase the value of this flag
                        print("BUILDING NUMBER:", build_count)                          ## print the value as a checkpoint
                        print("")

                        print("BASE TIME:",base_time)

                        database = updateData(x, y, size, level, next_level_time, base_time)

                        if db_flag == 0:
                            database.create_table()
                            db_flag = 1
                        else:
                            database.write_table(x, y, size, level, next_level_time, base_time)

                        pygame.display.flip()   ## refresh the display so that all the new stuff appears
                        clock.tick(60)          ## set the clock to 60 or increase it by 60 idk

                        database.parse_table()

                        for event in pygame.event.get():  # ~ excluded because it will only create one building while I am creating the database properly
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

main()





