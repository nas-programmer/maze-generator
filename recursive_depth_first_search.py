"""Backtracking Recursive Maze Generation"""

import pygame, sys, random

pygame.init()

win = pygame.display.set_mode((600, 360))
clock = pygame.time.Clock()

w = 10

cols = int(win.get_width()/w)
rows = int(win.get_height()/w)

grid = []
stack = []

def index(i, j):
    if i < 0 or j < 0 or i > cols -1 or j > rows - 1:
        return None
    else:
        return i+j*cols

class Cell:
    def __init__(self, i, j):
        self.i, self.j = i, j
        self.walls = [True, True, True, True]
        self.visited = False
        
    def show(self, win):
        x = self.i * w
        y = self.j * w
        if self.visited:
            pygame.draw.rect(win, (190, 90, 90), (self.i*w, self.j*w, w, w))
        if self.walls[0]:
            pygame.draw.line(win, (0, 0, 0), (x,y), (x+w,y))
        if self.walls[1]:    
            pygame.draw.line(win, (0, 0, 0), (x+w,y), (x+w,y+w))
        if self.walls[2]:    
            pygame.draw.line(win, (0, 0, 0), (x+w,y+w), (x,y+w))
        if self.walls[3]:
            pygame.draw.line(win, (0, 0, 0), (x,y+w), (x,y))
        
    def highlight(self, win):
        x = self.i * w
        y = self.j * w
        if self.visited:
            pygame.draw.rect(win, (90, 190, 190), (self.i*w, self.j*w, w, w))
    
    def checkNeighbors(self):
        neighbors = []
        i, j = self.i, self.j
        if index(i, j-1):
            top = grid[index(i, j-1)]
            if not top.visited:
                neighbors.append(top)
        if index(i+1, j):
            right = grid[index(i+1, j)]
            if not right.visited:
                neighbors.append(right)
        if index(i-1, j):
            left = grid[index(i-1, j)]
            if not left.visited:
                neighbors.append(left)
        if index(i, j+1):
            bottom = grid[index(i, j+1)]
            if not bottom.visited:
                neighbors.append(bottom)
                 
            
        if len(neighbors) > 0:
            return random.choice(neighbors)
        else:
            return None

        
def removeWalls(a, b):
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False
    y = a.j - b.j
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False
    

for j in range(rows):
    for i in range(cols):
        cell = Cell(i, j)
        grid.append(cell)

n = 0
#n = (cols*rows)//2 + (cols+rows)*2

current = grid[n]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    win.fill((0, 0, 0))
    
    
    for cell in grid:
        cell.show(win)
    
    current.visited = True
    current.highlight(win) 
    #Step1
    nextcell = current.checkNeighbors()   
    if isinstance(nextcell, Cell):
        nextcell.visited = True
        #Step2
        stack.append(current)
        #Step3
        removeWalls(current, nextcell)
        #Step4
        current = nextcell
    elif len(stack) > 0:
        current = stack.pop()

    pygame.display.flip()
