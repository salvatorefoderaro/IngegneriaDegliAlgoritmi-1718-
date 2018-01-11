from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
import time
import random
import os

def demoCasoMigliore(numNodes, strutturaDati):

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

    start = time.time()
    graph.controlloFunzione()
    end = time.time()
    print("\ndemoCasoMigliore\nIl tempo impiegato è:", end - start, "\nIl numero di archi è:", int(len(graph.getEdges()) / 2),
          "\nIl numero di nodi è:", len(graph.getNodes()))


def demoCasoMedio(numNodes, strutturaDati):

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


        start = time.time()
        graph.controlloFunzione()
        end = time.time()
        print("\ndemoCasoMedio\nIl tempo impiegato è:", end-start,"\nIl numero di archi è:", int(len(graph.getEdges())/2),"\nIl numero di nodi è:", len(graph.getNodes()))



def demoCasoPeggiore(numNodes, strutturaDati):

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

        start = time.time()
        print(graph.controlloFunzione())
        end = time.time()
        print("\ndemoCasoPeggiore\nIl tempo impiegato è:", end-start,"\nIl numero di archi è:", int(len(graph.getEdges())/2),"\nIl numero di nodi è:", len(graph.getNodes()))

if __name__ == "__main__":




        demoCasoMedio(100, GraphAdjacencyList)
        demoCasoMigliore(100, GraphAdjacencyList)

        demoCasoMedio(250, GraphAdjacencyList)
        demoCasoMigliore(250, GraphAdjacencyList)

        demoCasoMedio(500, GraphAdjacencyList)
        demoCasoMigliore(500, GraphAdjacencyList)

        demoCasoMedio(750, GraphAdjacencyList)
        demoCasoMigliore(750, GraphAdjacencyList)

        demoCasoMedio(1000, GraphAdjacencyList)
        demoCasoMigliore(1000, GraphAdjacencyList)

        demoCasoMedio(2000, GraphAdjacencyList)
        demoCasoMigliore(2000, GraphAdjacencyList)
        demoCasoMedio(3000, GraphAdjacencyList)
        demoCasoMigliore(3000, GraphAdjacencyList)
        demoCasoMedio(4000, GraphAdjacencyList)
        demoCasoMigliore(4000, GraphAdjacencyList)
        demoCasoMedio(5000, GraphAdjacencyList)
        demoCasoMigliore(5000, GraphAdjacencyList)
        demoCasoMedio(6000, GraphAdjacencyList)
        demoCasoMigliore(6000, GraphAdjacencyList)
        demoCasoMedio(7000, GraphAdjacencyList)
        demoCasoMigliore(7000, GraphAdjacencyList)


        demoCasoPeggiore(100, GraphAdjacencyList)
        demoCasoPeggiore(200, GraphAdjacencyList)
        demoCasoPeggiore(300, GraphAdjacencyList)
        demoCasoPeggiore(400, GraphAdjacencyList)
        demoCasoPeggiore(500, GraphAdjacencyList)
        demoCasoPeggiore(600, GraphAdjacencyList)
        demoCasoPeggiore(700, GraphAdjacencyList)
        demoCasoPeggiore(800, GraphAdjacencyList)
        demoCasoPeggiore(900, GraphAdjacencyList)
        demoCasoPeggiore(1000, GraphAdjacencyList)