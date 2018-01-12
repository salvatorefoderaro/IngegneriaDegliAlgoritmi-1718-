from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
import time
import random
import os


def createRandomGraph(numNodes, strutturaDati=GraphAdjacencyList):
    """"
    Questa funzione genera un Grafo non orientato ed aciclico, dato in input la struttura dati desiderata
    ed il numero di nodi
    """
    graph = strutturaDati()
    nodes = []
    heads = []
    numEdges = int(4 * numNodes)

    for k in range(1, numNodes):
        graph.addNode(k)
        nodes.append(k)

    for j in range(1, numEdges):
        a = random.choice(nodes)
        b = random.choice(nodes)
        if (a != b):
            if (b not in heads):
                heads.append(b)
                graph.insertEdge(a, b)
                graph.insertEdge(b, a)

    graph.addNode(numNodes)
    nodes.append(numNodes)

    return graph

def createBestGraph(numNodes, strutturaDati=GraphAdjacencyList):

    graph = strutturaDati()
    nodes = []

    for k in range(1, numNodes):
        graph.addNode(k)
        nodes.append(k)

    for i in range(1, numNodes):
        graph.insertEdge(i, i+1)
        graph.insertEdge(i+1, i)

    graph.addNode(numNodes)
    nodes.append(numNodes)

    return graph

def createWorstGraph(numNodes, strutturaDati=GraphAdjacencyList):
    graph = strutturaDati()
    nodes = []

    for k in range(1, numNodes):
        graph.addNode(k)
        nodes.append(k)

    for i in range(2, numNodes):
            graph.insertEdge(1,i)
            graph.insertEdge(i,1)

    graph.addNode(numNodes)
    nodes.append(numNodes)

    return graph

if __name__ == "__main__":

    grafo = createBestGraph(1000,GraphAdjacencyList)
    print("Il numero di nodi appartenenti al grafo è:", grafo.numNodes(),"\nIl numero di archi appartenenti al grafo è:", int(grafo.numEdges()/2),
          "\nIl nodo (nodi) medio è:", grafo.controlloFunzione())
