def bfs(self, rootId, distanzaRadice):
    """
    Execute a Breadth-First Search (BFS) in the graph starting from the
    specified node.
    :param rootId: the root node ID (integer).
    :return: the BFS list of nodes.
    """
    # if the root does not exists, return None
    if rootId not in self.nodes:
        return None

    # BFS nodes initialization
    bfs_nodes = []

    # queue initialization
    q = Queue()
    q.enqueue(rootId)

    explored = {rootId}  # nodes already explored

    while not q.isEmpty():  # while there are nodes to explore ...
        node = q.dequeue()  # get the node from the queue
        explored.add(node)  # mark the node as explored
        # add all adjacent unexplored nodes to the queue

        if node.distanza > distanzaRadice:
            return

        for adj_node in self.getAdj(node):
            if adj_node not in explored:
                q.enqueue(adj_node)
        bfs_nodes.append(node)