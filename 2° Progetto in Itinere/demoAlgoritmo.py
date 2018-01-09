from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
import time
import random


def generateRandomGraph(numNodes, numEdges, strutturaDati):

    if numEdges > numNodes:
        print("Errore, il numero di nodi non può essere minore del numero degli archi")
        return 0

    graph = strutturaDati()
    nodes = []
    heads = []

    for k in range (1,numNodes):
        graph.addNode(k)
        nodes.append(k)

    for j in range (1, numEdges):
        a = random.choice(nodes)
        b = random.choice(nodes)
        if (a != b and b not in heads):
            heads.append(b)
            graph.insertEdge(a,b)
            graph.insertEdge(b,a)

    print("Funzione!")
    start = time.time()
    print(graph.controlloFunzione())
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    for k in range(1, 3):
         generateRandomGraph(10000, 7000, GraphAdjacencyList)
         generateRandomGraph(50000, 35000, GraphAdjacencyList)
         generateRandomGraph(100000, 70000, GraphAdjacencyList)
