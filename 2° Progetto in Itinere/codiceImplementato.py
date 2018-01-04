def getRoot(self):
    """
    Questa funzione, dato un grafo non orientato ed aciclico, restituisce i nodi che non hanno archi entranti.
    :param self:
    :return: lista dei nodi senza archi in entrata
    """
    edges = self.getEdges()  # Ottengo la lista degli archi
    nodes = self.getNodes()  # Ottengo la lista dei nodi
    listaTeste = []
    listaRoot = []
    for i in edges:
        listaTeste.append(i.head)  # Per ogni arco, aggiungo alla lista il nodo di testa
    for j in nodes:
        if j.id not in listaTeste:  # Se il nodo che sto considerando non è in lista, allora non ha nessun arco in entrata
            listaRoot.append(j.id)  # Essendo un grafo aciclico non orientato, è unico
    return listaRoot  # Restituisco il nodo radice dell'albero


def mediumNode(self):
    """
    Questa funzione restituisce la lista dei nodi che risultano medi il maggior numero di volte

    :param
    int rootId: ID della radice dell'albero
    :return
    nodeMax: Nodo (o lista nodi) massimo per il maggior numero di volte
    """

    # Come per la visita generica, scorro l'albero ed accedo ad ogni nodo
    rootList = self.getRoot()
    nodeMax = [0]  # Nodo che risulta medio il maggior numero di volte
    max = 0  # Numero di volte che nodeMax risulta medio
    for rootId in rootList:

        if rootId not in self.nodes:  # Se il nodo che sto considerando come radice non appartiene al grafo, restituisco None
            return None

        treeNode = TreeNode(rootId)  # Creo un nuovo nodo
        vertexSet = {treeNode}  # Nodi da visitare
        markedNodes = {rootId}  # Nodi visitati

        while len(vertexSet) > 0:  # Fin quando ho dei nodi ancora non esplorati,
            treeNode = vertexSet.pop()  # considero un nodo che devo ancora visitare
            adjacentNodes = self.getAdj(treeNode.info)  # Ottengo i nodi adiacenti al nodo
            for nodeIndex in adjacentNodes:  # Per ogni nodo adiacente,
                if nodeIndex not in markedNodes:  # controllo se risulta visitato o meno. In caso non risulti visitato:
                    newTreeNode = TreeNode(nodeIndex)  # Creo un nuovo nodo
                    newTreeNode.father = treeNode  # Assegno il nodo come figlio del nodo che sto considerando
                    treeNode.sons.append(newTreeNode)  # Aggiungo il nodo alla lista dei figli del nodo padre
                    vertexSet.add(newTreeNode)  # Aggiungo il nodo alla lista dei nodi da visitare
                    markedNodes.add(nodeIndex)  # Aggiungo il nodo alla lista dei nodi visitati
                    newTreeNode.distanza = treeNode.distanza + 1  # Incrementa la distanza del nodo dalla radice
                    mediumNodo = self.calculateMediumValue(newTreeNode.info,
                                                           newTreeNode.distanza)  # Calcola il numero di volte che il nodo risulta medio
                    print("mediumNodo è: ", mediumNodo, "mentre Max è:", max)
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

    treeNode = TreeNode(rootId)  # Creo un nuovo nodo
    vertexSet = {treeNode}  # Nodi da visitare
    markedNodes = {rootId}  # Nodi visitati

    while len(vertexSet) > 0:  # Fin quando ho dei nodi ancora non esplorati,

        treeNode = vertexSet.pop()  # considero un nodo che devo ancora visitare
        adjacentNodes = self.getAdj(treeNode.info)  # Ottengo i nodi adiacenti al nodo

        # Se la distanza del nodo dalla radice è uguale alla distanza del nodo stesso dalla radice
        if treeNode.distanza == distanzaNodo:
            i = i + treeNode.distanza

        # Se non ci sono più nodi adiacenti
        elif not adjacentNodes:
            i = i + treeNode.distanza

        else:
            for nodeIndex in adjacentNodes:  # Per ogni nodo adiacente,
                if nodeIndex not in markedNodes:  # controllo se risulta visitato o meno. In caso non risulti visitato:
                    newTreeNode = TreeNode(nodeIndex)  # Creo un nuovo nodo
                    newTreeNode.father = treeNode  # Assegno il nodo come figlio del nodo che sto considerando
                    treeNode.sons.append(newTreeNode)  # Aggiungo il nodo alla lista dei figli del nodo padre
                    vertexSet.add(newTreeNode)  # Aggiungo il nodo alla lista dei nodi da visitare
                    markedNodes.add(nodeIndex)  # Aggiungo il nodo alla lista dei nodi visitati
                    newTreeNode.distanza = treeNode.distanza + 1  # Incrementa la distanza del nodo dalla radice

    return i  # Restituisco il numero di volte che il nodo risulta medio