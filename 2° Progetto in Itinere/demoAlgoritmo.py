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

    start = time.time()
    graph.controlloFunzione()
    end = time.time()
    print("\nIl tempo impiegato è:", end-start)

if __name__ == "__main__":

    for k in range (1,6):

         """generateRandomGraph(500, 500, GraphAdjacencyList)
         generateRandomGraph(1000, 1000, GraphAdjacencyList)
         generateRandomGraph(2000, 2000, GraphAdjacencyList)
         generateRandomGraph(5000, 5000, GraphAdjacencyList)
         generateRandomGraph(10000, 10000, GraphAdjacencyList)
         generateRandomGraph(20000, 20000, GraphAdjacencyList)
         generateRandomGraph(50000, 50000, GraphAdjacencyList)
         generateRandomGraph(100000, 100000, GraphAdjacencyList)"""
         generateRandomGraph(200000, 200000, GraphAdjacencyList)
         generateRandomGraph(500000, 500000, GraphAdjacencyList)
         generateRandomGraph(1000000, 1000000, GraphAdjacencyList)