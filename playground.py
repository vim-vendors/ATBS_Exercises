tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(my_list):
	colWidths = [0] * len(my_list)

# print(len(colWidths))

# set length for each column based on the length of the longest string 
# in nested list

	for x in range(len(my_list)):
		for y in range(len(my_list[x])):
			if colWidths[x] < len(my_list[x][y]):
				colWidths[x] = len(my_list[x][y])

#Print list with right justified max-length
	for y in range(len(my_list[0])):
		for x in range(len(my_list)):
			print(str(my_list[x][y]).rjust(colWidths[x]), end=" ")
		print()

printTable(tableData)