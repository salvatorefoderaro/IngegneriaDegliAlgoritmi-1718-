"""
in tutti e due i casi i codici utilizzati sono quelli della vista generica che ha costo O(n), dove n è il numero dei vertici.
La complessità teorica è di T(n)=O(n)*T(n-1), in quanto eseguo prima una visita generica su tutti i nodi, e per ogni nodo eseguo
una nuova visita che viene eseguita su tutti i nodi, tranne su quello considerato.
"""

def mediumNode(self, rootId):
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
    nodeMax = [0, 0]

    while len(vertexSet) > 0:  # while there are nodes to explore ...
        treeNode = vertexSet.pop()  # Prendi in nodo che non stato ancora visitato
        adjacentNodes = self.getAdj(treeNode.info)
        for nodeIndex in adjacentNodes:
            if nodeIndex not in markedNodes:  # Se il nodo non è stato esplorato...
                newTreeNode = TreeNode(nodeIndex)
                newTreeNode.father = treeNode
                treeNode.sons.append(newTreeNode)
                vertexSet.add(newTreeNode)
                markedNodes.add(nodeIndex)  # Segno il nodo come esplorato
                newTreeNode.distanza = treeNode.distanza + 1  # Incremento la distanza del nodo
                controllo = self.calculateSubNode(newTreeNode.info, newTreeNode.distanza)
                if controllo > nodeMax[1]:  # Se il numero di volte che il nodo considerato è medio è maggiore del massimo procedente
                    nodeMax[1] = controllo  # allora imposto il valore del nodo come nuovo massimo
                    nodeMax[0] = newTreeNode  # ed il nodo come nuovo nodo massimo
    if nodeMax[0] == 0:
        return 0    # Se nessun nodo è medio almeno una volta, restituisco 0
    else:
        return nodeMax[0].info # Restituisco l'ID del nodo


def calculateSubNode(self, rootId, distanzaNodo):
    """
    Questa funzione mi permette, dato in input un Nodo e la sua distanza dalla radice, di determinare il numero di volte
    che il nodo stesso risulta medio.
    
    :param self: Grafo
    :param rootId: ID del nodo
    :param distanzaNodo: Distanza del nodo dalla radice
    :return: Numero di volte che il nodo risulta medio
    """"

    if rootId not in self.nodes:
        return 0

    i = 0   # Contatore che indica il numero di volte che il nodo è risultato medio

    treeNode = TreeNode(rootId)
    tree = Tree(treeNode)
    vertexSet = {treeNode}
    markedNodes = {rootId}  # Nodi già visitati

    while len(vertexSet) > 0:  # while there are nodes to explore ...
        treeNode = vertexSet.pop()  # get an unexplored node
        adjacentNodes = self.getAdj(treeNode.info)

        """
        Se la distanza dal nodo è uguale alla distanza del nodo dalla radice, allora ul numero di volte
        che il nodo considerato risulta medio è uguale alla distanza dal nodo
        
        In questo modo interrompo anche l'iterazione, in quanto anche se gli altri nodi hanno una distanza maggiore,
        devo fare il controllo rispetto alla distanza del nodo dalla radice.
        """

        if treeNode.distanza == distanzaNodo:
            i = i + treeNode.distanza

        """
        Se non ci sono più nodi adiacenti, e se la condizione precedente non è stata soddisfatta,
        allora il numero di volte che il nodo risulta medio è uguale alla distanza dal nodo
        """
        elif not adjacentNodes:
            i = i + treeNode.distanza

        """
        Altrimenti continuo ad iterare
        """
        else:
            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:  # Se il nodo non è stato visitato
                    newTreeNode = TreeNode(nodeIndex) # Creo un nuovo nodo
                    newTreeNode.father = treeNode #
                    newTreeNode.distanza = treeNode.distanza + 1    # Incremento la distanza del nuovo nodo
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)  # Segno il nodo come visitato
    return i