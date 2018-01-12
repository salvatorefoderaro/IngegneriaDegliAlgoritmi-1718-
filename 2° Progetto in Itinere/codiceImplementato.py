def controlloFunzione(self):
    """
    Questa funzione, dato un grafo, restituisce una lista contenente la lista dei nodi massimi ed il numero di volte
    che risultano medi all'interno del grafo.

    :return: restituisco il nodo che risulta massimo nel grafo
    """

    nodi = []  # Lista dei nodi appartenenti al grafo, con almeno un elemento adiacente
    nodeMax = [[], 0]  # Informazioni sul nodo che risulta medio il maggior numero di volte
    nodiMedi = []  # Lista dei nodi che sono risultati medi
    percorsi = []  # Lista dei percorsi più lunghi nei vari sotto-grafi

    for nodo in (self.getNodes()):  # Considero ogni nodo
        if (self.getAdjModified(nodo.id) != 0):  # Se il nodo ha almeno un nodo adiacente,
            nodi.append(nodo.id)  # lo aggiungo alla lista dei nodi da visitare

    while (len(nodi) > 0):  # Fin quando ho nodi da di visitare
        percorso = self.mediumNode(random.choice(nodi))  # Ottengo il percorso più lungo nel grafo
        for fogliaProfonda in percorso[
            1]:  # Nel caso in cui all'interno di un sotto-grafo siano presenti più foglie con la stessa lunghezza del percorso
            if (fogliaProfonda != 0):  # Se esiste un percorso,
                nodoMassimo = self.backToFather(fogliaProfonda)  # calcolo il valore del(dei) nodo massimo(massimi)
                if (
                    nodoMassimo != 0):  # Verifico se la funzione ha restituito effettivamente una lista contenente i nodi medi
                    percorsi = percorsi + [nodoMassimo]  # Aggiungo il percorso alla lista
                    nodiMedi = nodiMedi + nodoMassimo[0]  # Aggiungo i nodi medi alla lista

        nodi = list(
            set(nodi) - set(percorso[2]))  # Rimuovo dalla lista dei nodi quelli appartenenti al sottografo considerato

    # Se presenti duplicati, li rimuovo dalla lista dei nodi medi
    nodiMedi = list(set(nodiMedi))

    for k in nodiMedi:  # Considero ogni nodo risultato medio
        contatoreNodo = 0  # Pongo a 0 il suo contatore
        for i in percorsi:  # Per ogni percorso
            if k in i[0]:  # Se il nodo considerato è presente nel percorso,
                contatoreNodo = contatoreNodo + i[
                    1]  # aggiungo al contatore del nodo il numero di volte che il nodo è risultato medio
                i[0].remove(
                    k)  # Rimuovo il nodo dal percorso, in questo modo il prossimo ciclo dovrà "cercare" in un numero minore di nodi

        if (contatoreNodo > nodeMax[
            1]):  # Confronto il contatore del numero di volte che il nodo risulta medio con il valore dell'attuale nodo massimo
            nodeMax[0] = [k]  # Se maggiore, pongo il nuovo nodo come massimo,
            nodeMax[1] = contatoreNodo  # ed il suo contatore come indice di paragone per i nodi successivi

        if (contatoreNodo == nodeMax[1]):  # Se uguale,
            nodeMax[0].append(k)  # aggiungo il nodo alla lista

    nodeMax[0] = list(set(nodeMax[0]))  # Rimuovo, se presenti, i nodi considerati più volte
    return nodeMax  # Restituisco il nodo massimo e le volte che risulta massimo nel grafo

