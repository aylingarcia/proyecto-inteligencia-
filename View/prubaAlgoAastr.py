import heapq
import math

from Model.GrafoNoDirigido import GrafoNoDirigido
from Model.ManagerFile import ManagerFile


def buscar_camino_astar(grafo, nodo_inicio, nodo_objetivo):
    # Función heurística (distancia estimada) entre dos nodos
    def heuristica(nodo_actual, nodo_objetivo):
        x_actual, y_actual = nodo_actual.getXY()
        x_objetivo, y_objetivo = nodo_objetivo.getXY()

        distancia = math.sqrt((x_actual - x_objetivo)**2 + (y_actual - y_objetivo))
        return distancia

    lista_abierta = [(0, nodo_inicio)]
    heapq.heapify(lista_abierta)
    visitados = set()
    padres = {}
    g = {nodo: float('inf') for nodo in grafo.grafoDiccionario}
    g[nodo_inicio] = 0

    while lista_abierta:
        f_actual, nodo_actual = heapq.heappop(lista_abierta)
        if nodo_actual == nodo_objetivo:
            camino = [nodo_actual]
            while nodo_actual in padres:
                nodo_actual = padres[nodo_actual]
                camino.append(nodo_actual)
            camino.reverse()
            return camino

        visitados.add(nodo_actual)

        for vecino in grafo[nodo_actual]:
            if vecino in visitados:
                continue

            g_temp = g[nodo_actual] + 1  # En este caso, consideramos una distancia constante de 1 entre nodos vecinos

            if g_temp < g[vecino]:
                padres[vecino] = nodo_actual
                g[vecino] = g_temp

                h = heuristica(vecino, nodo_objetivo)
                f = g_temp + h

                heapq.heappush(lista_abierta, (f, vecino))

    return None


if __name__ == "__main__":
    manage = ManagerFile()
    grafo = manage.obGrafoSinText(GrafoNoDirigido)
    node = grafo.grafoDiccionario
    nodoini2 = grafo.getVertex('n2')
    nododes4 = grafo.getVertex('n4')

    print(nodoini2)
    print(nododes4)
    var = buscar_camino_astar(grafo, nodoini2, nodoini2)
    for i in var:
        print(i)

"""
def heuristica(nodo_actual, nodo_objetivo):
    # Calcula la distancia Euclidiana entre los nodos actual y objetivo
    x_actual, y_actual = nodo_actual
    x_objetivo, y_objetivo = nodo_objetivo
    distancia = math.sqrt((x_actual - x_objetivo)**2 + (y_actual - y_objetivo)**2)
    return distancia
"""