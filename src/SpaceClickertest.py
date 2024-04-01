import pygame
from pygame.locals import *

pygame.init()

canvas = pygame.display.set_mode((250, 250), pygame.RESIZABLE)
pygame.display.set_caption("Hello World")

done = False
win = False
points = 0
start = False

red = (255,0,0)
orange = (255,125,0)
yellow = (255,255,0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255,0, 255)

while start == False:
   for event in pygame.event.get():
      canvas.fill(blue)
      font = pygame.font.SysFont("Arial", 20)
      txtsurf = font.render(str(points), True, orange)
      canvas.blit(txtsurf, (100, 100))
      if event.type == pygame.MOUSEBUTTONDOWN:
         start = true
      
while done == False:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
      if event.type == pygame.MOUSEBUTTONDOWN:
         pos=pygame.mouse.get_pos()
         distance_squared = (pos[0] - 125) ** 2 + (pos[1] - 125) ** 2
         if distance_squared <= 25 ** 2:
            points += 1
      if points >= 10 and win == False:
         print("you win")
         win = True
   canvas.fill(blue)
   if win:
      font = pygame.font.SysFont("Arial", 20)
      txtsurf = font.render("You Win! Click to exit.", True, orange)
      canvas.blit(txtsurf, (25, 100))
   else:
      pygame.draw.circle(canvas, purple, (125,125), 25)
      font = pygame.font.SysFont("Arial", 20)
      txtsurf = font.render(str(points), True, orange)
      canvas.blit(txtsurf, (100, 100))
   pygame.display.update()

   if win:
      for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            done = True
   
