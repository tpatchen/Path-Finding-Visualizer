import pygame

WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0, 0, 0)
RED = (255,  0, 0)
CYAN = (0, 255, 255)
PINK = (255, 51, 153)
GREEN = (0, 255, 0)

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.weight = 1
    def get_xy(self):
        return self.row, self.col
    
    def is_barrier(self):
        return self.color == BLACK

    def set_as_barrier(self):
        self.color = BLACK
    
    def set_start(self):
        self.color = CYAN

    def is_start(self):
        return self.color == CYAN

    def set_end(self):
        self.color = PINK
    
    def is_end(self):
        return self.color == PINK
    
    def is_weight(self):
        return self.weight == 5

    def reset_node(self):
        self.color = WHITE
        self.weight = 1

    def set_open(self):
        self.color = GREEN
    
    def set_closed(self):
        self.color = RED

    def set_path(self):
        self.color = BLUE
    
    def set_weight(self):
        self.weight = 15
    
    def get_neighbors(self, grid):
        neighbors = []
        row, col = self.row, self.col
        if col > 0 and not grid.array[row][col - 1].is_barrier(): #left
            neighbors.append(grid.array[row][col - 1])
        if col < grid.cols - 1 and not grid.array[row][col + 1].is_barrier(): #right
            neighbors.append(grid.array[row][col + 1])
        if row > 0 and not grid.array[row - 1][col].is_barrier(): #up
            neighbors.append(grid.array[row - 1][col])
        if row < grid.rows - 1 and not grid.array[row + 1][col].is_barrier(): #down
            neighbors.append(grid.array[row + 1][col])
        self.neighbors = neighbors

    def draw(self,display, weight):
        pygame.draw.rect(display, self.color, (self.x + 1, self.y + 1, self.width - 1, self.width - 1))
        if self.weight == 15:
            display.blit(weight, (self.x, self.y))