    def mediumNode(self, rootId):

        """
        Questa funzione, dato un Grafo ed un nodo di partenza, mi permette di trovare il nodo che risulta medio
        per il maggior numero di coppie nel grafo.

        :param rootId: Nodo di partenza
        :return: Lista nodi medi per il maggior numero di volte
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

            """ Se sto considerando la radice e questa non ha nessun figlio, allora restituisco None """
            if not adjacentNodes and treeNode.info == rootId:
                print("La radice non ha nessun nodo adiacente!")
                return None

            """ Quando un nodo, diverso dalla radice, che non ha nodi adiacenti invoco la funzione backToRoot"""
            if not adjacentNodes:
                self.backToRoot(treeNode, treeNode.distanza)

            """ Scorro l'albero, aggiornando il valore della distanza dalla radice dei singoli nodi"""
            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:  # Se il nodo non è stato esplorato...
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)  # Segno il nodo come esplorato
                    newTreeNode.distanza = treeNode.distanza + 1  # Incremento la distanza del nodo
        return self.getMaxMedium(tree)

    def backToRoot(self, treeRoot, rootDistance):

        """
        Questa funzione, dato in input un nodo e la sua distanza dalla radice dell'albero, aggiorna il valore del
        campo 'medium' di tutti i nodi che incontra nel suo cammino verso la radice.

        :param treeRoot: Nodo di partenza
        :param rootDistance: Distanza del nodo dalla radice
        """

        """ Controllo se sto considerando un nodo diverso dalla radice dell'albero """
        # if (treeRoot.father is None):
        #    treeRoot = treeRoot.father

        while ((rootDistance - treeRoot.distanza) < rootDistance): # Controllo che il nodo considerato non sia la radice
            distanzaFoglia = rootDistance - treeRoot.distanza

            """ Se il nodo ha lo stesso numero di 'figli in avanti' e 'figli all'indietro',
                allora sarà medio per un numero di nodi pari alla sua distanza dalla radice (o dalla foglia).
                 
                Se invece il nodo ha un numero inferiore di 'figli in avanti' rispetto ai 'figli all'indietro',
                allora sarà medio per un numero di nodi pari alla sua distanza dalla foglia.
            """
            
            if (distanzaFoglia == treeRoot.distanza):
                treeRoot.medium = treeRoot.medium + treeRoot.distanza

            elif ((distanzaFoglia < treeRoot.distanza) and (treeRoot.distanza > 0)):
                treeRoot.medium = treeRoot.medium + distanzaFoglia
            
            treeRoot = treeRoot.father # Accedo al nodo successivo nell'albero


    def getMaxMedium(self, tree):

        """
        Questa funzione, dato in input un albero, per ogni nodo controlla il valore 'medium' e crea una lista dei nodi
        che hanno questo valore maggiore di tutti gli altri.

        :param tree: Albero da controllare
        :return: Lista nodi
        """

        nodeMax = [0]
        max = 0
        q = Queue()
        if tree.root is not None:
            q.enqueue(tree.root)
        while not q.isEmpty():
            current = q.dequeue()
            for s in current.sons:
                controllo = s.medium # Per ogni nodo considero il valore del campo 'medium'
                if controllo == max: # Se il nodo ha il campo 'medium' uguale al nodo attualmente massimo
                    nodeMax.append(s.info) # aggiungo il nodo che sto considerando alla lista dei nodi
                elif controllo > max: # Se invece il valore del nodo che sto considerando è superiore a quello dell'attuale massimo
                    nodeMax = [0] # Azzero la lista
                    max = controllo # Imposto il nuovo valore massimo
                    nodeMax[0] = s.info #Imposto il nuovo nodo massimo
                q.enqueue(s)
        if nodeMax[0] == 0:
            return 0  # Se nessun nodo è medio almeno una volta, restituisco 0
        else:
            return nodeMax  # Restituisco l'ID del nodo