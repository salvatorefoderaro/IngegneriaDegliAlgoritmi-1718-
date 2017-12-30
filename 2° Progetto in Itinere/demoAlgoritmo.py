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

    print("Creo i nodi")
    for i in range(1, 5000000):
        node = graph.addNode(i)
        nodes.append(node)

    print("Inserisco gli archi")
    for j in range(1, 2000000):
        graph.insertEdge(j,(j*5))
        graph.insertEdge(j, (j*5)+1)
        graph.insertEdge(j, (j*5)+2)
        graph.insertEdge(j, (j*5)+3)
        graph.insertEdge(j, (j*5)+4)



    print("Eseguo la funzione")
    start = time.time()
    print(graph.mediumNode(1))
    end = time.time()
    print(end - start)

if __name__ == "__main__":


    demoProgetto(GraphAdjacencyList)
