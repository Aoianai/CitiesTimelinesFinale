## time ui ##

import pygame, sys, time

class timeUI():

    def __init__(self):
        pygame.font.init()          ## start font
        self.y_date = 1990          ## start year
        self.m_date = 1             ## start month (jan)
        self.d_date = 1             ## start day (first)
        self.d_limit = 32           ## number of days in month (starts in jan so 31 days (count from 0 so 32)
        self.date_array = []        ## an array to display the date in DrawObjectBuild()

        self.t_font = pygame.font.SysFont('Myriad Pro', 45)

    def timeUpdate(self):
        time.sleep(0.1)                     ## wait 1ms
        self.d_date += 1                    ## progress to next day
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
                if self.m_date == 2000:     ## if it reaches year 2K
                    quit()                  ## stop

    def timeDisplay(self):
        self.date_array = [str(self.d_date), str(self.m_date), str(self.y_date)]
        self.t_time = '/'.join(self.date_array)
        time_sur = self.t_font.render(self.t_time, False, (0,0,0))
        screen.blit(time_sur, (850, 12))