def backToFather(self, rootID):
    """
    Questa funzione, dato un grafo ed il percorso più lungo all'interno di un suo sottografo, restituisce una lista contenente l'Id
    del nodo (o dei nodi) ed il numero di volte che risultano medi.

    :param percorso: lista dei nodi appartenenti al percorso
    :return: lista contenente le informazioni sul nodo massimo
    """
    nodeList = [[], 0]  # Informazioni riguardo al nodo massimo

    percorso = []  # La lista dei nodi appartenenti al percorso più lungo
    while (rootID.father != None and rootID != int):  # Fin quando il nodo che sto considerando ha un padre,
        percorso.append(rootID.info)  # aggiungo il padre alla lista dei nodi appartenenti al percorso,
        rootID = rootID.father  # imposto il padre come nuovo nodo
    percorso.append(rootID.info)

    if len(percorso) < 3:  # Se ho meno di tre elementi nel percorso, nessun nodo risulta medio
        return 0

    if (len(
            percorso) % 2) == 0:  # Se il numero di elementi è pari, devo controllare quale dei due elementi ha il maggior numero di figli
        # Ottengo i due elementi medi nella lista
        primoElemento = percorso[int(len(percorso) / 2)]
        secondoElemento = percorso[int((len(percorso) / 2) + 1)]

        first = self.calculateSubNode(primoElemento)  # Numero di nodi figli del primo elemento
        second = self.calculateSubNode(secondoElemento)  # Numero di nodi figli del secondo elemento

        # Confronto il numero di elementi appartenenti ai sottoalberi ottenuti dai due elementi
        if first < second:
            nodeList = [[secondoElemento], second]
        elif second > first:
            nodeList = [[primoElemento], first]
        else:
            nodeList = [[primoElemento, secondoElemento], first]
    else:
        # Se il numero di elementi nel percorso è dispari, prendo quello che sta a metà
        nodeList = [[percorso[int(len(percorso) / 2)]], int(len(percorso) / 2)]

    return nodeList


def calculateSubNode(self, rootId):
    """
    Questa funzione, dato un grafo e l'Id di un suo nodo, mi restituisce il numero di nodi raggiungibili a partire dal nodo
    :param rootId: Id del nodo
    :return: Numero di elementi che posso raggiungere a partire dal nodo
    """
    # Utilizzo l'algoritmo per la visita generica visto a lezione

    if rootId not in self.nodes:
        return None
    counter = 0  # Contatore dei igli del nodo
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


def mediumNode(self, rootId):
    """
    Questa funzione, dato un grafo e l'id di un nodo, esegue una visita generica. Per ogni foglia, chiama la funzione
    leafDistance, confrontando i valori ottenuti con quelli della lista massima.

    :param Id della radice da cui far partire la visita
    :return: lista contenente le informazioni sul nodo massimo e sul percorso
    """

    max = [0, [], 0, []]  # Inizializzo a 0

    # max[0] = lunghezza del percorso
    # max[1] = Lista dei nodi più profondi
    # max[2] = lista dei nodi visitati
    # max[3] = Id dei nodi più profondi

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
                max[3] = max[3] + lunghezzaPercorso[2]
            if (lunghezzaPercorso[0] == max[0]):
                for i in lunghezzaPercorso[1]:  # Per ogni nodo il cui percorso risulta massimo,
                    if (i.info not in max[3]):  # controllo che non sia già presente nella lista dei nodi massimi
                        max[1] = max[1] + lunghezzaPercorso[
                            1]  # In caso non sia presente, lo aggiungo alla lista dei nodi "più profondi"

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

    lunghezzaPercorso = [0, [], []]  # Inizializzo a 0

    # lunghezzaPercorso[0] = distanza del nodo dalla radice
    # lunghezzaPercorso[1] = nodo
    # lunghezzaPercorso[2] = Id del nodo

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
                lunghezzaPercorso[1] = []
                lunghezzaPercorso[1].append(treeNode)
                lunghezzaPercorso[2].append(treeNode.info)
            elif lunghezzaPercorso[
                0] == treeNode.distanza:  # Altrimenti aggiungo agli altri valori già presenti in lista
                lunghezzaPercorso[1].append(treeNode)
                lunghezzaPercorso[2].append(treeNode.info)

        for nodeIndex in adjacentNodes:
            if nodeIndex not in markedNodes:
                newTreeNode = TreeNode(nodeIndex)
                newTreeNode.father = treeNode
                newTreeNode.distanza = treeNode.distanza + 1  # Incremento la distanza del nodo
                treeNode.sons.append(newTreeNode)
                vertexSet.add(newTreeNode)
                markedNodes.append(nodeIndex)

    return lunghezzaPercorso  # Restituisco la lista con i valori