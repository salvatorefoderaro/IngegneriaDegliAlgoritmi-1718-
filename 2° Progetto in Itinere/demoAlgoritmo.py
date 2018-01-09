from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
import time
import random

def generateRandomGraph(numNodes, numEdges, strutturaDati):
    print("\n", numNodes, "nodi e", numEdges, "archi")

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
        if (a != b):
            if (b not in heads):
                heads.append(b)
                graph.insertEdge(a,b)
                graph.insertEdge(b,a)

    start = time.time()
    graph.controlloFunzione()
    end = time.time()
    print(end - start)

if __name__ == "__main__":

    for k in range (1,4):

         generateRandomGraph(500, 200, GraphAdjacencyList)
         generateRandomGraph(1000, 400, GraphAdjacencyList)
         generateRandomGraph(2000, 800, GraphAdjacencyList)
         generateRandomGraph(5000, 1000, GraphAdjacencyList)
         generateRandomGraph(10000, 2000, GraphAdjacencyList)
         generateRandomGraph(20000, 4000, GraphAdjacencyList)
         generateRandomGraph(50000, 10000, GraphAdjacencyList)
         generateRandomGraph(100000, 20000, GraphAdjacencyList)
         generateRandomGraph(200000, 40000, GraphAdjacencyList)
         generateRandomGraph(500000, 100000, GraphAdjacencyList)

         generateRandomGraph(500, 400, GraphAdjacencyList)
         generateRandomGraph(1000, 800, GraphAdjacencyList)
         generateRandomGraph(2000, 1600, GraphAdjacencyList)
         generateRandomGraph(5000, 4000, GraphAdjacencyList)
         generateRandomGraph(10000, 8000, GraphAdjacencyList)
         generateRandomGraph(20000, 16000, GraphAdjacencyList)
         generateRandomGraph(50000, 40000, GraphAdjacencyList)
         generateRandomGraph(100000, 80000, GraphAdjacencyList)
         generateRandomGraph(200000, 160000, GraphAdjacencyList)
         generateRandomGraph(500000, 400000, GraphAdjacencyList)



