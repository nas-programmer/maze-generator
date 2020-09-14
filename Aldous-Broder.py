"""Aldous-Broder"""

import pygame, sys, random

pygame.init()

win = pygame.display.set_mode((600, 360))
clock = pygame.time.Clock()

w = 10

cols = int(win.get_width()/w)
rows = int(win.get_height()/w)

grid = []
unvisited = []

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
        self.col = 10
        
    def show(self, win):
        x = self.i * w
        y = self.j * w
        
        if self.visited:
            pygame.draw.rect(win, (10, 120, 250), (self.i*w, self.j*w, w, w))
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
            neighbors.append(top)
        if index(i+1, j):
            right = grid[index(i+1, j)]
            neighbors.append(right)
        if index(i-1, j):
            left = grid[index(i-1, j)]
            neighbors.append(left)
        if index(i, j+1):
            bottom = grid[index(i, j+1)]
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
        unvisited.append(cell)

n = 0

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
    for cell in unvisited:
        if cell == current:
            unvisited.remove(cell)
    current.highlight(win) 
    if len(unvisited) > 0:
        nextcell = current.checkNeighbors()  
        if isinstance(nextcell, Cell) and not nextcell.visited:
            removeWalls(current, nextcell)
            nextcell.visited = True
        current = nextcell

    pygame.display.flip()