from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
import time

def demoProgetto(strutturaDati, numeroEsecuzioni):
    """
    :param numeroNodi:
    :param numeroArchi:
    :param strutturaDati: GraphAdjacencyList, GraphAdjacencyMatrix, GraphIncidenceList
    :return:
    """

    graph = strutturaDati()

    nodes = []

    for i in range(1, numeroEsecuzioni):
        node = graph.addNode(i)
        nodes.append(node)

    for j in range(1, numeroEsecuzioni):
        graph.insertEdge(j,(50*j))
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)
        graph.insertEdge(j,(50*j)+1)











    print("Numero di esecuzioni: ", numeroEsecuzioni)
    start = time.time()
    graph.mediumNodeOld(1)
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    esecuzioni = [0, 5, 10, 50, 75, 100, 250, 500, 1000, 2500, 5000, 10000]
    strutture = [GraphAdjacencyList, GraphIncidenceList]
    for k in strutture:
        print("\n\n Esecuzione con struttura ",k,"\n")
        for m in esecuzioni:
            demoProgetto(k , m)
    esecuzioniMatrice = [0, 5, 10, 50, 75, 100, 250, 500, 1000, 2500, 5000, 10000]
    for h in esecuzioniMatrice:
        print("\n\n Esecuzione con struttura matrice \n\n")
        demoProgetto(GraphAdjacencyMatrix,h)
