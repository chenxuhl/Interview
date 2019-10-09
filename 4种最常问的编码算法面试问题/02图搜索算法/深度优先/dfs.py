"""pseudo-code"""

"""
¶ÑÕ»+µÝ¹é
(Depth-First Search)
DFS(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
for every edge (s, v):
    if v unexplored:
        DFS(G, v)
"""


def dfs(graph, start):
    """The DFS function simply calls itself recursively for every unvisited child of its argument. We can emulate that
     behaviour precisely using a stack of iterators. Instead of recursively calling with a node, we'll push an iterator
      to the node's children onto the iterator stack. When the iterator at the top of the stack terminates, we'll pop
       it off the stack."""
    explored, stack = set(), [start]
    while stack:
        v = (
            stack.pop()
        )  # one difference from BFS is to pop last element here instead of first one

        if v in explored:
            continue

        explored.add(v)

        for w in graph[v]:
            if w not in explored:
                stack.append(w)
                print(stack)
        print('********************************************')
        print(explored)
        print('********************************************')
    return explored


def dfs_modify(graph, start):
    explored, stack = [], [start]
    while stack:
        v = (
            stack.pop()
        )  # one difference from BFS is to pop last element here instead of first one

        if v in explored:
            continue

        explored.append(v)

        for w in graph[v]:
            if w not in explored:
                stack.append(w)
        #         print(stack)
        # print('********************************************')
        # print(explored)
        # print('********************************************')
    return explored

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
G2 = {
    "1": ["2", "5"],
    "2": ["1", "3", "4"],
    "3": ["2", "4", "5"],
    "4": ["2", "3", "5"],
    "5": ["1", "3", "4"],
}

# print(dfs(G, "A"))
print(dfs_modify(G2, "1"))
