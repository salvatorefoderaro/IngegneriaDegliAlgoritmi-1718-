""" CODICE MIO """


def mediumNode(self, rootId):
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
                controllo = self.calculateSubNode(newTreeNode.info, newTreeNode.distanza)
                if controllo > nodeMax[1]:  ### Codici implementati da me e da controllare
                    nodeMax[1] = controllo  ### Codici implementati da me e da controllare
                    nodeMax[0] = newTreeNode  ### Codici implementati da me e da controllare


def calculateSubNode(self, rootId, distanzaNodo):
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