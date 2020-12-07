from queue import PriorityQueue
import pygame
import sys

def h(start, end):
    x0, y0 = start
    x1, y1 = end
    return abs(x0 - x1) + abs(y0 - y1)
    
def reconstruct_path(came_from, current):
    current.set_end()
    while current in came_from:
        current = came_from[current]
        current.set_path()
    current.set_start()


def a_star(grid, start, end, display, weight):
    count = 0
    openSet = PriorityQueue()
    cameFrom = {}
    gScore = {node: float('inf') for row in grid.array for node in row}
    gScore[start] = 0
    fScore = {node: float('inf') for row in grid.array for node in row}
    fScore[start] = h(start.get_xy(), end.get_xy())
    openSet.put((0, count, start))
    openSetNodes = {start}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        grid.draw_nodes(display, weight)
        current = openSet.get()[2]
        openSetNodes.remove(current)
        if current == end:
            reconstruct_path(cameFrom, current)
            return
        
        for neighbor in current.neighbors:
            tentative_gScore = gScore[current] + neighbor.weight
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + h(neighbor.get_xy(), end.get_xy())
                if neighbor not in openSetNodes:
                    count += 1
                    openSet.put((fScore[neighbor], count, neighbor))
                    openSetNodes.add(neighbor)
                    neighbor.set_open()
        if current != start:
            current.set_closed()
    return


def djikstras(grid, start, end, display, weight):
    queue = PriorityQueue()
    dist = {node: float('inf') for row in grid.array for node in row}
    prev = {node: None for row in grid.array for node in row}
    dist[start] = 0
    counter = 0
    queue.put((dist[start],counter, start))
    
    while not queue.empty():
        grid.draw_nodes(display, weight)
        current = queue.get()[2]
        for neighbor in current.neighbors:
            if neighbor != start and neighbor != end:
                neighbor.set_open()
            alt = dist[current] + neighbor.weight
            if alt < dist[neighbor]:
                counter += 1
                queue.put((alt, counter, neighbor))
                dist[neighbor] = alt
                prev[neighbor] = current
    make_djikstra_path(prev, start, end)
    

def make_djikstra_path(prev, start, end):
    pointer = end
    while pointer != start and prev[pointer] != None:
        prev[pointer].set_path()
        pointer = prev[pointer]