def mediumNode(self, rootId):
    """
    Questa funzione, dato in input l'ID della radice di un albero, restituisce il nodo che risulta medio per il maggior
    numero di volte

    :param
    int rootId: ID della radice dell'albero
    :return
    nodeMax: Nodo (o lista nodi) massimo per il maggior numero di volte
    """

    # Come per la visita generica, scorro l'albero ed accedo ad ogni nodo

    if rootId not in self.nodes:
        return None

    treeNode = TreeNode(rootId)
    # tree = Tree(treeNode)
    vertexSet = {treeNode}
    markedNodes = {rootId}
    j = 0
    nodeMax = [0]
    max = 0

    while len(vertexSet) > 0:
        treeNode = vertexSet.pop()
        adjacentNodes = self.getAdj(treeNode.info)
        for nodeIndex in adjacentNodes:
            if nodeIndex not in markedNodes:
                newTreeNode = TreeNode(nodeIndex)
                newTreeNode.father = treeNode
                treeNode.sons.append(newTreeNode)
                vertexSet.add(newTreeNode)
                markedNodes.add(nodeIndex)
                newTreeNode.distanza = treeNode.distanza + 1  # Incrementa la distanza del nodo
                mediumNodo = self.calculateMediumValue(newTreeNode.info,
                                                       newTreeNode.distanza)  # Calcola il numero di volte che il nodo risulta medio
                if mediumNodo == max:  # Se il valore corrisponde a quello dell'attuale nodo massimo,
                    nodeMax.append(newTreeNode.info)  # aggiungi alla lista dei nodi massimi il nodo
                elif mediumNodo > max:  # Se il valore risulta superiore a quello dell'attuale nodo massimo,
                    nodeMax = [0]  # azzera la lista dei nodi massimi
                    max = mediumNodo  # Imposta il valore del nuovo nodo massimo
                    nodeMax[0] = newTreeNode.info  # Imposta il nodo come nodo massimo

    if nodeMax[0] == 0:
        return 0  # Se nessun nodo è medio almeno una volta, restituisco 0
    else:
        return nodeMax  # Restituisco l'ID del nodo


def calculateMediumValue(self, rootId, distanzaNodo):
    """
    Questa funzione, dato in input l'ID di un Nodo e la sua distanza dalla radice, restituisce il numero di volte
    che il nodo stesso risulta medio per una coppia di nodi

    :param
    int rootId: ID del nodo
    :param
    int distanzaNodo: Distanza del nodo dalla radice
    :return
    int i: Numero di volte che il nodo risulta medio
    """
    if rootId not in self.nodes:
        return 0

    i = 0  # Contatore del numero di volte che il nodo risulta medio

    treeNode = TreeNode(rootId)
    # tree = Tree(treeNode)
    vertexSet = {treeNode}
    markedNodes = {rootId}

    while len(vertexSet) > 0:  # while there are nodes to explore ...

        treeNode = vertexSet.pop()  # get an unexplored node
        adjacentNodes = self.getAdj(treeNode.info)

        # Se la distanza del nodo dalla radice è uguale alla distanza del nodo stesso dalla radice
        if treeNode.distanza == distanzaNodo:
            i = i + treeNode.distanza

        # Se non ci sono più nodi adiacenti
        elif not adjacentNodes:
            i = i + treeNode.distanza

        else:
            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    newTreeNode.distanza = treeNode.distanza + 1
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)
    return i  # Restituisco il numero di volte che il nodo risulta medio