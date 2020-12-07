import pygame, sys, math
from pygame.locals import *
from Algos import a_star, djikstras
from Grid import Grid
from Node import Node
import os


pygame.init()
display_width = 800
DISPLAY = pygame.display.set_mode((display_width, display_width),0,32)
pygame.display.set_caption("Pathfinding Algorithms")
weight = pygame.image.load('bomb.bmp')
small_weight = pygame.transform.scale(weight, (display_width // 50, display_width // 50))

WHITE = (255,255,255)

DISPLAY.fill(WHITE)

def get_clicked_node(rows, pos):
    gap = display_width // rows
    x = pos[0] // gap
    y = pos[1] // gap
    return x,y

def main():
    start = None
    end = None
    grid = Grid(50, 50, display_width)
    grid.draw_lines(DISPLAY)
    while True:
        grid.draw_nodes(DISPLAY, small_weight)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]: #left mouse button clicked
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_node(50, pos)
                node = grid.array[row][col]
                if not start and node != end:
                    grid.array[row][col].set_start()
                    start = node
                elif not end and node != start:
                    grid.array[row][col].set_end()
                    end = node
                else:
                    if node.is_start():
                        continue
                    elif node.is_end():
                        continue
                    grid.array[row][col].set_as_barrier()

            if pygame.mouse.get_pressed()[2]: #right mouse button clicked
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_node(50, pos)
                node = grid.array[row][col]
                if node.is_start():
                    start = None
                elif node.is_end():
                    end = None
                grid.array[row][col].reset_node()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_node(50, pos)
                    node = grid.array[row][col]
                    if node is not start:
                        node.set_weight()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and start and end:
                    for row in grid.array:
                        for node in row:
                            node.get_neighbors(grid)
                    a_star(grid, start, end, DISPLAY, small_weight)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and start and end:
                    for row in grid.array:
                        for node in row:
                            node.get_neighbors(grid)
                    djikstras(grid, start, end, DISPLAY, small_weight)
        pygame.display.update()

main()