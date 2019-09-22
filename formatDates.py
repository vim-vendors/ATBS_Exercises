import re

#print(str(firstRE.search('03-14-2015')))
testing = firstRE.search('03-14-2015').group()

print(testing)
testing = secondRE.search('2015-03-14').group()
print(testing)

def cleanDates(dates):
	
	months = {1: 'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7: 'July', 8: 'August', 9:'September', 10: 'October', 11: 'November', 12: 'December'}
	
	firstRE = re.compile('^\d{1,2}[-/]\d{1,2}[-/]\d{4}$')
  secondRE = re.compile('^\d{4}[-/]\d{1,2}[-/]\d{1,2}$')
  
  if firstRE.search(dates).group() && 2ndRE.search(dates).group()
