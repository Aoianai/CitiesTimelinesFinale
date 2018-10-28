## collision testing

import pygame
import sys

class StickMan(pygame.sprite.Sprite):

   # We’ll just accept the x-position here
   def __init__(self, xPosition):

      pygame.sprite.Sprite.__init__(self)
      self.old = (0, 0, 0, 0)
      self.image = pygame.image.load('lev_two.png')
      self.rect = self.image.get_rect()
      self.rect.x = xPosition

   # The x-position remains the same
   def update(self, yPosition):

      self.old = self.rect
      self.rect = self.rect.move([0, yPosition - self.rect.y])

# Define a function to erase old sprite positions
# This will be used later
def eraseSprite(screen, rect):
   screen.blit(blank, rect)

pygame.init()
screen = pygame.display.set_mode((256, 256))
pygame.display.set_caption('Sprite Groups')
screen.fill((255, 255, 255))

# Create the three stick men
stick1 = StickMan(25)
stick2 = StickMan(75)
stick3 = StickMan(125)

# Create a group and add the sprites
stickGroup = pygame.sprite.Group()
stickGroup.add((stick1, stick2, stick3))

# Add a variable for the direction, y-position and height of the sprite we are dealing with
stickGroup.direction = "up"
stickGroup.y = screen.get_rect().centery
stickGroup.height = stick1.rect.height

# Create a blank piece of background
blank = pygame.Surface((stick1.rect.width, stick1.rect.height))
blank.fill((255, 255, 255))

pygame.display.update()

# Create an event that will appear ever 100 milliseconds
# This will be used to update the screen
pygame.time.set_timer(pygame.USEREVENT + 1, 100)

while True:

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()

      # Check for our update event
      if event.type == pygame.USEREVENT + 1:

         # Update the y-position
         if stickGroup.direction == "up":
            stickGroup.y = stickGroup.y - 10
         else:
            stickGroup.y = stickGroup.y + 10

         # Check if we have gone off the screen
         # If we have, fix it
         if stickGroup.direction == "up" and stickGroup.y <= 0:
            stickGroup.direction = "down"
         elif stickGroup.direction == "down" and stickGroup.y >= (screen.get_rect().height - stickGroup.height):
            stickGroup.direction = "up"
            stickGroup.y = screen.get_rect().height - stickGroup.height

         # Clear the old sprites
         # Notice that we pass our eraseSprite function
         # This will be called, and the screen and old position will be passed
         stickGroup.clear(screen, eraseSprite)

         # Update the sprites
         stickGroup.update(stickGroup.y)

         # Blit the sprites
         stickGroup.draw(screen)

         # Create a list to store the updated rectangles
         updateRects = []

         # Get the updated rectangles
         for man in stickGroup:
            updateRects.append(man.old)
            updateRects.append(man.rect)
         pygame.display.update(updateRects)

'''{mospagebreak title=Explaining the Group Class}'''
