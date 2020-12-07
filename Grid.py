from Node import Node
import pygame

BLACK = (0, 0, 0)

class Grid:
    def __init__(self, rows, cols, display_width):
        self.rows = rows
        self.cols = cols
        self.display_width = display_width
        self.array  = [[Node(row, col, display_width // rows) for col in range(cols)] for row in range(rows)]

    def draw_lines(self, display):
        dist = self.display_width // self.rows
        for i in range(self.cols):
            pygame.draw.line(display, BLACK, (i*dist, 0), (i*dist, self.display_width))
            for j in range(self.rows):
                pygame.draw.line(display, BLACK, (0, j*dist), (self.display_width, j*dist))

    def draw_nodes(self, display, weight):
        for row in self.array:
            for node in row:
                node.draw(display, weight)
        pygame.display.update()