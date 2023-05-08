import math 


class Node():
    """A node class for A* Pathfinding"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 #distance from start 
        self.h = 0 #estimated distance from end using hypotenuse
        self.f = self.g + self.h #g + h
    
    def __eq__(self, other):
        return (self.position[0] == other.position[0]) and (self.position[1] == other.position[1])
    def __ne__(self, other):
        return (self.position[0] != other.position[0]) or (self.position[1] != other.position[1])

class Robot():

    def __init__(self):
        self.path = []
        self.orders = []
        self.delivery = []
        self.flag = 0

    def printPath(self):
        print(self.path)

def A_star(grid, start, robots):
    #create start and end nodes
    startNode = Node(None, start)
    #run A* for each robot
    closedNodes = []

    for robot in robots:
        iteration = 0
        for deliveryNum in range(len(robot.delivery)):
            if(deliveryNum == 0):
                openNode = startNode
            closedNodes.clear()
            #have to implement multiple orders
            endNode = Node(None, robot.delivery[deliveryNum])

            openNode.g = 0
            openNode.h = (openNode.position[0] - endNode.position[0])**2 + (openNode.position[1] - endNode.position[1])**2 #pythagorean theorem
            openNode.f = openNode.g + openNode.h

            while openNode != endNode and iteration < 200:
                iteration = iteration + 1

                 # Get the current node
                currentNode = openNode

                #move this outside the while loop
                for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares
                    #we check the heuristic of each of these sqaures
                    #if there's no obstacle and it's unexplored, then we add it to nextNodes array
                    tempNode = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])
                    #check bound
                    if tempNode[0] >= len(grid[0]) or tempNode[1] >= len(grid) or tempNode[0] < 0 or tempNode[1] < 0:
                        #out of bounds
                        continue
                    #check if obstacle
                    if grid[tempNode[0]][tempNode[1]] == 1:
                        #obstacle
                        continue
                    #check if already explored
                    childNode = Node(None, tempNode)
                    for node in closedNodes:
                        if(node == childNode):
                            continue
                    #add this node to already explored nodes    
                    closedNodes.append(childNode)

                    childNode.g = currentNode.g + 1
                    childNode.h = (childNode.position[0] - endNode.position[0])**2 + (childNode.position[1] - endNode.position[1])**2 #pythagorean theorem
                    childNode.f = childNode.g + childNode.h

                    if childNode.f <= openNode.f:
                        #finding the best heuristic out of the adjacent nodes
                        childNode.parent = currentNode
                        openNode = childNode
            if(iteration >= 200):
                #no solution
                path = [-1]
                robot.setFlag()
                break

            path = []
            current = openNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            robot.path = path[::-1]
    return

         
    