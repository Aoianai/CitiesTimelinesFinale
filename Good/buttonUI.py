## button UI ##

import pygame

bg_play = pygame.image.load("bg_play.png").convert_alpha()
bg_pause = pygame.image.load("bg_pause.png").convert_alpha()
bg_blank = pygame.image.load("bg_blank.png").convert_alpha()

class buttonUI(pygame.sprite.Sprite):

    def __init__(self,bg_blank, bg_pause, bg_play, WID, HIG):
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
