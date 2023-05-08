import random


class Node():
    """A node class for A* Pathfinding"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 #distance from start 
        self.h = 0 #estimated distance from end using hypotenuse
        self.f = self.g + self.h #g + h
    
        def __eq__(self, other):
            return self.position == other.position


class Robot():
    
    def __init__(self):
        self.orders = []
        self.path = []

    def printPath(self):
        for node in self.path:
            print("(" + node[0] + ", " + node[1] + ")")


    #adding this function so I can test the animation, really should be called addPath or something -Love Brian ;)
    def tracePath(self, locations):
        self.path.append(locations)



def A_star(grid, start, end, robots):
    #create start and end nodes
    startNode = Node(None, start)
    endNode = Node(None, end)

    openNodes = []
    closedNodes = []
    children = []

    #run A* for each robot
    for robot in robots:
        openNodes.append(startNode) 

        while len(openNodes) > 0:
            currentNode = openNodes.pop
            closedNodes.append(currentNode)
            if currentNode == endNode:
                #done
                path = []
                current = currentNode
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                    robot.path = path[::-1]
                    return
            else:
                for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
                    #we check the heuristic of each of these sqaures
                    #if there's no obstacle and it's unexplored, then we add it to nextNodes array
                    tempNode = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])
                    #check bound
                    if tempNode.position[0] > len(grid[0]) or tempNode.position[1] > len(grid) or tempNode.position[0] < 0 or tempNode.position[1] < 0:
                        #out of bounds
                        continue
                    #check if obstacle
                    if grid[tempNode.position[0]][tempNode.position[1]] == 1:
                        #obstacle
                        continue
                    #check if already explored
                    for node in closedNodes:
                        if(node == closedNodes):
                            continue

                    childNode = Node(currentNode, tempNode)
                    childNode.g = currentNode.g + 1
                    childNode.h = (childNode.position[0] - end.position[0])**2 + (childNode.position[1] - end.position[1])**2 #pythagorean theorem
                    childNode.f = childNode.g + childNode.h
                    children.append(childNode)

                    #check to see if node already is in open list
                    for node in openNodes:
                        if childNode == node and childNode.g > node.g:
                            continue

                    if childNode.f < currentNode.f:
                        #favorable heuristic
                        openNodes.append(childNode)
                    else:
                        #unfavorable heuristic
                        closedNodes.append(childNode)