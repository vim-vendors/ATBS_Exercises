grid = [['.','.','.','.','.','.'],
				['.','0','0','.','.','.'],
				['0','0','0','0','.','.'],
				['0','0','0','0','0','.'],
				['.','0','0','0','0','0'],
				['0','0','0','0','0','.'],
				['0','0','0','0','.','.'],
				['.','0','0','.','.','.'],
				['.','.','.','.','.','.']]
		
#Print by col		
for j in range(len(grid[0])):
	for i in range(len(grid)):
		print grid[i][j],
	print ' '

print ' '

#Print by row
for i in range(len(grid)):	
	for j in range(len(grid[0])):
		print grid[i][j],
	print ' '			

