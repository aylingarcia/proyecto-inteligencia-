import math
import time
import tkinter as tk
from collections import deque
import heapq

from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile

class Controller():
    def __init__(self, app):
        self.app = app
        self.manage = ManagerFile()
        self.grafo = GrafoNoDirigido
        self.grafo = self.manage.obGrafoSinText(self.grafo)
        self.nodes = self.manage.obtenerNodesMana(self.grafo)

        self.app.config(bg="#212F3D")

        self.drawBackground()
        self.draw_Nodes()

        self.app.clear_button.configure(command=lambda: self.clear())
        self.app.send_agent_button.configure(command=lambda: self.run_algorithm())

        self.app.mainloop()

    def run_algorithm(self):
        start = self.app.entry_start.get()
        goal = self.app.entry_destination.get()
        ini = self.grafo.getVertex(start)
        fin = self.grafo.getVertex(goal)

        bfs_path = self.buscar_nodo_en_grafo(self.grafo.grafoDiccionario, ini, fin)
        a_star_path = self.buscar_nodo_en_grafo_a_star(ini, fin)
        bi_path = self.bidirectional(self.grafo, ini, fin)

#colores de los caminos
        self.drawPath(bfs_path, "red")
        self.drawPath(a_star_path, "blue")
        self.drawPath(bi_path, "green")

    def buscar_nodo_en_grafo(self, grafo, nodo_inicio, nodo_objetivo):
        visitados = set()
        cola = deque([(nodo_inicio, [])])

        while cola:
            nodo, camino = cola.popleft()
            if nodo == nodo_objetivo:
                return camino + [nodo]

            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in grafo[nodo]:
                    cola.append((vecino, camino + [nodo]))
        return None

    def buscar_nodo_en_grafo_a_star(self, nodo_inicio, nodo_objetivo):
        visitados = set()
        cola_prioridad = [(0, nodo_inicio, [])]

        while cola_prioridad:
            _, nodo, camino = heapq.heappop(cola_prioridad)

            if nodo == nodo_objetivo:
                return camino + [nodo]

            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in self.grafo.grafoDiccionario[nodo]:
                    costo = self.calculate_distance(nodo, vecino) + self.heuristic(vecino, nodo_objetivo)
                    heapq.heappush(cola_prioridad, (costo, vecino, camino + [nodo]))

        return None

    def heuristic(self, nodo, nodo_objetivo):
        x1, y1 = nodo.getXY()
        x2, y2 = nodo_objetivo.getXY()
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def bidirectional(self, graph, start, goal):
        # Inicialización
        open_list_start = [start]
        open_list_goal = [goal]
        closed_list_start = set()
        closed_list_goal = set()
        parents_start = {start: None}
        parents_goal = {goal: None}

        while open_list_start and open_list_goal:
            # Expandir desde el nodo de inicio
            current_node_start = open_list_start.pop(0)

            if current_node_start in closed_list_goal:
                # Se ha encontrado una intersección, reconstruir el camino
                path = []
                while current_node_start is not None:
                    path.append(current_node_start)
                    current_node_start = parents_start[current_node_start]
                path.reverse()

                current_node_goal = closed_list_goal.intersection(path).pop()
                while current_node_goal is not None:
                    path.append(current_node_goal)
                    current_node_goal = parents_goal[current_node_goal]

                return path

            closed_list_start.add(current_node_start)

            # Explorar vecinos desde el nodo de inicio

            for neighbor in graph.getNeighbors(current_node_start):
                if neighbor not in closed_list_start:
                    open_list_start.append(neighbor)
                    parents_start[neighbor] = current_node_start

            # Expandir desde el nodo objetivo
            current_node_goal = open_list_goal.pop(0)

            if current_node_goal in closed_list_start:
                # Se ha encontrado una intersección, reconstruir el camino
                path = []
                while current_node_goal is not None:
                    path.append(current_node_goal)
                    current_node_goal = parents_goal[current_node_goal]
                path.reverse()

                current_node_start = closed_list_start.intersection(path).pop()
                while current_node_start is not None:
                    path.append(current_node_start)
                    current_node_start = parents_start[current_node_start]

                return path

            closed_list_goal.add(current_node_goal)
            # Explorar vecinos desde el nodo objetivo
            for neighbor in graph.getNeighbors(current_node_goal):
                if neighbor not in closed_list_goal:
                    open_list_goal.append(neighbor)
                    parents_goal[neighbor] = current_node_goal

        # No se ha encontrado un camino
        return None

    #Crea las lineas permanentes
    def drawBackground(self):
        for n in self.nodes:
            valor = self.grafo.grafoDiccionario[n]
            for nod in valor:
                node_origin = n.getXY()
                node_dest = nod.getXY()
                distance = self.calculate_distance(n, nod)
                self.drawEdge(node_origin[0], node_origin[1], node_dest[0], node_dest[1], "#FFFFFF")
                self.drawDistanceLabel((node_origin[0] + node_dest[0]) / 2, (node_origin[1] + node_dest[1]) / 2, distance)

#Escribe la distancia de los nodos
    def drawDistanceLabel(self, x, y, distance):
        self.app.img_frame.create_text(x, y, text=f"{distance:.2f}", fill="#34495E")
#Calcula la distancia de los nodos
    def calculate_distance(self, vertex1, vertex2):
        x1, y1 = vertex1.getXY()
        x2, y2 = vertex2.getXY()
        distance = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
        return distance

#Creacion de Aristas
    def drawPath(self, path, color):
        if path[0] != None:
            start = path[0]
            for fs in range(1,len(path)):
                node_origin = start.getXY()
                node_dest = path[fs].getXY()
                self.drawEdge(node_origin[0], node_origin[1], node_dest[0], node_dest[1], color)
                start = path[fs]
        else:
            print("esta vacia")

    def drawEdge(self, x1, y1, x2, y2, color):
        self.app.img_frame.create_line(x1, y1, x2, y2, fill=color, width=3)

#Creacion de Nodos
    def draw_Nodes(self):
        self.nodes
        for nod in self.nodes:
            node = nod.getXY()
            node_id = nod.getName()
            (x, y) = node
            self.app.img_frame.create_oval(x - 5, y - 5, x + 5, y + 5, fill="orange")
            self.app.img_frame.create_text(x, y, text=node_id)

#Funcion de el boton limpieza
    def clear(self):
        self.drawBackground()
        self.draw_Nodes()
