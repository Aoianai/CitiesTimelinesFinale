## DrawObjectMain

## Runs the DrawObject series of files 

import pygame, random

import DrawObjectBuilding



def SpaceBuild():
    flag = 0

    bg_color = (255,255,255)

    window = pygame.display.set_mode((1356,720))
    window.fill(bg_color)
    pygame.display.set_caption(":(")
    pygame.display.flip()

    level_one_group = pygame.sprite.Group()

    origin_building = DrawObjectBuilding.DrawBuild()

    level_one_group.add(origin_building)

    done = True
    clock = pygame.time.Clock()

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                while event.key == pygame.K_SPACE and flag <= 100:

                    b = origin_building.drawSprite()

                    level_one_group.add(b)                   
                    level_one_group.update()

                    level_one_group.draw(window)
                    pygame.display.flip()

                    clock.tick(60)
                    flag += 1

SpaceBuild()
