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

    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
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
        self.nodes = {}  # dictionary {nodeId: node}
        self.nextId = 0  # the next node ID to be assigned

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
        newNode = Node(elem, elem)
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
    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
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

    def backToFather(self, rootID):

        percorso = []  # La lista dei nodi appartenenti al percorso più lungo
        while (rootID.father != None and rootID != int):  # Fin quando il nodo che sto considerando ha un padre,
            percorso.append(rootID.info)  # aggiungo il padre alla lista dei nodi appartenenti al percorso,
            rootID = rootID.father  # imposto il padre come nuovo nodo

        if len(percorso) < 3:  # Se ho meno di tre elementi nel percorso, nessun nodo risulta medio
            return "Nessun nodo risulta medio"

        if (len(
                percorso) % 2) == 0:  # Se il numero di elementi è pari, devo controllare quale dei due elementi ha il maggior numero di figli

            # Ottengo i due elementi medi nella lista
            primoElemento = percorso[int(len(percorso) / 2)]
            secondoElemento = percorso[int((len(percorso) / 2) + 1)]

            # Elimino l'arco che collega i due nodi, in modo da poter eseguire due visite separate
            self.deleteEdge(primoElemento, secondoElemento)
            self.deleteEdge(secondoElemento, primoElemento)

            first = self.calculateSubNode(primoElemento)  # Numero di nodi figli del primo elemento
            second = self.calculateSubNode(secondoElemento)  # Numero di nodi figli del secondo elemento

            if first < second:
                return "Il nodo che risulta medio per il maggior numero di coppie di nodi è", secondoElemento
            elif second > first:
                return "Il nodo che risulta medio per il maggior numero di coppie di nodi è", primoElemento
            else:
                return "I nodi che risultano medi per il maggior numero di coppie di nodi sono:", primoElemento, secondoElemento
        else:
            return "Il nodo che risulta medio per il maggior numero di coppie di nodi è", percorso[
                int(len(percorso) / 2)]

    def calculateSubNode(self, rootId):
        """
        Execute a generic search in the graph starting from the specified node.
        :param rootId: the root node ID (integer).
        :return: the generic exploration tree.
        """

        counter = 0  # Contatore degli elementi figli del nodo

        # Utilizzo l'algoritmo per la visita generica visto a lezione
        if rootId not in self.nodes:
            return None

        treeNode = TreeNode(rootId)
        vertexSet = {treeNode}
        markedNodes = {rootId}

        while len(vertexSet) > 0:
            treeNode = vertexSet.pop()
            adjacentNodes = self.getAdj(treeNode.info)
            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:
                    counter = counter + 1  # Incremento il contatore
                    newTreeNode = TreeNode(nodeIndex)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)
        return counter

    def controlloFunzione(self):

        nodi = []
        for nodo in (self.getNodes()):
            if len(self.getAdj(nodo.id)) != 0:
                nodi.append(nodo.id)
        print(nodi)

    def mediumNode(self, rootId):
        """
        Execute a generic search in the graph starting from the specified node.
        :param rootId: the root node ID (integer).
        :return: the generic exploration tree.
        """
        max = [0, 0, 0]  # Inizializzo a 0 le informazioni riguardo al nodo massimo

        # Utilizzando l'algoritmo per la visita generica visto a lezione, scansiono l'albero
        if rootId not in self.nodes:
            return None

        treeNode = TreeNode(rootId)
        vertexSet = {treeNode}
        markedNodes = {rootId}

        while len(vertexSet) > 0:
            treeNode = vertexSet.pop()
            adjacentNodes = self.getAdj(treeNode.info)

            if len(
                    adjacentNodes) == 1:  # Se il nodo che sto considerando ha solamente un nodo adiacente, dunque è una foglia:
                lunghezzaPercorso = self.leafDistance(
                    treeNode.info)  # Calcolo la lunghezza del percorso massimo raggiungibile dalla foglia
                if lunghezzaPercorso[0] > max[
                    0]:  # Se il percorso è più lungo dell'attuale massimo, imposto i valori della foglia
                    max[0] = lunghezzaPercorso[0]
                    max[1] = lunghezzaPercorso[1]

            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)

        if max[1] != 0:
            return self.backToFather(max[1])
        else:
            return "Nessun nodo risulta medio"

    def leafDistance(self, rootId):
        """
        Execute a generic search in the graph starting from the specified node.
        :param rootId: the root node ID (integer).
        :return: the generic exploration tree.
        """

        lunghezzaPercorso = [0, 0]
        # lunghezzaPercorso[0] = distanza del nodo dalla radice
        # lunghezzaPercorso[1] = nodo

        # Eseguo una visita generica utilizzando l'algoritmo visto a lezione
        if rootId not in self.nodes:
            return None

        treeNode = TreeNode(rootId)
        vertexSet = {treeNode}
        markedNodes = {rootId}

        while len(vertexSet) > 0:
            treeNode = vertexSet.pop()
            adjacentNodes = self.getAdj(treeNode.info)

            if len(
                    adjacentNodes) == 1:  # Quando trovo una foglia, controllo la sua distanza dalla foglia considerata in questo caso come radice
                if lunghezzaPercorso[
                    0] < treeNode.distanza:  # Se la foglia ha una distanza superiore a quella dell'attuale percorso, imposto i nuovi valori
                    lunghezzaPercorso[0] = treeNode.distanza
                    lunghezzaPercorso[1] = treeNode
                elif lunghezzaPercorso[0] == treeNode.distanza:
                    lunghezzaPercorso[0] = treeNode.distanza
                    lunghezzaPercorso[1] = treeNode

            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    newTreeNode.distanza = treeNode.distanza + 1  # Incremento la distanza del nodo
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)

        return lunghezzaPercorso  # Restituisco la lista con i valori

    def genericSearch(self, rootId):
        """
        Execute a generic search in the graph starting from the specified node.
        :param rootId: the root node ID (integer).
        :return: the generic exploration tree.
        """
        if rootId not in self.nodes:
            return None

        treeNode = TreeN.ode(rootId)
        tree = Tree(treeNode)
        vertexSet = {treeNode}  # nodes to explore
        markedNodes = {rootId}  # nodes already explored

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
        return tree

    def bfs(self, rootId):
        """
        Execute a Breadth-First Search (BFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the BFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        # BFS nodes initialization
        bfs_nodes = []

        # queue initialization
        q = Queue()
        q.enqueue(rootId)

        explored = {rootId}  # nodes already explored

        while not q.isEmpty():  # while there are nodes to explore ...
            node = q.dequeue()  # get the node from the queue
            explored.add(node)  # mark the node as explored
            # add all adjacent unexplored nodes to the queue
            for adj_node in self.getAdj(node):
                if adj_node not in explored:
                    q.enqueue(adj_node)
            bfs_nodes.append(node)

        return bfs_nodes

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

    @abstractmethod
    def print(self):
        """
        Print the graph.
        :return: void.
        """
        ...


if __name__ == "__main__":
    graph = GraphBase()  # error due to the instantiation of an abstract class
