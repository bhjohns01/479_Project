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
        return self.position == other.position
    def __ne__(self, other):
        return self.position != other.position

class Robot():
    
    path = []
    orders = []
    def __init__(self, path=None, orders=None, delivery=None):
        self.orders = orders
        self.path = path
        self.delivery = delivery

    def printPath(self):
        print(self.path)

def A_star(grid, start, end, robots):
    #create start and end nodes
    startNode = Node(None, start)
    endNode = Node(None, end)
    startNode.g = 0
    startNode.h = (startNode.position[0] - endNode.position[0])**2 + (startNode.position[1] - endNode.position[1])**2 #pythagorean theorem
    startNode.f = startNode.g + startNode.h

    closedNodes = []


    #run A* for each robot
    for robot in robots:
        openNode = startNode

        while openNode != endNode:
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
        path = []
        current = openNode
        while current is not None:
            path.append(current.position)
            current = current.parent
            robot.path = path[::-1]
        return

def main():

    NUMBER_OF_ROBOTS = 10
    GOAL = (9,9)
    START = (0, 0)

    robots = [Robot() for _ in range(NUMBER_OF_ROBOTS)]

    #create board
    rows, cols = (10,10)
    #generate a board with no obstacles
    # 0 = open, 1 = obstacle
    grid = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    A_star(grid, START, GOAL, robots)
    for robot in robots:
        robot.printPath()

if __name__ == '__main__':
    main()

         
         
    