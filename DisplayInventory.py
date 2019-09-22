stuff = {'rope': 1, 'torch':6, 'gold coin':42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		print str(v) + ' ' + k   
		item_total+= int(v)
	print("Total number of items: " + str(item_total))
	
displayInventory(stuff)

print 

def addToInventory(inventory, addedItems):
	for i in addedItems:
		if i in inventory.keys():
			inventory[i] += 1
		else:
			inventory.setdefault(i, 1)
	
inv = {'gold coin': 42, 'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)
