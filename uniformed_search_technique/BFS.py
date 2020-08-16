"""
Python implementation for the Breadth First search in the tree level using the FIFO queue
It is just a abstract version of the BFS, solution for the state could be implement according to the questions
"""


# Basic Node structure
class Node:
    def __init__(self, state):
        self.state = state
        self.actions = []


# Implementaion of BFS

class BFS:

    def __init__(self, root):
        self.root = root
        self.string = ""

    def transversalOfBFS(self, goal):
        # Base case
        if self.root is None:
            # Failure
            return
        # Initial Check for the root
        if goal.state == self.root.state:
            return

        # Initializing a queue (frontier)
        queue = []
        explored = []

        # Enqueue Root and intialize height
        queue.append(self.root)

        while len(queue) > 0:

            # Check for the node state and compare with goal state
            # here it is just print the node state
            self.string += str(queue[0].state) + " --> "
            node = queue.pop(0)

            # Enqueue children

            for i in range(len(node.actions)):
                # Only for the actions that is not None
                if node.actions[i] is not None:
                    # comparing the goal state with the child node state
                    if goal.state == node.actions[i].state:
                        print(self.string)
                        print("using the state " + str(node.state))
                        return
                    queue.append(node.actions[i])

        print(self.string)


# Driver program to test
root = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
eleven = Node(11)
rootActions = [one, two]
root.actions = rootActions
one.actions = [three, four, five]
two.actions = [six, seven]
three.actions = [eight]
four.actions = [nine]
six.actions = [ten, eleven]
bfs = BFS(root)
goal = Node(7)
bfs.transversalOfBFS(goal)
