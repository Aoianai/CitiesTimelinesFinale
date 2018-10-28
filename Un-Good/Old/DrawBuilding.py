## DrawBuilding

import pygame, sys

WID = 1000
HIG = 720
WHITE = (255, 255, 255)
size = 40

class BuildingObject(pygame.sprite.Sprite):

    def __init(self, x_coor):
        pygame.sprite.Sprie.__init__(self)
        self.image = pygame.image.load('lev_two.png')
        self.rect = self.image.get_rect()
        self.rect.x = x_coor
        self.rect.y = y_coor

def eraseSprite(screen, rect):
    screen.blit(blank,rect)

pygame.init()
screen = pygame.display.setmode((WID,HIG))
pygame.display.set_caption(':(')
screen.fill(WHITE)

build1 = BuildingObject(random.randrange(0,WID,size),random.randrange(0,HIG,size))
build2 = BuildingObject(random.randrange(0,WID,size),random.randrange(0,HIG,size))
build3 = BuildingObject(random.randrange(0,WID,size),random.randrange(0,HIG,size))

building_group = pygame.sprite.Group()
building_group.add((build1, build2, build3))

blank = pygame.Surface((build1.rect.width, build1,rect,height))
blank.fill(WHITE)

pygame.display.update()

pygame.time.set_timer(pygame.USEREVENT + 1, 100)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit

        if event.type == ygame.USEREVENT + 1:
            if building_group
