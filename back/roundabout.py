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


class Car(Agent):
    def __init__(self, unique_id, model, pos, matrix, end, end_positions):
        super().__init__(unique_id, model)
        self.end = end  # Indica la posición destino del coche
        self.pos = pos  # Indica la posición actual del coche
        self.type = "Car"  # Indica el tipo de agente para identificarse en el front-end
        self.condition = "HIDDEN"  # Indica si el coche está escondido o no, para no crear y destruir instancias siempre vamos a tener el mismo número de coches tanto en el back como en el front
        # Indica las posiciones destino posibles del coche
        self.end_positions = end_positions
        self.prev_pos = pos  # Indica la posición anterior del coche
        # Define la matriz local del coche, está matriz se usará para definir su comportamiento
        self.matrix = copy.deepcopy(matrix)
        self.direction = (1, 0)  # Indica la dirección del coche

        # Indica el porcentaje de probabilidad para que el coche desaparezca al llegar a su destino
        self.hidden_prob = 80
        self.shown_prob = 2  # Si el coche está oculto indica el porcentaje de probabilidad para que el coche vuelva a dibujarse en el paso actual de simulación y siguientes

        # Aplica las reglas dedel coche en la posición inicial
        self.roundabout_rules(pos)

    def roundabout_rules(self, pos):  # Aplica las reglas del coche en la posición actual
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

    # Elimina las reglas del coche en la posición anterior
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

    # Comprueba si hay un coche oculto en la posición siguiente
    def agent_in_front_hidden(self, next_x, next_y):
        agent_in_front_hidden = False
        for agent in self.model.grid.get_cell_list_contents((next_x, next_y)):
            if isinstance(agent, Car) and agent.condition == "HIDDEN":
                agent_in_front_hidden = True
        return agent_in_front_hidden

    def step(self):  # Método que se ejecuta en cada paso de simulación
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
                elif dx < 0:
                    self.direction = (-1, 0)  # Izquierda
                elif dy > 0:
                    self.direction = (0, 1)  # Arriba
                elif dy < 0:
                    self.direction = (0, -1)  # Abajo

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


class TrafficLight(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        # Indica el tipo de agente para identificarse en el front-end
        self.type = "TrafficLight"
        self.pos = pos  # Indica la posición del semáforo
        self.condition = False  # Indica si el semáforo está en verde o en rojo
        # Indica el tiempo que el semáforo estará en verde o en rojo
        self.timerRandom = random.randint(0, 4)

    def step(self):  # Método que se ejecuta en cada paso de simulación
        # Cada 10 pasos de simulación cambia el estado del semáforo
        if (self.model.time*self.timerRandom) % 10 == 0:
            self.condition = not self.condition  # Cambia el estado del semáforo


class Roundabout(Model):
    def __init__(self):
        super().__init__()
        # Posiciones iniciales de los coches
        self.start_positions = [(0, 7), (7, 16), (16, 9), (9, 0)]
        # Posiciones finales de los coches
        self.end_positions = [(0, 9), (16, 7), (7, 0), (9, 16)]
        self.schedule = RandomActivation(self)  # Inicializa el modelo
        self.grid = MultiGrid(17, 17, torus=False)  # Inicializa el grid
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
        ]  # Matriz del modelo

        self.time = 0  # Indica el tiempo de simulación

        for i in range(12):  # Crea 12 coches
            randomInt = random.randint(0, 3)
            car = Car(self.next_id(), self,
                      self.start_positions[i % 4], self.matrix, self.end_positions[randomInt], self.end_positions)
            self.grid.place_agent(car, car.pos)
            self.schedule.add(car)

        for _, (x, y) in self.grid.coord_iter():  # Crea los semáforos
            if self.matrix[y][x] == 2:
                traffic = TrafficLight(self.next_id(), self, (x, y))
                self.grid.place_agent(traffic, traffic.pos)
                self.schedule.add(traffic)

    def step(self):  # Método que se ejecuta en cada paso de simulación
        self.schedule.step()  # Ejecuta el método step de cada agente
        self.time += 1  # Incrementa el tiempo de simulación
