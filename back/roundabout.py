from mesa import Agent, Model
from mesa.space import MultiGrid
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
    def __init__(self, unique_id, model, pos, matrix, end, color, end_positions):
        super().__init__(unique_id, model)
        self.end = end
        self.pos = pos
        self.type = "Car"
        self.condition = "HIDDEN"
        self.end_positions = end_positions
        self.prev_pos = pos
        self.matrix = copy.deepcopy(matrix)
        self.direction = (1, 0)

        self.hidden_prob = 80
        self.shown_prob = 2
        if color == "red":
            self.image_paths = ["sprites/car_right.png",
                                "sprites/car_left.png", "sprites/car_up.png", "sprites/car_down.png"]
            self.image_path = "sprites/car_right.png"
        elif color == "blue":
            self.image_paths = ["sprites/car_right_blue.png",
                                "sprites/car_left_blue.png", "sprites/car_up_blue.png", "sprites/car_down_blue.png"]
            self.image_path = "sprites/car_right_blue.png"
        elif color == "green":
            self.image_paths = ["sprites/car_right_green.png",
                                "sprites/car_left_green.png", "sprites/car_up_green.png", "sprites/car_down_green.png"]
            self.image_path = "sprites/car_right_green.png"
        elif color == "yellow":
            self.image_paths = ["sprites/car_right_yellow.png",
                                "sprites/car_left_yellow.png", "sprites/car_up_yellow.png", "sprites/car_down_yellow.png"]
            self.image_path = "sprites/car_right_yellow.png"

        self.roundabout_rules(pos)

    def roundabout_rules(self, pos):
        x, y = pos
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

    def agent_in_front_hidden(self, next_x, next_y):
        agent_in_front_hidden = False
        for agent in self.model.grid.get_cell_list_contents((next_x, next_y)):
            if isinstance(agent, Car) and agent.condition == "HIDDEN":
                agent_in_front_hidden = True
        return agent_in_front_hidden

    def step(self):
        if self.condition == "HIDDEN" and self.shown_prob >= random.random()*100:
            self.condition = "SHOWN"
        if self.condition == "SHOWN":
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
                    if traffic_light_in_vision.condition and isEmpty:
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

                if self.model.grid.is_cell_empty(new_pos) or self.agent_in_front_hidden(new_pos[0], new_pos[1]):
                    self.model.grid.move_agent(self, new_pos)
                    self.des_roundabout_rules(self.prev_pos)
                    self.prev_pos = new_pos
                    self.roundabout_rules(self.pos)
                    self.end = random.choice(self.end_positions)
                    if self.hidden_prob >= random.random()*100:
                        self.condition = "HIDDEN"
                        self.model.sound.play()


class Block(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.type = "Block"
        self.condition = "none"
        self.pos = pos

    def step(self):
        print("Block")


class TrafficLight(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.type = "TrafficLight"
        self.pos = pos
        self.condition = False
        self.timerRandom = random.randint(0, 4)

    def step(self):
        if (self.model.time*self.timerRandom) % 10 == 0:
            self.condition = not self.condition


class Roundabout(Model):
    def __init__(self):
        super().__init__()
        self.start_positions = [(0, 7), (7, 16), (16, 9), (9, 0)]
        self.end_positions = [(0, 9), (16, 7), (7, 0), (9, 16)]
        self.colors = ["red", "blue", "green", "yellow"]
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(17, 17, torus=True)
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

        for i in range(12):
            randomInt = random.randint(0, 3)
            car = Car(self.next_id(), self,
                      self.start_positions[i % 4], self.matrix, self.end_positions[randomInt], self.colors[i % 4], self.end_positions)
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
    if isinstance(agent, Car) and agent.condition == "SHOWN":
        return {"Shape": agent.image_path, "Layer": 1}
    elif isinstance(agent, Block):
        return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Gray", "Layer": 0}
    elif isinstance(agent, TrafficLight):
        if agent.condition:
            return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Green", "Layer": 0}
        else:
            return {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Color": "Red", "Layer": 0}


grid = CanvasGrid(agent_portrayal, 17, 17, 450, 450)

server = ModularServer(Roundabout, [grid], "Roundabout Simulation", {})
server.port = 8522
server.launch()
