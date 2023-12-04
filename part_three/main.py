import heapq

class Node:
    def __init__(self, name, heuristic_cost):
        self.name = name
        self.heuristic_cost = heuristic_cost
        self.adjacent_nodes = {}
        self.parent = None
        self.g_cost = float('inf')

    def add_neighbor(self, neighbor, cost):
        self.adjacent_nodes[neighbor] = cost

def find_shortest_path(start, goal):
    open_set = []
    closed_set = set()

    start.g_cost = 0
    start.f_cost = start.g_cost + start.heuristic_cost
    heapq.heappush(open_set, (start.f_cost, start))

    while open_set:
        current_node = heapq.heappop(open_set)[1]

        if current_node == goal:
            path = []
            while current_node:
                path.insert(0, current_node.name)
                current_node = current_node.parent
            return path

        closed_set.add(current_node)

        for neighbor, cost in current_node.adjacent_nodes.items():
            if neighbor not in closed_set:
                tentative_g_cost = current_node.g_cost + cost

                if tentative_g_cost < neighbor.g_cost:
                    neighbor.parent = current_node
                    neighbor.g_cost = tentative_g_cost
                    neighbor.f_cost = neighbor.g_cost + neighbor.heuristic_cost

                    if neighbor not in [node[1] for node in open_set]:
                        heapq.heappush(open_set, (neighbor.f_cost, neighbor))

    return None

A = Node('A', 5)
B = Node('B', 3)
C = Node('C', 2)
D = Node('D', 7)
E = Node('E', 8)

A.add_neighbor(B, 2)
A.add_neighbor(C, 1)
B.add_neighbor(D, 4)
C.add_neighbor(E, 3)
D.add_neighbor(E, 1)

path = find_shortest_path(A, E)

if path:
    print(f"Đường đi ngắn nhất từ A đến E: {' -> '.join(path)}")
else:
    print("Không tồn tại đường đi từ A đến E.")
