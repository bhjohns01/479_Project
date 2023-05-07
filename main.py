from foodOrder import foodOrder
import numpy as np
import random

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