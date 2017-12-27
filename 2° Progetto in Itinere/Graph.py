from abc import ABCMeta, abstractmethod
from base import Node
from tree.treeArrayList import TreeArrayListNode as TreeNode
from tree.treeArrayList import TreeArrayList as Tree
from queue.Queue import CodaArrayList_deque as Queue
from stack.Stack import PilaArrayList as Stack


class Graph:
    """
    Graph interface.
    It shows how to simulate interfaces behaviour in Python.
    """

    def isEmpty(self):
        """
        Check if the graph is empty.
        :return: True, if the graph is empty; False, otherwise.
        """
        raise NotImplementedError("You should have implemented this method!")

    def numNodes(self):
        """
        Return the number of nodes.
        :return: the number of nodes.
        """
        raise NotImplementedError("You should have implemented this method!")

    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        raise NotImplementedError("You should have implemented this method!")

    def addNode(self, elem):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """
        raise NotImplementedError("You should have implemented this method!")

    def deleteNode(self, nodeId):
        """
        Remove the specified node.
        :param nodeId: the node ID (integer).
        :return: void.
        """
        raise NotImplementedError("You should have implemented this method!")



    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        raise NotImplementedError("You should have implemented this method!")

    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        raise NotImplementedError("You should have implemented this method!")

    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        raise NotImplementedError("You should have implemented this method!")

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        raise NotImplementedError("You should have implemented this method!")

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        raise NotImplementedError("You should have implemented this method!")

    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        raise NotImplementedError("You should have implemented this method!")

    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        """
        raise NotImplementedError("You should have implemented this method!")

    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        raise NotImplementedError("You should have implemented this method!")

    def print(self):
        """
        Print the graph.
        :return: void.
        """
        raise NotImplementedError("You should have implemented this method!")


