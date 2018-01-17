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

def createRelationGraphDispari(strutturaDati=GraphAdjacencyList):

    graph = strutturaDati()
    nodes = []

    for k in range(1, 10):
        graph.addNode(k)
        nodes.append(k)


    graph.insertEdge(1,2)
    graph.insertEdge(2,1)

    graph.insertEdge(1,3)
    graph.insertEdge(3,1)
    graph.insertEdge(3,7)
    graph.insertEdge(7,3)
    graph.insertEdge(1,4)
    graph.insertEdge(4,1)
    graph.insertEdge(4,6)
    graph.insertEdge(6,4)
    graph.insertEdge(1,8)
    graph.insertEdge(8,1)
    graph.insertEdge(8,5)
    graph.insertEdge(5,8)



    graph.addNode(k)
    nodes.append(k)

    return graph

def createRelationGraphPari(strutturaDati=GraphAdjacencyList):

    graph = strutturaDati()
    nodes = []

    for k in range(1, 20):
        graph.addNode(k)
        nodes.append(k)


    graph.insertEdge(10,12)
    graph.insertEdge(12,10)

    graph.insertEdge(10,9)
    graph.insertEdge(9,10)

    graph.insertEdge(12,13)
    graph.insertEdge(13,12)

    graph.insertEdge(9,14)
    graph.insertEdge(14,9)

    graph.insertEdge(9,8)
    graph.insertEdge(8,9)

    graph.insertEdge(9,15)
    graph.insertEdge(15,9)

    graph.insertEdge(13,11)
    graph.insertEdge(11,13)

    graph.insertEdge(13,16)
    graph.insertEdge(16,13)





    graph.addNode(k)
    nodes.append(k)

    return graph

if __name__ == "__main__":

    grafo = createRelationGraphPari(GraphAdjacencyList)
    print("Il numero di nodi appartenenti al grafo è:", grafo.numNodes(),"\nIl numero di archi appartenenti al grafo è:", int(grafo.numEdges()/2),
          "\nIl nodo (nodi) medio è:", grafo.mediumNode())
