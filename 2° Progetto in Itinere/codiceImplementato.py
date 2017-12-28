def mediumNode(self, rootId):
    """
    :param rootId:
    :return:
    """
    if rootId not in self.nodes:
        return None

    treeNode = TreeNode(rootId)
    # tree = Tree(treeNode)
    vertexSet = {treeNode}  # nodes to explore
    markedNodes = {rootId}  # nodes already explored
    j = 0
    nodeMax = [0]
    max = 0

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
                controllo = self.calculateSubNode(newTreeNode.info, newTreeNode.distanza)
                if controllo == max:
                    nodeMax.append(newTreeNode.info)
                elif controllo > max:  ### Codici implementati da me e da controllare
                    nodeMax = [0]
                    max = controllo  ### Codici implementati da me e da controllare
                    nodeMax[0] = newTreeNode.info  ### Codici implementati da me e da controllare
    if nodeMax[0] == 0:
        return 0  # Se nessun nodo è medio almeno una volta, restituisco 0
    else:
        return nodeMax  # Restituisco l'ID del nodo


def calculateSubNode(self, rootId, distanzaNodo):
    """
    :param rootId:
    :param distanzaNodo:
    :return:
    """
    if rootId not in self.nodes:
        return 0

    i = 0

    treeNode = TreeNode(rootId)
    # tree = Tree(treeNode)
    vertexSet = {treeNode}  # nodes to explore
    markedNodes = {rootId}  # nodes already explored

    while len(vertexSet) > 0:  # while there are nodes to explore ...

        treeNode = vertexSet.pop()  # get an unexplored node
        adjacentNodes = self.getAdj(treeNode.info)

        if treeNode.distanza == distanzaNodo:
            i = i + treeNode.distanza

        elif not adjacentNodes:
            i = i + treeNode.distanza

        else:
            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:  # if not explored ...
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    newTreeNode.distanza = treeNode.distanza + 1
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)  # mark as explored
    return i