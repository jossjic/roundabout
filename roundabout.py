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
import pygame


class Car(Agent):
    def __init__(self, unique_id, model, pos, matrix, end):
        super().__init__(unique_id, model)
        self.end = end
        self.pos = pos
        self.prev_pos = pos
        self.matrix = copy.deepcopy(matrix)
        self.direction = (1, 0)
        self.image_paths = ["car_right.png",
                            "car_left.png", "car_up.png", "car_down.png"]
        self.image_path = "car_right.png"

        self.roundabout_rules()

    def roundabout_rules(self):
        x, y = self.pos
        if (x, y) == (0, 7):
            self.matrix[8][4:7] = [0, 0, 0]
        elif (x, y) == (7, 16):
            for row in range(10, 13):
                self.matrix[row][8] = 0
        elif (x, y) == (16, 9):
            self.matrix[8][10:13] = [0, 0, 0]
        elif (x, y) == (9, 0):
            for row in range(4, 7):
                self.matrix[row][8] = 0

    def des_roundabout_rules(self, pos):
        x, y = pos
        if (x, y) == (0, 7):
            self.matrix[8][4:7] = [1, 1, 1]
        elif (x, y) == (7, 16):
            for row in range(10, 13):
                self.matrix[row][8] = 1
        elif (x, y) == (16, 9):
            self.matrix[8][10:13] = [1, 1, 1]
        elif (x, y) == (9, 0):
            for row in range(4, 7):
                self.matrix[row][8] = 1

    def step(self):
        grid = Grid(matrix=self.matrix)
        (x, y) = self.pos
        start = grid.node(self.pos[0], self.pos[1])
        end = grid.node(self.end[0], self.end[1])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        if len(path) > 1:
            next_x, next_y = path[1]

            neighbors = self.model.grid.get_neighbors(
                self.pos, moore=True, include_center=False, radius=3)

            traffic_light_in_vision = next(
                (agent for agent in neighbors if isinstance(agent, TrafficLight)), None)

            isEmpty = self.model.grid.is_cell_empty((next_x, next_y))
            if traffic_light_in_vision and self.matrix[next_y][next_x] == 3:
                if traffic_light_in_vision.canPass and isEmpty:
                    self.model.grid.move_agent(self, (next_x, next_y))

            elif isEmpty:
                self.model.grid.move_agent(self, (next_x, next_y))

            dx = next_x - x
            dy = next_y - y
            if dx > 0:
                self.direction = (1, 0)  # Derecha
                self.image_path = self.image_paths[0]
            elif dx < 0:
                self.direction = (-1, 0)  # Izquierda
                self.image_path = self.image_paths[1]
            elif dy > 0:
                self.direction = (0, 1)  # Arriba
                self.image_path = self.image_paths[2]
            elif dy < 0:
                self.direction = (0, -1)  # Abajo
                self.image_path = self.image_paths[3]

        elif self.pos == self.end:
            if (self.pos[0]+self.direction[0]) == 17:
                new_pos = (0, self.pos[1])
            elif (self.pos[0]+self.direction[0]) == -1:
                new_pos = (16, self.pos[1])
            elif (self.pos[1]+self.direction[1]) == 17:
                new_pos = (self.pos[0], 0)
            elif (self.pos[1]+self.direction[1]) == -1:
                new_pos = (self.pos[0], 16)

            if self.model.grid.is_cell_empty(new_pos):
                self.model.grid.move_agent(self, new_pos)
                self.des_roundabout_rules(self.prev_pos)
                self.prev_pos = new_pos
                self.roundabout_rules()
                self.model.sound.play()


class Block(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos


class TrafficLight(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
        self.canPass = False

    def step(self):
        if self.model.time % 10 == 0:
            self.canPass = not self.canPass


class Roundabout(Model):
    def __init__(self):
        super().__init__()
        self.start_positions = [(0, 7), (7, 16), (16, 9), (9, 0)]
        self.end_positions = [(0, 9), (16, 7), (7, 0), (9, 16)]

        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(17, 17, torus=True)
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

        self.time = 0

        pygame.init()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("torus.mp3")

        for i in range(4):
            randomInt = random.randint(0, 3)
            car = Car(self.next_id(), self,
                      self.start_positions[i], self.matrix, self.end_positions[randomInt])
            self.grid.place_agent(car, car.pos)
            self.schedule.add(car)

        for _, (x, y) in self.grid.coord_iter():
            if self.matrix[y][x] == 0:
                block = Block(self.next_id(), self, (x, y))
                self.grid.place_agent(block, block.pos)
            elif self.matrix[y][x] == 2:
                traffic = TrafficLight(self.next_id(), self, (x, y))
                self.grid.place_agent(traffic, traffic.pos)
                self.schedule.add(traffic)

    def step(self):
        self.schedule.step()
        self.time += 1


def agent_portrayal(agent):
    if isinstance(agent, Car):
        return {"Shape": agent.image_path, "Layer": 1}
    elif isinstance(agent, Block):
        return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Gray", "Layer": 0}
    elif isinstance(agent, TrafficLight):
        if agent.canPass:
            return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Green", "Layer": 0}
        else:
            return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Red", "Layer": 0}


grid = CanvasGrid(agent_portrayal, 17, 17, 450, 450)

server = ModularServer(Roundabout, [grid], "Roundabout Simulation", {})
server.port = 8522
server.launch()
