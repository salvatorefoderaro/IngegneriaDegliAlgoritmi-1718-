def controlloFunzione(self):
    nodi = []
    h = 0
    nodoMax = [0, 0]
    for nodo in (self.getNodes()):
        adj = len(self.getAdj(nodo.id))
        if adj != 0:
            while (h < 1):
                if adj == 1:
                    foglia = nodo.id
                    h = 1
            nodi.append(nodo.id)
    print(nodi)
    while len(nodi) > 0:
        # print("Le informazioni riguardo al nodo massimo ed alla distanza del nodo sono", nodoMassimoPercorso)
        nodoMassimo = self.mediumNode(foglia)
        print(nodoMassimo)
        if (nodoMassimo != 0):

            if (nodoMassimo[1] > nodoMax[1]):
                nodoMax[0] = nodoMassimo[0]
                nodoMax[1] = nodoMassimo[1]

        nodi = [x for x in nodi if x not in nodoMassimo[2]]

        return nodoMax[0]


def mediumNode(self, rootId):
    """
    Questa funzione restituisce la lista dei nodi che risultano medi il maggior numero di volte
    :param
    int rootId: ID della radice dell'albero
    :return
    nodeMax: Nodo (o lista nodi) massimo per il maggior numero di volte
    """

    # Come per la visita generica, scorro l'albero ed accedo ad ogni nodo


    if rootId not in self.nodes:  # Se il nodo che sto considerando come radice non appartiene al grafo, restituisco None
        return None

    treeNode = TreeNode(rootId)  # Creo un nuovo nodo
    vertexSet = {treeNode}  # Nodi da visitare
    markedNodes = [rootId]  # Nodi visitati
    max = 0
    nodeMax = [0]

    while len(vertexSet) > 0:  # Fin quando ho dei nodi ancora non esplorati,
        treeNode = vertexSet.pop()  # considero un nodo che devo ancora visitare
        adjacentNodes = self.getAdj(treeNode.info)  # Ottengo i nodi adiacenti al nodo
        for nodeIndex in adjacentNodes:  # Per ogni nodo adiacente,
            if nodeIndex not in markedNodes:  # controllo se risulta visitato o meno. In caso non risulti visitato:
                newTreeNode = TreeNode(nodeIndex)  # Creo un nuovo nodo
                newTreeNode.father = treeNode  # Assegno il nodo come figlio del nodo che sto considerando
                treeNode.sons.append(newTreeNode)  # Aggiungo il nodo alla lista dei figli del nodo padre
                vertexSet.add(newTreeNode)  # Aggiungo il nodo alla lista dei nodi da visitare
                markedNodes.append(nodeIndex)  # Aggiungo il nodo alla lista dei nodi visitati
                newTreeNode.distanza = treeNode.distanza + 1  # Incrementa la distanza del nodo dalla radice
                mediumNodo = self.calculateMediumValue(newTreeNode.info,
                                                       newTreeNode.distanza)  # Calcola il numero di volte che il nodo risulta medio
                print(mediumNodo, max)
                if mediumNodo == max:  # Se il valore corrisponde a quello dell'attuale nodo massimo,
                    nodeMax.append(newTreeNode.info)  # Aggiungo alla lista dei nodi massimi il nodo
                elif mediumNodo > max:  # Se il valore risulta superiore a quello dell'attuale nodo massimo,
                    nodeMax = [0]  # azzera la lista dei nodi massimi
                    max = mediumNodo  # Imposta il valore del nuovo nodo massimo
                    nodeMax[0] = newTreeNode.info  # Imposta il nodo come nodo massimo

    print(nodeMax)
    nodoMassimo = [nodeMax, max, markedNodes]

    if nodeMax[0] == 0:
        return 0  # Se nessun nodo è medio almeno una volta, restituisco 0
    else:
        return nodoMassimo  # Restituisco l'ID del nodo


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

    # Eseguo una visita generica prendendo come radice il nodo considerato

    # queue initialization


    treeNode = TreeNode(rootId)  # Creo un nuovo nodo

    vertexSet = Queue()
    vertexSet.enqueue(treeNode)

    # vertexSet = {treeNode}  # Nodi da visitare
    markedNodes = {rootId}  # Nodi visitati

    while not vertexSet.isEmpty():  # while there are nodes to explore ...
        # while len(vertexSet) > 0:  # Fin quando ho dei nodi ancora non esplorati,

        # treeNode = vertexSet.pop()  # considero un nodo che devo ancora visitare
        treeNode = vertexSet.dequeue()  # get the node from the queue
        print("Considero il nodo", treeNode.info, "Nodi visitati sono", distanzaNodo, "Nodi da visitare",
              treeNode.distanza)

        adjacentNodes = self.getAdj(treeNode.info)  # Ottengo i nodi adiacenti al nodo

        # Se la distanza del nodo dalla radice è uguale alla distanza del nodo stesso dalla radice
        if treeNode.distanza == distanzaNodo:
            i = i + treeNode.distanza

        # Se non ci sono più nodi adiacenti
        elif len(adjacentNodes) == 1:
            i = i + treeNode.distanza


        elif treeNode.distanza > distanzaNodo:
            return i

        else:
            for nodeIndex in adjacentNodes:  # Per ogni nodo adiacente,
                if nodeIndex not in markedNodes:  # controllo se risulta visitato o meno. In caso non risulti visitato:
                    newTreeNode = TreeNode(nodeIndex)  # Creo un nuovo nodo
                    newTreeNode.father = treeNode  # Assegno il nodo come figlio del nodo che sto considerando
                    treeNode.sons.append(newTreeNode)  # Aggiungo il nodo alla lista dei figli del nodo padre
                    # vertexSet.add(newTreeNode)  # Aggiungo il nodo alla lista dei nodi da visitare
                    vertexSet.enqueue(newTreeNode)
                    markedNodes.add(nodeIndex)  # Aggiungo il nodo alla lista dei nodi visitati
                    newTreeNode.distanza = treeNode.distanza + 1  # Incrementa la distanza del nodo dalla radice
    return i  # Restituisco il numero di volte che il nodo risulta medio
