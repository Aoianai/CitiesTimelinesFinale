import DrawObjectBuilding
import pygame

image = pygame.image.load("BuildingLevelOne.png").convert_alpha()
x = 0
y = 0
create = DrawObjectBuilding.BuildObject(x,y,image)
create.getXY
create.drawBlit(image)
