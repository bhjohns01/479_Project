from foodOrder import foodOrder
import numpy as np
import random
import grid as g

# pass in a single order and return bagged items
def sorting(order):
    large, medium, small, fragile = [], [], [], []
    bag1, bag2 = [], []
    bag1_cap, bag2_cap = 0, 0

    #separate objects into arrays by size
    for item in order.items:
        item_attributes = order.items[item]
        if item_attributes["size"] == 4:
            large.append(item)
        if item_attributes["size"] == 2:
            medium.append(item)
        if item_attributes["size"] == 1:
            small.append(item)
        # put in freezer bag
        if item_attributes["isFrozen"] == True:
            print(item + " placed in a freezer bag. ")  
        # check if fragile
        if item_attributes["isFragile"] == True:
            fragile.append(item)
        
    # bag large items first
    if len(large) > 0:
        bag1.append(large[0])
        bag1_cap = 4
        print("Large item " + large[0] + "placed in bag 1. ")
    if len(large) == 2:
        bag2.append(large[1])
        bag2_cap = 4
        print("Large item " + large[1] + "placed in bag 2. ")

    # bag medium items
    if len(medium) > 0:
        for m in range(len(medium)):
            if medium[m] not in fragile:
                if bag1_cap <=2:
                    bag1.append(medium[m])
                    bag1_cap += 2
                    print("Medium item " + medium[m] + " placed in bag 1. ")
                elif bag2_cap <= 2:
                    bag2.append(medium[m])
                    bag2_cap += 2
                    print("Medium item " + medium[m] + " placed in bag 2. ")

    # bag small items
    if len(small) > 0:
        for s in range(len(small)):
            if small[s] not in fragile:
                if bag1_cap <=3:
                    bag1.append(small[s])
                    bag1_cap += 1
                    print("Small item " + small[s] + " placed in bag 1. ")
                elif bag2_cap <= 3:
                    bag2.append(small[s])
                    bag2_cap += 1
                    print("Small item " + small[s] + " placed in bag 2. ")

    # bag fragile items
    if len(fragile) > 0:
        for f in range(len(fragile)):
            f_temp = 0
            bagged_flag = 0
            for i in enumerate(order.items.keys()):
                if fragile[f] == i[1]:
                    index = i[1]
                    f_temp = order.items[index]
            if bag1_cap < 4:
                if f_temp["size"] == 2 and bag1_cap <= 2:
                    bag1.append(fragile[f])
                    bag1_cap += 2
                    bagged_flag = 1
                    print("Fragile medium item " + fragile[f] + " placed in bag 1 last.")
                if f_temp["size"] == 1 and bag1_cap <= 3:
                    bag1.append(fragile[f])
                    bag1_cap += 1
                    bagged_flag = 1
                    print("Fragile small item " + fragile[f] + " placed in bag 1 last.")
            if bag2_cap < 4 and bagged_flag == 0:
                if f_temp["size"] == 2 and bag2_cap <= 2:
                    bag2.append(fragile[f])
                    bag2_cap += 2
                    print("Fragile medium item " + fragile[f] + " placed in bag 2 last.")
                if f_temp["size"] == 1 and bag1_cap <= 3:
                    bag2.append(fragile[f])
                    bag2_cap += 1
                    print("Fragile small item " + fragile[f] + " placed in bag 2 last.")

    return bag1, bag2


def main():

    #user inputs
    filename = input("Enter the filename: ") # file includes order and delivery location
    numRobots = input("Enter the number of robots: ")

    #read input file to store orders and locations
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        readOrders = []
        readLocations = []
        for line in lines:
            items, locations = line.rsplit(' ', 1)
            items_list = items.split(',')
            location_list = [int(x) for x in locations.strip('[]').split(',')]
            readOrders.append(items_list)
            readLocations.append(location_list)

    # create a list of order objects 
    orders = []
    print("\n- - - - - - - - - - - - Orders Placed - - - - - - - - - - - - \n")
    for o in range(len(readOrders)):
        orders.append(foodOrder(readLocations[o], readOrders[o]))
        print("Order " + str(o + 1) + ":")
        print(readOrders[o], end='')
        print('\n')

    # bag the orders accordingly
    print("- - - - - - - - - - - Bagging the orders - - - - - - - - - -\n")
    bagged_orders = []
    for o in range(len(orders)):
        print("Order " + str(o + 1) + ":" )
        bagged_orders.append(sorting(orders[o]))
        print("\tBag 1: ", end = '')
        for x in range(len(bagged_orders[o][0])):
            print(bagged_orders[o][0][x], end = '   ')
        print("\n\tBag 2: ", end = '')
        for x in range(len(bagged_orders[o][1])):
            print(bagged_orders[o][1][x], end = '   ')
        print('\n')

    #create robot objects 
    robots = []
    for x in range(int(numRobots)):
          robots.append(g.Robot())

    order_idx = 0
    #put the orders in the robots 
    #FIXME: append order locations to the robot class
    for r in range(len(robots)):
        bags_in_r = 0
        if len(robots[r].orders) < 2 and order_idx < len(orders):
            robots[r].orders.append(bagged_orders[order_idx][0])
            bags_in_r += 1
            robots[r].delivery.append(readLocations[order_idx])
            # if there is a second bag in the order
            if len(bagged_orders[order_idx][1]) != 0:
                robots[r].orders.append(bagged_orders[order_idx][1])
                bags_in_r += 1
            order_idx += 1
            #if space in the robot for a 1-bag order
            if bags_in_r < 2 and order_idx < len(orders):
                if len(bagged_orders[order_idx][1]) == 0:
                    robots[r].orders.append(bagged_orders[order_idx][0])
                    robots[r].delivery.append(readLocations[order_idx])
                    order_idx += 1
                    bags_in_r += 1


    #create grid
    size = 10
    grid = np.zeros((size, size))

    #flag random indices for random obstacles
    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0: #skip (0, 0), aka Food Warehouse
                continue
            if random.random() < 0.1: #probability of obstacle 10%
                grid[i][j] = 1
    print(grid)

    #call A* heuristic
    start = (0, 0)
    goal = readLocations[0] # will need to for-loop around somehow
    g.A_star(grid, start, goal, robots)
    for robot in robots:
        robot.printPath()

    
if __name__ == '__main__':
    main()