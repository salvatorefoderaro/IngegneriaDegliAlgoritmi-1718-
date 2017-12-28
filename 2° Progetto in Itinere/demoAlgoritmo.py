from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
import time

def demoProgetto(strutturaDati):
    """
    :param numeroNodi:
    :param numeroArchi:
    :param strutturaDati: GraphAdjacencyList, GraphAdjacencyMatrix, GraphIncidenceList
    :return:
    """

    graph = strutturaDati()

    nodes = []

    for i in range(1, 100000):
        node = graph.addNode(i)
        nodes.append(node)

    for j in range(1, 64):
        graph.insertEdge(j,(j*2))
        graph.insertEdge(j,(j*2)+1)


    print(graph.mediumNode(1))
    """
    start = time.time()
    graph.genericSearch(1)
    end = time.time()
    print(end - start)
    """
if __name__ == "__main__":


    demoProgetto(GraphAdjacencyList)
