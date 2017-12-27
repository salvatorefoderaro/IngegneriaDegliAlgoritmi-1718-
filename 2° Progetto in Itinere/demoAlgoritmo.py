from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
import time

def demoProgetto(numeroNodi, numeroArchi, strutturaDati):
    """
    :param numeroNodi:
    :param numeroArchi:
    :param strutturaDati: GraphAdjacencyList, GraphAdjacencyMatrix, GraphIncidenceList
    :return:
    """

    graph = strutturaDati()

    nodes = []

    for i in range(1, numeroNodi):
        node = graph.addNode(i)
        nodes.append(node)
    for j in range(1, numeroArchi):
        graph.insertEdge(j,2*j)
        graph.insertEdge(j,(2*j)+1)
    return graph.mediumNode(1)


if __name__ == "__main__":


    print(demoProgetto(30, 8, GraphAdjacencyList))