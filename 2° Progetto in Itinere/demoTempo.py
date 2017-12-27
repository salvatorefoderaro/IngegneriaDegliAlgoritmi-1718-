from Graph import GraphBase
from base import Edge, Node
from tree.treeArrayList import TreeArrayListNode as TreeNode
from tree.treeArrayList import TreeArrayList as Tree
from queue.Queue import CodaArrayList_deque as Queue
from stack.Stack import PilaArrayList as Stack
from list.DoubleLinkedList import ListaDoppiamenteCollegata as List
import time
from Graph_AdjacencyList import GraphAdjacencyList
from Graph_AdjacencyMatrix import GraphAdjacencyMatrix
from Graph_IncidenceList import GraphIncidenceList
from datetime import datetime


def demoTempo(numeroEsecuzioni):
    """
    :param self:
    :param strutturaDati:
    :return:
    """

    graph = GraphIncidenceList()

    nodes = []
    for i in range(numeroEsecuzioni):
        node = graph.addNode(i)
        nodes.append(node)
    for i in range(numeroEsecuzioni):
        graph.insertEdge(0, i)
    start = time.time()
    graph.mediumNodeBack(0)
    end = time.time()
    elapsed = (end - start)
    return elapsed



if __name__ == "__main__":
    for i in range (6):
            print("\nEsecuzione numero ", i)
            print(demoTempo(100))
            print( demoTempo(250))
            print(demoTempo(500))
            print( demoTempo(1000))
            print(demoTempo(2500))
            print( demoTempo(5000))
            print(demoTempo(10000))
            print(demoTempo(15000))
            print(demoTempo(25000))
            print(demoTempo(50000))