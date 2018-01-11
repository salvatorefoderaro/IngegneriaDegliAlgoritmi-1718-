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
    return graph

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
    print(graph.controlloFunzione())
    end = time.time()
    print("demoCasoMigliore\nIl tempo impiegato è:", end - start, "\nIl numero di archi è:", int(len(graph.getEdges())/ 2), "\nIl numero di nodi è:", len(graph.getNodes()), "\n")


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
        print(graph.controlloFunzione())
        end = time.time()
        print("demoCasoMedio\nIl tempo impiegato è:", end-start,"\nIl numero di archi è:", int(len(graph.getEdges())/2),"\nIl numero di nodi è:", len(graph.getNodes()), "\n")



def demoCasoPeggiore(numNodes, strutturaDati):

        graph = strutturaDati()
        nodes = []

        for k in range(1, numNodes):
            graph.addNode(k)
            nodes.append(k)

        """for i in range(2, numNodes):
                graph.insertEdge(1,i)
                graph.insertEdge(i,1)

        """
        graph.insertEdge(1,2)
        graph.insertEdge(1,8)
        graph.insertEdge(8,5)
        graph.insertEdge(1,4)
        graph.insertEdge(4,6)
        graph.insertEdge(1,3)
        graph.insertEdge(3,7)
        graph.insertEdge(2,9)

        graph.insertEdge(2,1)
        graph.insertEdge(8,1)
        graph.insertEdge(5,8)
        graph.insertEdge(4,1)
        graph.insertEdge(6,4)
        graph.insertEdge(3,1)
        graph.insertEdge(7,3)
        graph.insertEdge(9,2)

        graph.addNode(numNodes)
        nodes.append(numNodes)

        start = time.time()
        print(graph.controlloFunzione())
        end = time.time()
        print("demoCasoPeggiore\nIl tempo impiegato è:", end-start,"\nIl numero di archi è:", int(len(graph.getEdges())/2),"\nIl numero di nodi è:", len(graph.getNodes()),"\n")

if __name__ == "__main__":

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

        demoCasoMedio(100, GraphAdjacencyList)
        demoCasoMedio(200, GraphAdjacencyList)
        demoCasoMedio(500, GraphAdjacencyList)
        demoCasoMedio(1000, GraphAdjacencyList)
        demoCasoMedio(2000, GraphAdjacencyList)
        demoCasoMedio(3000, GraphAdjacencyList)
        demoCasoMedio(4000, GraphAdjacencyList)
        demoCasoMedio(5000, GraphAdjacencyList)
        demoCasoMedio(6000, GraphAdjacencyList)
        demoCasoMedio(7500, GraphAdjacencyList)
        demoCasoMedio(10000, GraphAdjacencyList)

        demoCasoMigliore(100, GraphAdjacencyList)
        demoCasoMigliore(200, GraphAdjacencyList)
        demoCasoMigliore(500, GraphAdjacencyList)
        demoCasoMigliore(1000, GraphAdjacencyList)
        demoCasoMigliore(2000, GraphAdjacencyList)
        demoCasoMigliore(3000, GraphAdjacencyList)
        demoCasoMigliore(4000, GraphAdjacencyList)
        demoCasoMigliore(5000, GraphAdjacencyList)
        demoCasoMigliore(6000, GraphAdjacencyList)
        demoCasoMigliore(7500, GraphAdjacencyList)
        demoCasoMigliore(10000, GraphAdjacencyList)