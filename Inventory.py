def dispInventory(inventory):
    print('Inventory (qty, type):')
    total=0
    for a,s in inventory.items():
        print(' - '+str(s)+' '+str(a))
        total +=s
    print('Total number of items: '+str(total))
    if total >=100:
        print('Your character is overencumbered! Capacity: '+str(total)+'/100')

def addLoot(loot,inventory):
    for d in range(len(loot)):
      inventory.setdefault(loot[d],0)
      inventory[loot[d]]+=1
    return inventory


player1={'apples':10,'sword':2,'bow':1,'arrows':92,'dickbutt':1}
dispInventory(player1)

dragon=['ruby','sword','gold','apples','dickbutt','arrows','arrows']

player1=addLoot(dragon,player1)
dispInventory(player1)
