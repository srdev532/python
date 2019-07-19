stuff = {'rope': 1,'rope': 2,'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display(inventory):
    print(inventory)
    item_total = 0
    #count = {}
    for k,v in inventory.items():
        print ('key:' + k + 'value:' + str(v))
        for k in inventory.keys()
        item_total += v
        print ('the total values:' ''+ k +' '+str(item_total))

    
'''
    item_total = item_total + 
        
        #item_total = item_total + v.get(item,0)
        #return item_total
    #print ('Total Count is ' + str(item_total))
    '''


inventory = stuff
display(inventory)