class GraphBase(Graph, metaclass=ABCMeta):
    """
    The basic graph data structure (abstract).
    """

    def __init__(self):
        """
        Constructor.
        """
        self.nodes = {} # dictionary {nodeId: node}
        self.nextId = 0 # the next node ID to be assigned

    def isEmpty(self):
        """
        Check if the graph is empty.
        :return: True, if the graph is empty; False, otherwise.
        """
        return not any(self.nodes)

    def numNodes(self):
        """
        Return the number of nodes.
        :return: the number of nodes.
        """
        return len(self.nodes)

    @abstractmethod
    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        ...

    @abstractmethod
    def addNode(self, elem):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """
        newNode = Node(self.nextId, elem)
        self.nextId += 1
        return newNode

    @abstractmethod
    def deleteNode(self, nodeId):
        """
        Remove the specified node.
        :param nodeId: the node ID (integer).
        :return: void.
        """
        ...



    @abstractmethod
    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        ...

    @abstractmethod
    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        ...

    @abstractmethod
    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        ...

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        ...

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        ...

    @abstractmethod
    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        # Note: this method only checks if tail and head exist
        return False if self.nodes is None else (tail in self.nodes and head in self.nodes)


    @abstractmethod
    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        :rtype: list
        """
        ...

    @abstractmethod
    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        ...

    def genericSearchTotal(self, rootId):
            """
            Execute a generic search in the graph starting from the specified node.
            :param rootId: the root node ID (integer).
            :return: the generic exploration tree.
            """
            if rootId not in self.nodes:
                return None

            treeNode = TreeNode(rootId)
            tree = Tree(treeNode)
            vertexSet = {treeNode}  # nodes to explore
            markedNodes = {rootId}  # nodes already explored
            j = 0
            nodeMax = [0, 0]

            while len(vertexSet) > 0:  # while there are nodes to explore ...
                treeNode = vertexSet.pop()  # get an unexplored node
                adjacentNodes = self.getAdj(treeNode.info)
                for nodeIndex in adjacentNodes:
                    if nodeIndex not in markedNodes:  # if not explored ...
                        newTreeNode = TreeNode(nodeIndex)
                        newTreeNode.father = treeNode
                        treeNode.sons.append(newTreeNode)
                        vertexSet.add(newTreeNode)
                        markedNodes.add(nodeIndex)  # mark as explored
                        newTreeNode.distanza = treeNode.distanza + 1  ### Codici implementati da me e da controllare
                        print("Il nodo che sto considerando è:", newTreeNode.info, "con distanza:", newTreeNode.distanza)
                        controllo = self.genericSearch(newTreeNode.info, newTreeNode.distanza)
                        if controllo > nodeMax[1]:  ### Codici implementati da me e da controllare
                            nodeMax[1] = controllo  ### Codici implementati da me e da controllare
                            nodeMax[0] = newTreeNode  ### Codici implementati da me e da controllare

            print ("Il nodo che è medio per il maggior numero di coppie di nodi è: ", nodeMax[0].info, ", che appare un numero di volte:", nodeMax[1])


    def genericSearch(self, rootId, distanzaNodo):
        """
        Execute a generic search in the graph starting from the specified node.
        :param rootId: the root node ID (integer).
        :return: the generic exploration tree.
        """
        if rootId not in self.nodes:
            return 0

        i = 0

        treeNode = TreeNode(rootId)
        tree = Tree(treeNode)
        vertexSet = {treeNode} # nodes to explore
        markedNodes = {rootId} # nodes already explored

        while len(vertexSet) > 0: # while there are nodes to explore ...
            treeNode = vertexSet.pop() # get an unexplored node
            adjacentNodes = self.getAdj(treeNode.info)

            if treeNode.distanza == distanzaNodo:
                i = i + treeNode.distanza

            elif not adjacentNodes:
                i = i + treeNode.distanza

            else:
                for nodeIndex in adjacentNodes:
                    if nodeIndex not in markedNodes: # if not explored ...
                        newTreeNode = TreeNode(nodeIndex)
                        newTreeNode.father = treeNode
                        newTreeNode.distanza = treeNode.distanza + 1
                        treeNode.sons.append(newTreeNode)
                        vertexSet.add(newTreeNode)
                        markedNodes.add(nodeIndex) # mark as explored

        return i

    def bfs(self, rootId):
        """
        Execute a Breadth-First Search (BFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the BFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            print("Stampa...")
            return None

        # BFS nodes initialization
        bfs_nodes = []

        # queue initialization
        q = Queue()
        q.enqueue(rootId)

        explored = {rootId} # nodes already explored
        print("Stampa...")
        while not q.isEmpty(): # while there are nodes to explore ...
            node = q.dequeue() # get the node from the queue
            explored.add(node) # mark the node as explored
            # add all adjacent unexplored nodes to the queue
            for adj_node in self.getAdj(node):
                adj_node.distanza = node.distanza + 1
                print("La distanza del nodo è:", adj_node.distanza)
                if adj_node not in explored:
                    q.enqueue(adj_node)
            bfs_nodes.append(node)

        return node.distanza

    """

    Root ID e

    """

    def dfsTest(self, rootId):
        """
        Execute a Depth-First Search (DFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the DFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        # DFS nodes initialization
        dfs_nodes = []

        # queue initialization
        s = Stack()
        s.push(rootId)

        explored = {rootId}  # nodes already explored
        distanze = []


        while not s.isEmpty():  # while there are nodes to explore ...
            node = s.pop()  # get the node from the stack
            explored.add(node)  # mark the node as explored
            # add all adjacent unexplored nodes to the stack
            for adj_node in self.getAdj(node):
                if adj_node not in explored:
                    s.push(adj_node)
            dfs_nodes.append(node)

        return dfs_nodes

    def dfs(self, rootId):
        """
        Execute a Depth-First Search (DFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the DFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        # DFS nodes initialization
        dfs_nodes = []

        # queue initialization
        s = Stack()
        s.push(rootId)

        explored = {rootId}  # nodes already explored

        while not s.isEmpty():  # while there are nodes to explore ...
            node = s.pop()  # get the node from the stack
            explored.add(node)  # mark the node as explored
            # add all adjacent unexplored nodes to the stack
            for adj_node in self.getAdj(node):
                if adj_node not in explored:
                    s.push(adj_node)
            dfs_nodes.append(node)

        return dfs_nodes

    """ CODICE MIO """

    def mediumNodeBack(self, rootId):
        """
        Questa funzione, dato in input un nodo di un Grafo non orientato ed aciclico, restituisce il nodo che risulta
        medio il maggior numero di volte.

        :param self: Grafo
        :param rootId:  ID del nodo dal quale partire
        :return: ID del nodo che risulta medio il maggior numero di volte (0 nel caso in cui nessun nodo)
        """

        if rootId not in self.nodes:
            return None

        treeNode = TreeNode(rootId)
        tree = Tree(treeNode)
        vertexSet = {treeNode}  # nodes to explore
        markedNodes = {rootId}  # nodes already explored

        while len(vertexSet) > 0:  # while there are nodes to explore ...
            treeNode = vertexSet.pop()  # Prendi in nodo che non stato ancora visitato
            adjacentNodes = self.getAdj(treeNode.info)

            if not adjacentNodes:
                self.backToRoot(treeNode, treeNode.distanza, tree)

            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:  # Se il nodo non è stato esplorato...
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)  # Segno il nodo come esplorato
                    newTreeNode.distanza = treeNode.distanza + 1  # Incremento la distanza del nodo
        return self.check(tree)

    def backToRoot(self, treeRoot, rootDistance, tree):

        if (treeRoot.father is None):
            treeRoot = treeRoot.father


        while ((rootDistance - treeRoot.distanza) < rootDistance):
            distanzaFoglia = rootDistance - treeRoot.distanza
            if (distanzaFoglia == treeRoot.distanza):
                treeRoot.medium = treeRoot.medium + treeRoot.distanza

            elif ((distanzaFoglia < treeRoot.distanza) and (treeRoot.distanza > 0)):
                treeRoot.medium = treeRoot.medium + distanzaFoglia
            treeRoot = treeRoot.father


    def check(self, tree):
        nodeMax = [0]
        max = 0
        q = Queue()
        if tree.root is not None:
            q.enqueue(tree.root)
        while not q.isEmpty():
            current = q.dequeue()
            for s in current.sons:
                controllo = s.medium
                if controllo == max:
                    nodeMax.append(s.info)
                elif controllo > max:  ### Codici implementati da me e da controllare
                    nodeMax = [0]
                    max = controllo  ### Codici implementati da me e da controllare
                    nodeMax[0] = s.info  ### Codici implementati da me e da controllare
                q.enqueue(s)
        if nodeMax[0] == 0:
            return 0  # Se nessun nodo è medio almeno una volta, restituisco 0
        else:
            return nodeMax  # Restituisco l'ID del nodo



    @abstractmethod
    def print(self):
        """
        Print the graph.
        :return: void.
        """
        ...

if __name__ == "__main__":
    graph = GraphBase() # error due to the instantiation of an abstract class

