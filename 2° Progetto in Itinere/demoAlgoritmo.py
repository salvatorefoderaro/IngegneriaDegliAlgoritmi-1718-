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
    valori = [0, 1000, 10000, 100000, 1000000]

    for k in valori:
        nodes = []
        for i in range(1, k):
            node = graph.addNode(i)
            nodes.append(node)

        for j in range(1,int(k/4)):
            graph.insertEdge(j,j+1)

        for m in range(int((k/4)+1), int(k/2)):
            graph.insertEdge(m,m+1)

        for n in range(int((k/2)+1), int(3*(k/4))):
            graph.insertEdge(n,n+1)

        for p in range(int(3*(k/4)+1), k):
            graph.insertEdge(p,p+1)




        start = time.time()
        print("La lista delle radici è:", graph.getRoot())
        print("I nodi medi sono:", graph.mediumNode())
        end = time.time()
        print("Il tempo impiegato è:", end - start)

if __name__ == "__main__":


    demoProgetto(GraphAdjacencyList)
    # demoProgetto(GraphIncidenceList)
