"""
Implementation of the uniform cost search, better version of the BFS.
Instead of expanding the shallowest node, uniform-cost search expands the node n with the lowest path cost
"""

from queue import PriorityQueue

# Graph function implementation
class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node + to_node)]



def uniform_cost_search(graph, start_node, goal):
    """

    :param graph: The simple directed graph with the weight as string
    :param start_node: start node is the starting point
    :param goal: The end point to reach, that is goal state
    :return: nothing to return, prints the total cost
    """
    path = set()
    explored = set()

    if start_node == goal:
        return path, explored

    path.add(start_node)
    path_cost = 0
    frontier = PriorityQueue()
    frontier.put((path_cost, start_node))

    while frontier:
        cost, node = frontier.get()

        if node not in explored:
            explored.add(node)
        if node == goal:
            print("all good")
            print("At the cost of " + str(cost))
            return

        for neighbor in graph.neighbors(node):
            if neighbor not in explored:
                total_cost = cost + graph.get_cost(node, neighbor)
                frontier.put((total_cost, neighbor))




# Driver Function
edges = {
    'S': ['R', 'F'],
    'R': ['P'],
    'F': ['B'],
    'P': ['B']
}
weigth = {
    'SR': 80,
    'SF': 99,
    'RP': 97,
    'PB': 101,
    'FB': 211
}

simple_graph = Graph()
simple_graph.edges = edges
simple_graph.weights = weigth

uniform_cost_search(simple_graph, 'S', 'B')
