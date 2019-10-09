"""
¶ÓÁÐ+µÝ¹é
BFS.(Breadth-First Search)

pseudo-code:

BFS(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
let Q = queue data structure, initialized with s
while Q is non-empty:
    remove the first node of Q, call it v
    for each edge(v, w):  // for w in graph[v]
        if w unexplored:
            mark w as explored
            add w to Q (at the end)

"""

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def bfs(graph, start):
    """
    >>> ''.join(sorted(bfs(G, 'A')))
    'ABCDEF'
    """
    explored, queue = set(), [start]  # collections.deque([start])
    explored.add(start)
    while queue:
        v = queue.pop(0)  # queue.popleft()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                queue.append(w)
    return explored

def bfs_modify(graph, start):
    explored, queue = [], [start]  # collections.deque([start])
    explored.append(start)
    while queue:
        v = queue.pop(0)  # queue.popleft()
        for w in graph[v]:
            if w not in explored:
                explored.append(w)
                queue.append(w)
    return explored

G2 = {
    "1": ["2", "5"],
    "2": ["1", "3", "4"],
    "3": ["2", "4", "5"],
    "4": ["2", "3", "5"],
    "5": ["1", "3", "4"],
}

if __name__ == "__main__":
    # print(bfs(G, "A"))
    # res = bfs(G, "A")
    res = bfs_modify(G2, "1")
    print("result is:", res)