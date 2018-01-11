    def controlloFunzione(self):
        """
        Questa funzione, dato un grafo, restituisce una lista contenente la lista dei nodi massimi ed il numero di volte
        che risultano medi all'interno del grafo.

        :return: restituisco il nodo che risulta massimo nel grafo
        """

        nodi = []  # Lista dei nodi appartenenti al grafo, con almeno un elemento adiacente
        nodeMax = [0, 0]  # Informazioni sul nodo che risulta medio il maggior numero di volte
        for nodo in (self.getNodes()):  # Considero ogni nodo
            if (self.getAdjModified(nodo.id) == 0):
            if (self.getAdjModified(nodo.id) != 0):  # Se il nodo ha almeno un nodo adiacente,
                nodi.append(nodo.id)  # lo aggiungo alla lista dei nodi da visitare

        while (len(nodi) > 0):  # Fin quando ho nodi da di visitare
            percorso = self.mediumNode(random.choice(nodi))  # Ottengo il percorso più lungo nel grafo
            # Va aggiunto il codice nel caso in cui ci siano più percorsi più lunghi
            if percorso[1] != 0:  # Se esiste un percorso,
                nodoMassimo = self.backToFather(percorso[3])  # calcolo il valore del(dei) nodo massimo(massimi)
                if (nodoMassimo != 0 and nodoMassimo[1] > nodeMax[
                    1]):  # Se il nuovo nodo è medio per un numero superiore di volte all'attuale massimo,
                    nodeMax[0] = nodoMassimo[0]  # imposto i suoi valori come nuovo massimo
                    nodeMax[1] = nodoMassimo[1]
                # Aggiungere anche qui caso in cui siano medi uguali
            nodi = list(set(nodi) - set(
                percorso[2]))  # Rimuovo dalla lista dei nodi quelli appartenenti al sottografo considerato

        return nodeMax  # Restituisco il nodo massimo e le volte che risulta massimo nel grafo

    def backToFather(self, percorso):
        """
        Questa funzione, dato un grafo ed il percorso più lungo all'interno di un suo sottografo, restituisce una lista contenente l'Id
        del nodo (o dei nodi) ed il numero di volte che risultano medi.

        :param percorso: lista dei nodi appartenenti al percorso
        :return: lista contenente le informazioni sul nodo massimo
        """
        nodeList = [0, 0]  # Informazioni riguardo al nodo massimo

        percorso = []  # La lista dei nodi appartenenti al percorso più lungo
        while (rootID.father != None and rootID != int):  # Fin quando il nodo che sto considerando ha un padre,
            percorso.append(rootID.info)  # aggiungo il padre alla lista dei nodi appartenenti al percorso,
            rootID = rootID.father  # imposto il padre come nuovo nodo
        percorso.append(rootID)

        if len(percorso) < 3:  # Se ho meno di tre elementi nel percorso, nessun nodo risulta medio
            return 0

        if (len(
                percorso) % 2) == 0:  # Se il numero di elementi è pari, devo controllare quale dei due elementi ha il maggior numero di figli
            # Ottengo i due elementi medi nella lista
            primoElemento = percorso[int(len(percorso) / 2)]
            secondoElemento = percorso[int((len(percorso) / 2) + 1)]

            # Aggiungere rimozione dell'arco tra i due nodi

            # Da modificare first = len(percorso[:percorso.index(primoElemento)])  # Numero di nodi figli del primo elemento
            # Da modificare second = len(percorso[percorso.index(secondoElemento):])  # Numero di nodi figli del secondo elemento

            # Confronto il numero di elementi appartenenti ai sottoalberi ottenuti dai due elementi
            if first < second:
                nodeList = [secondoElemento, second]
            elif second > first:
                nodeList = [primoElemento, first]
            else:
                nodeList = [[primoElemento, secondoElemento], first]
        else:
            # Se il numero di elementi nel percorso è dispari, prendo quello che sta a metà
            nodeList = [percorso[int(len(percorso) / 2)], int(len(percorso) / 2)]

        return nodeList

    def mediumNode(self, rootId):
        """
        Questa funzione, dato un grafo e l'id di un nodo, esegue una visita generica. Per ogni foglia, chiama la funzione
        leafDistance, confrontando i valori ottenuti con quelli della lista massima.

        :param Id della radice da cui far partire la visita
        :return: lista contenente le informazioni sul nodo massimo e sul percorso
        """

        max = [0, 0, 0, 0]  # Inizializzo a 0 le informazioni riguardo al nodo massimo

        # max[0] = lunghezza del percorso
        # max[1] = foglia più profonda
        # max[2] = lista dei nodi visitati
        # max[3] = nodi appartenenti al percorso più lungo

        # Utilizzando l'algoritmo per la visita generica visto a lezione, scansiono l'albero
        if rootId not in self.nodes:
            return None

        treeNode = TreeNode(rootId)
        vertexSet = {treeNode}
        markedNodes = [rootId]  # Nodi visitati

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
                    max[3] = lunghezzaPercorso[2]

            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.append(nodeIndex)

        max[2] = markedNodes
        return max

    def leafDistance(self, rootId):
        """
        Questa funzione, dato un grafo e l'id di una foglia, restituisce il percoso più lungo e la sua lunghezza.

        :param rootId: the root node ID (integer).
        :return: the generic exploration tree.
        """

        lunghezzaPercorso = [0, 0, 0]
        # lunghezzaPercorso[0] = distanza del nodo dalla radice
        # lunghezzaPercorso[1] = nodo

        # Eseguo una visita generica utilizzando l'algoritmo visto a lezione
        if rootId not in self.nodes:
            return None

        treeNode = TreeNode(rootId)
        vertexSet = {treeNode}
        markedNodes = [rootId]

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
                    markedNodes.append(nodeIndex)
        lunghezzaPercorso[2] = markedNodes

        return lunghezzaPercorso  # Restituisco la lista con i valori