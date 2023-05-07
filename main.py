from foodOrder import foodOrder
import numpy as np
import random

# pass in a single order and return bagged items
def sorting(order):
    large, medium, small, fragile = [], [], [], []
    bag1, bag2 = [], []
    bag1_cap, bag2_cap = 0, 0

    #separate objects into arrays by size
    for item in order:
        if item["size"] == 4:
            large.append(item)
        if item["size"] == 2:
            medium.append(item)
        if item["size"] == 1:
            small.append(item)

    # put in freezer bag
    for i in order:
        if i["isFrozen"] == True:
            print(i + " was placed in a freezer bag.\n")

    # bag large items first
    if large is not None:
        bag1.append(large[0])
        bag1_cap = 4
    if len(large) == 2:
        bag2.append(large[1])
        bag2_cap = 4

    # bag medium items
    if medium is not None:
        for m in range(len(medium)):
            if m["isFragile"] == True:
                fragile.append(m)
            else:
                if bag1_cap <=2:
                    bag1.append(medium[m])
                    bag1_cap += 2
                elif bag2_cap <= 2:
                    bag2.append(medium[m])
                    bag2_cap += 2

    # bag small items
    if small is not None:
        for s in range(len(small)):
            if s["isFragile"] == True:
                fragile.append(s)
            else:
                if bag1_cap <=3:
                    bag1.append(small[s])
                    bag1_cap += 1
                elif bag2_cap <= 3:
                    bag2.append(small[s])
                    bag2_cap += 1

    # bag fragile items
    if fragile is not None:
        for f in range(len(fragile)):
            if bag1_cap < 4:
                if f["size"] == 2 and bag1_cap <= 2:
                    bag1.append(fragile[f])
                    bag1_cap += 2
                if f["size"] == 1 and bag1_cap <= 3:
                    bag1.append(fragile[f])
                    bag1_cap += 1
            if bag2_cap < 4:
                if f["size"] == 2 and bag2_cap <= 2:
                    bag2.append(fragile[f])
                    bag2_cap += 2
                if f["size"] == 1 and bag1_cap <= 3:
                    bag2.append(fragile[f])
                    bag2_cap += 1

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

    #create a list of order objects 
    orders = []
    for o in range(len(readOrders)):
        orders.append(foodOrder(readLocations[o], readOrders[o]))

    bag1, bag2 = sorting(orders[0])
    ##### past here, just ideas of implementation

    #create grid
    size = 5
    grid = np.zeros((size, size))

    #flag random indices for random obstacles
    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0: #skip (0, 0), aka Food Warehouse
                continue
            if random.random() < 0.1: #probability of obstacle 10%
                grid[i][j] = 1


    
if __name__ == '__main__':
    main()