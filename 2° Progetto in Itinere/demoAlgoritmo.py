from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
import time
import random


def demoProgettoPeggiore(strutturaDati):
    """
    :param numeroNodi:
    :param numeroArchi:
    :param strutturaDati: GraphAdjacencyList, GraphAdjacencyMatrix, GraphIncidenceList
    :return:
    """

    graph = strutturaDati()
    valori = [0, 50, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]
    tempi = []
	
    for k in valori:
        nodes = []
        for i in range(1, k):
            node = graph.addNode(i)
            nodes.append(node)

        for j in range(1, k):
            graph.insertEdge(1,j)
            graph.insertEdge(j,1)

        # for j in range(1, k):
        #    graph.insertEdge(1,j)
        #    graph.insertEdge(j,1)
        print("Eseguo la funzione")
        start = time.time()
        graph.algoritmoAlberto(int(k / 2))
        end = time.time()
        tempi.append(end-start)

    print(tempi)


def demoProgettoMigliore(strutturaDati):
    """
    :param numeroNodi:
    :param numeroArchi:
    :param strutturaDati: GraphAdjacencyList, GraphAdjacencyMatrix, GraphIncidenceList
    :return:
    """
    tempi = []
    graph = strutturaDati()
    valori = [0, 51, 101, 251, 501, 751, 1001, 2500, 5000, 7500, 10000]

    for k in valori:
        nodes = []
        for i in range(1, k):
            node = graph.addNode(i)
            nodes.append(node)

        for j in range(1, k):
            graph.insertEdge(j, j+1)


            graph.insertEdge(j+1,j)

        # for j in range(1, k):
        #    graph.insertEdge(1,j)
        #    graph.insertEdge(j,1)
        start = time.time()
        graph.mediumNode()
        end = time.time()
        tempi.append(end-start)
    print(tempi)

def demoProgettoMedio(strutturaDati):
    """
    :param numeroNodi:
    :param numeroArchi:
    :param strutturaDati: GraphAdjacencyList, GraphAdjacencyMatrix, GraphIncidenceList
    :return:
    """
    tempi = []
    graph = strutturaDati()
    print("Esecuzione funzione con", strutturaDati)
    valori = [0, 50, 100,250, 500, 750, 1000, 2500, 5000, 7500, 10000]

    for k in valori:
        nodes = []
        for i in range(1, 1000):
            node = graph.addNode(i)
            nodes.append(i)



        for j in range(1,1000):
            graph.insertEdge(j, (j*2))
            graph.insertEdge(j, (j*2)+1)


            graph.insertEdge((j*2), j)
            graph.insertEdge((j*2)  +1, j)
        #for j in range(1, k):
        #    graph.insertEdge(1,j)
        #    graph.insertEdge(j,1)
        start = time.time()
        print(graph.mediumNode(random.choice(nodes)))
        end = time.time()
        tempi.append(end-start)
        print(end-start)
    print(tempi)


if __name__ == "__main__":

    print("Demo progetto medio")
    for m in range (1,6):
        demoProgettoMedio(GraphAdjacencyList)
        #demoProgettoMigliore(GraphAdjacencyList)
        #demoProgettoPeggiore(GraphAdjacencyList)
        # demoProgetto(GraphIncidenceList)