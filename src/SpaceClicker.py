import pygame
from pygame.locals import *

pygame.init()

size = [500, 500]

done = False
win = False
start = False
points = 0
multiplier = 1

red = (255,0,0)
orange = (255,125,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
white = (255,255,255)
black = (0,0,0)

font = pygame.font.SysFont("Arial", 42)

canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Space Clicker")

def play():
   global start, done, win, points, multiplier
   while start == False:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            start = True
            done = True
         canvas.fill(blue)
         text = font.render("Welcome to Space Clicker", True, white)
         center_x = (size[0] // 2) - (text.get_width() // 2)
         canvas.blit(text, (center_x, 70))
         text2 = font.render("Click to begin", True, white)
         center_x = (size[0] // 2) - (text2.get_width() // 2)
         canvas.blit(text2, (center_x, 300))
         text2 = font.render("Click to gain points", True, orange)
         center_x = (size[0] // 2) - (text2.get_width() // 2)
         canvas.blit(text2, (center_x, 150))
         text3 = font.render("Get to 1000 points to win", True, orange)
         center_x = (size[0] // 2) - (text3.get_width() // 2)
         canvas.blit(text3, (center_x, 200))
         if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
         pygame.display.update()
      
   while done == False:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            done = True
         if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            distance_squared = (pos[0] - (size[0] // 2)) ** 2 + (pos[1] - (size[1] // 2)) ** 2
            if distance_squared <= 100 ** 2:
               points += (1 * multiplier)
     #       if pos[0] <= 100 and pos[0] >= 50 and pos[1] <= 100 and pos[1] >= 50 and points >= 5:
      #         multiplier += 1
       #        points -= 5
            upgrade(50, 50, 1, 5, pos[0], pos[1])
         if points >= 1000 and win == False:
            print("you win")
            win = True
      canvas.fill(blue)
      if win:
         text = font.render("You Win! Click to exit.", True, orange)
         center_x = (size[0] // 2) - (text.get_width() // 2)
         center_y = (size[1] // 2) - (text.get_height() // 2)
         canvas.blit(text, (center_x, center_y))
         
      pygame.draw.circle( canvas, purple, ((size[0] // 2), (size[1] // 2)), 100)
      pygame.draw.rect(canvas, purple, pygame.Rect(50, 50, 150, 100))  
      text = font.render("You have: " + str(points) + " points", True, orange)
      center_x = (size[0] // 2) - (text.get_width() // 2)
      canvas.blit(text, (center_x, 100))
      pygame.display.update()

      if win:
         for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
               done = True

def upgrade(posx, posy, value, cost, mousex, mousey):
   global points, multiplier
   posx2 = posx + 100
   posy2 = posy + 50
   #pygame.draw.rect(canvas, purple, pygame.Rect(posx, posy, posx2, posy2))  
   #if click in area and have the cost increase by value
   if mousex <= posx2 and mousex >= posx and mousey <= posy2 and mousey >= posy and points >= cost:
      multiplier += value
      points -= cost
   pygame.display.update()
   
play()
