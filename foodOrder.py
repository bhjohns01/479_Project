class foodOrder:

    def __init__(self, deliveryLoc, items = None):
        self.deliveryLoc = deliveryLoc
        self.items = {}
        if items is not None:
            for item_name in items:
                self.addItems(item_name)

    #Add the user inputed items to the foodOrder object
    def addItems(self, item_name):
        # define menu
        # SIZE: small = 1 // medium = 2 // large = 4
        menu = {
            "16oz Water": {"isFrozen": False, "isFragile": False, "size": 1},
            "Sprite": {"isFrozen": False, "isFragile": False, "size": 1},
            "Diet Coke": {"isFrozen": False, "isFragile": False, "size": 1},
            "Black Coffee": {"isFrozen": False, "isFragile": False, "size": 1},
            "Latte": {"isFrozen": False, "isFragile": False, "size": 1},
            "1 Gallon Water": {"isFrozen": False, "isFragile": False, "size": 4},
            "1 Gallon Milk": {"isFrozen": False, "isFragile": False, "size": 4},
            "Popsicle": {"isFrozen": True, "isFragile": True, "size": 1},
            "Pint of Ice Cream": {"isFrozen": True, "isFragile": False, "size": 2},
            "Cookie Dough": {"isFrozen": True, "isFragile": False, "size": 2},
            "Frozen Pizza": {"isFrozen": True, "isFragile": False, "size": 4},
            "Eggs": {"isFrozen": False, "isFragile": True, "size": 2},
            "Bread": {"isFrozen": False, "isFragile": True, "size": 2},
            "Frozen Bagel Bites": {"isFrozen": True, "isFragile": False, "size": 2},
            "Chicken": {"isFrozen": True, "isFragile": False, "size": 2},
            "Salad": {"isFrozen": False, "isFragile": False, "size": 2},
            "Doritos": {"isFrozen": False, "isFragile": False, "size": 1},
            "Spicy Doritos": {"isFrozen": False, "isFragile": False, "size": 1},
            "Lays": {"isFrozen": False, "isFragile": False, "size": 1},
            "Sun Chips": {"isFrozen": False, "isFragile": False, "size": 1}
        }

        #append item if on the menu
        if item_name in menu:
            item = menu[item_name]
            
            #increment quantity if already in items
            if item_name in self.items:
                self.items[item_name]["quantity"] += 1
            #else add new entry
            else:
                self.items[item_name] = {"quantity": 1, "isFrozen": item["isFrozen"], 
                                         "isFragile": item["isFragile"], "size": item["size"]}
        else:
            print(f"Sorry, we don't have {item_name} on the menu")

