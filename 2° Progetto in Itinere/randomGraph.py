import random

def generateRandomGraph(numNodes, numEdges, strutturaDati):

    #strutturaDati deve essere
    #GraphAdjacencyList
    #GraphAdjacencyMatrix
    #GraphIncidenceList

    if numEdges > numNodes:
        print("Errore, il numero di nodi non può essere minore del numero degli archi")
        return 0

    graph = strutturaDati()
    nodes = []
    heads = []

    for k in range(1, numNodes):
        graph.addNode(k)
        nodes.append(k)

    for j in range(1, numEdges):
        a = random.choice(nodes)
        b = random.choice(nodes)
        if (a != b and b not in heads):
            heads.append(b)
            graph.insertEdge(a, b)
            #graph.insertEdge(b,a) -> Togliere il commento se il grafo non è orientato
    for i in graph.getEdges():
        print(i)