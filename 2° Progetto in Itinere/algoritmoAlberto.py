
def genericSearch(self, rootId):
    """
    Execute a generic search in the graph starting from the specified node.
    :param rootId: the root node ID (integer).
    :return: the generic exploration tree.
    """

    info = []
    # info[0] = Profondità del nodo
    # info[1] = ID del nodo più profondo
    # info[2] = Padre al bivio del nodo più profondo

    if rootId not in self.nodes:
        return None

    treeNode = TreeNode(rootId)
    vertexSet = {treeNode} # nodes to explore
    markedNodes = {rootId} # nodes already explored

    while len(vertexSet) > 0: # while there are nodes to explore ...
        treeNode = vertexSet.pop() # get an unexplored node
        adjacentNodes = self.getAdj(treeNode.info)

        if len(adjacentNodes) > 1:
            # Funzione

            infoNew = profonditaBivio(treeNode) # Passo alla funzione il nodo che genera il bivio
            info[0] = info[0] + infoNew[0]
            info[1] = info[1] + infoNew[1]
            info[2] = info[2] + infoNew[2]

        else:
            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes: # if not explored ...
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex) # mark as explored
                    info[0] = info[0] + 1
    return info

    # La funzione restituisce la lunghezza del percorso
    # Mi serve anche che mi restituisca la lista dei bivi da considerare


def genericSearch(self, rootId):
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