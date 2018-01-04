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
    for i in range(1, 10):
        node = graph.addNode(i)
        nodes.append(node)


    graph.insertEdge(1,2)
    graph.insertEdge(2,3)
    graph.insertEdge(3,4)

    graph.insertEdge(5,6)

    graph.insertEdge(7,8)
    graph.insertEdge(8,9)




    start = time.time()
    print("La lista delle radici è:", graph.getRoot())
    print("I nodi medi sono:", graph.mediumNode())
    end = time.time()
    print("Il tempo impiegato è:", end - start)

if __name__ == "__main__":


    demoProgetto(GraphAdjacencyList)
    # demoProgetto(GraphIncidenceList)
