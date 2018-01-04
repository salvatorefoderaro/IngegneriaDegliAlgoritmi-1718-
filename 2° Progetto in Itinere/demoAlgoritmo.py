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
    print("\n\n")
    valori = [0,5,10,50,75,100, 250, 500, 1000, 2500]

    for k in valori:
        graph = strutturaDati()

        nodes = []
        for i in range(1, k):
            node = graph.addNode(i)
            nodes.append(node)


        for j in range(1, k):
            graph.insertEdge(j, j+1)




        start = time.time()
        graph.mediumNode()
        end = time.time()
        print(end - start)

if __name__ == "__main__":


    # demoProgetto(GraphAdjacencyList)
    # demoProgetto(GraphIncidenceList)
    demoProgetto(GraphAdjacencyMatrix)
