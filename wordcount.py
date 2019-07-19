stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(stuff):
    print("Inventory: ")
    item_total = 0

    for k,v in stuff.items():
        print(str(v) + ' ' + str(k) )
        item_total += v
    print("The total item values are" + str(item_total))


    
def addToInventory(stuff, dragonLoot):
    for item in dragonLoot:
        stuff.setdefault(item,0)
        stuff[item] += 1
    print (stuff)
    
    
displayInventory(stuff)

addToInventory(stuff, dragonLoot)

Hello world

Try to compare the difference
