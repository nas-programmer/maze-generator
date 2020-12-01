"""Maze Generation"""

#Imports
import pygame, sys, random, os
import cv2

#Pygame Initialization
pygame.init()
win = pygame.display.set_mode((600, 360))
pygame.display.set_caption('Maze')
clock = pygame.time.Clock()

#Pixels for Map Creation
mapy = cv2.imread('screenshot.png')

#Wall List
lineList = []

#Player Class
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.size = 6, 6
        self.rect = pygame.Rect((self.x, self.y), self.size)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 2
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self, list_):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        if not self.collidelist(list_):
            self.x += self.velX
            self.y += self.velY

        self.rect = pygame.Rect((int(self.x), int(self.y)), self.size)
    
    def collidelist(self, list_):
        for wall in list_:
            temp = pygame.Rect((int(self.x)+self.velX, int(self.y)+self.velY), self.size)
            if temp.colliderect(wall):
                return True
        return False

#Player Initialization
player = Player(4, 4)

#Image
image = pygame.image.load('screenshot.png') 

#Walls Initialization
i = 0
while i < len(mapy) - 1:
    j = 0
    while j-10 < len(mapy[0])-1:
        try:
            if list(mapy[i][j]) == [0, 0, 0] and list(mapy[i][j+9]) == [0, 0, 0]:
                lineList.append(pygame.draw.line(win, (0, 0, 0), (j, i), (j+9,i), 2))
            if list(mapy[i][j]) == [0, 0, 0] and list(mapy[i+9][j]) == [0, 0, 0]:
                lineList.append(pygame.draw.line(win, (0, 0, 0), (j, i), (j,i+9), 2))
        except Exception as e:
            pass
        j+=10
    i+=10


#Main Loop
while True:

    #Set Fps
    clock.tick(60)

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
        
    #Draw 
    win.blit(image, (0, 0))
    player.draw(win)


    #update
    player.update(lineList)
    pygame.display.flip()
