spam = ['apples', 'bannanas', 'tofu', 'cats']
bands = ['the Replacements', 'the Pixies', 'the Stooges', 'the Beatles', 'Nirvana']

def listify(my_list):
	temp = ''
	for i in range(len(my_list)-1):
		temp += ( my_list[i] + ', ')
	temp += ('and ' + my_list[len(my_list)-1])
	return (temp)
	
new_string = listify(bands)
print new_string

