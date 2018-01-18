"""
    File name: demoAlgoritmo.py
    Author: Salvatore Foderaro, Alberto Menichelli, Giorgia Di Blasi
    Date created: 23/12/2017
    Modified By: Salvatore Foderaro
    Date last modified: 18/01/2018
    Python Version: 3.6.3

    Questo modulo implementa diverse funzioni per creare i grafi descritti nella relazione del progetto.
"""


from graphFile.Graph_AdjacencyList import GraphAdjacencyList
from graphFile.Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from graphFile.Graph_IncidenceList import GraphIncidenceList
import random


def createRandomGraph(numNodes, strutturaDati=GraphAdjacencyList):
    """"
    Questa funzione genera un Grafo non orientato ed aciclico, dato in input la struttura dati desiderata
    ed il numero di nodi
    """
    graph = strutturaDati()
    nodes = []
    heads = []
    numEdges = int(4 * numNodes)

    for k in range(1, numNodes+1):
        graph.addNode(k)
        nodes.append(k)

    for j in range(1, numEdges):
        a = random.choice(nodes)
        b = random.choice(nodes)
        controllo1 = graph.getEdge(a,b) # Controllo se è presente un arco (a,b)
        controllo2 = graph.getEdge(b,a) # Controllo se è presente un arco (b,a)
        if (a != b and b not in heads):
            if (controllo1 == None and controllo2 == None):  # Se non è presente nessuno dei due archi tra i due nodi
                heads.append(b)
                graph.insertEdge(a, b)
                graph.insertEdge(b, a)

    graph.addNode(numNodes)
    nodes.append(numNodes)

    return graph

def createBestGraph(numNodes, strutturaDati=GraphAdjacencyList):

    graph = strutturaDati()
    nodes = []

    for k in range(1, numNodes+1):
        graph.addNode(k)
        nodes.append(k)

    for i in range(1, numNodes+1):
        graph.insertEdge(i, i+1)
        graph.insertEdge(i+1, i)

    graph.addNode(numNodes+1)
    nodes.append(numNodes+1)

    return graph

def createWorstGraph(numNodes, strutturaDati=GraphAdjacencyList):
    graph = strutturaDati()
    nodes = []

    for k in range(1, numNodes+1):
        graph.addNode(k)
        nodes.append(k)

    for i in range(2, numNodes+1):
            graph.insertEdge(1,i)
            graph.insertEdge(i,1)

    graph.addNode(numNodes+1)
    nodes.append(numNodes+1)

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

    return graph

if __name__ == "__main__":
    print("---------- GRAFO RANDOM + 1 NODO DISCONNESSO ----------")
    grafo = createRandomGraph(100)
    print("\nNumero di nodi:", len(grafo.getNodes()),"\nNumero di archi:", int(len(grafo.getEdges())/2),"\nLa lista dei nodi medi nel grafo è:", grafo.mediumNode(),"\n")
    print("---------- (N-1)-HEAP + 1 NODO DISCONNESSO ----------")
    grafo = createWorstGraph(100)
    print("\nNumero di nodi:", len(grafo.getNodes()),"\nNumero di archi:", int(len(grafo.getEdges())/2),"\nLa lista dei nodi medi nel grafo è:", grafo.mediumNode(),"\n")
    print("---------- 1-HEAP + 1 NODO DISCONNESSO")
    grafo = createBestGraph(100)
    print("\nNumero di nodi:", len(grafo.getNodes()),"\nNumero di archi:", int(len(grafo.getEdges())/2),"\nLa lista dei nodi medi nel grafo è:", grafo.mediumNode(),"\n")
    print("---------- GRAFO FIGURA 2 RELAZIONE ----------")
    grafo = createRelationGraphPari()
    print("\nNumero di nodi:", len(grafo.getNodes()),"\nNumero di archi:", int(len(grafo.getEdges())/2),"\nLa lista dei nodi medi nel grafo è:", grafo.mediumNode(),"\n")
    print("---------- GRAFO FIGURA 1 RELAZIONE ----------")
    grafo = createRelationGraphDispari()
    print("\nNumero di nodi:", len(grafo.getNodes()),"\nNumero di archi:", int(len(grafo.getEdges())/2),"\nLa lista dei nodi medi nel grafo è:", grafo.mediumNode(),"\n")
