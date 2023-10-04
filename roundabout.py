# A01736149 - HUGO MUÑOZ
from mesa import Agent, Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

import random
import copy

image_path = "car_right.png"
time = 0


class Car(Agent):
    def __init__(self, model, pos, matrix, end):
        super().__init__(model.next_id(), model)
        self.end = end
        self.pos = pos
        self.matrix = copy.deepcopy(matrix)
        self.direction = (1, 0)
        if pos == (0, 7):
            # matrixbloqued for (0,7) roundabout rules
            self.matrix[8][5] = 0
            self.matrix[8][6] = 0
            self.matrix[8][4] = 0

        elif pos == (7, 16):
            # matrixbloqued for (7,16) roundabout rules
            self.matrix[10][8] = 0
            self.matrix[11][8] = 0
            self.matrix[12][8] = 0
        elif pos == (16, 9):
            # matrixbloqued for (16,9) roundabout rules
            self.matrix[8][10] = 0
            self.matrix[8][11] = 0
            self.matrix[8][12] = 0
        elif pos == (9, 0):
            # matrixbloqued for (9,0) roundabout rules
            self.matrix[5][8] = 0
            self.matrix[6][8] = 0
            self.matrix[4][8] = 0
        # self.matrixBloqued=

    def step(self):
        global image_path
        grid = Grid(matrix=self.matrix)
        (x, y) = self.pos
        start = grid.node(self.pos[0], self.pos[1])
        end = grid.node(self.end[0], self.end[1])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        if len(path) > 1:
            next_x, next_y = path[1]

            neighbors = []
            neighborsCoords = self.model.grid.get_neighborhood(
                self.pos, moore=True, include_center=False, radius=3)

            for agent in neighborsCoords:
                neighbor = self.model.grid.get_cell_list_contents([agent])
                if neighbor:
                    neighbors.append(neighbor)

            traffic_light_in_vision = next(
                (agent for [agent] in neighbors if isinstance(agent, TrafficLight)), None)

            if traffic_light_in_vision and self.matrix[next_y][next_x] == 3:
                if traffic_light_in_vision.canPass:
                    # The TrafficLight allows passing, move the car to the target cell
                    self.model.grid.move_agent(self, (next_x, next_y))
                else:
                    # The TrafficLight does not allow passing, do not move the car
                    pass
            else:
                # No traffic light in vision, move the car to the target cell
                self.model.grid.move_agent(self, (next_x, next_y))

                dx = next_x - x
                dy = next_y - y
                if dx > 0:
                    self.direction = (1, 0)  # Derecha
                    image_path = "car_right.png"
                elif dx < 0:
                    self.direction = (-1, 0)  # Izquierda
                    image_path = "car_left.png"
                elif dy > 0:
                    self.direction = (0, 1)  # Abajo
                    image_path = "car_up.png"
                elif dy < 0:
                    self.direction = (0, -1)  # Arriba
                    image_path = "car_down.png"


class Block(Agent):
    def __init__(self, model, pos):
        super().__init__(model.next_id(), model)
        self.pos = pos


class TrafficLight(Agent):
    def __init__(self, model, pos):
        super().__init__(model.next_id(), model)
        self.pos = pos
        self.canPass = False

    def step(self):
        global time
        # asymetric traffic light 10 seconds green, 5 seconds red
        if time % 10 == 0:
            self.canPass = not self.canPass


class Roundabout(Model):
    def __init__(self):
        super().__init__()
        self.start = [(0, 7), (7, 16), (16, 9), (9, 0)]
        self.end = [(0, 9), (16, 7), (7, 0), (9, 16)]

        random1 = random.randint(0, 3)
        random2 = random.randint(0, 3)
        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(17, 17, torus=False)
        self.matrix = [
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 3, 1, 1, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1],
            [0, 0, 0, 0, 3, 1, 1, 0, 0, 0, 1, 1, 3, 0, 0, 0, 0],
            [1, 1, 1, 1, 3, 1, 1, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        ]

        car = Car(self, self.start[random2], self.matrix, self.end[random1])
        self.grid.place_agent(car, car.pos)
        self.schedule.add(car)

        for _, (x, y) in self.grid.coord_iter():
            if self.matrix[y][x] == 0:
                block = Block(self, (x, y))
                self.grid.place_agent(block, block.pos)
            elif self.matrix[y][x] == 2:
                traffic = TrafficLight(self, (x, y))
                self.grid.place_agent(traffic, traffic.pos)
                self.schedule.add(traffic)

        grid = Grid(matrix=self.matrix)
        start = grid.node(0, 0)
        end = grid.node(2, 2)

    def step(self):
        global time
        self.schedule.step()
        time += 1


def agent_portrayal(agent):
    global image_path
    if type(agent) == Car:
        return {"Shape": image_path, "Layer": 1}

    elif type(agent) == Block:
        return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Gray", "Layer": 0}
    elif type(agent) == TrafficLight:
        if agent.canPass:
            return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Green", "Layer": 0}
        else:
            return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Red", "Layer": 0}


grid = CanvasGrid(agent_portrayal, 17, 17, 450, 450)

server = ModularServer(Roundabout, [grid], "Roundabout Simulation", {})
server.port = 8522
server.launch()
