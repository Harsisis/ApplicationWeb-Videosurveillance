import sys
import pygame
from IPWebCam import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((176,144))

ipcam = IPWEBCAM('192.168.68.103:8080')

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()
      sys.exit()
  screen.blit(ipcam.get_pygame_image(),(0,0))
  pygame.display.flip()
  clock.tick(0)
