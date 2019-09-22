import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
#print('Phone number found: '+ mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
#print(mo.group())
#print(mo.group(1))

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo2.group())

batRegex = re.compile(r'Bat(wo)+man')
mo3 = batRegex.search('The Adventures of Batwowoman')
print(mo3.group())

haRegex = re.compile(r'(Ha){3}')
mo4 = haRegex.search('HaHaHa')
print(mo4.group())

greedyRegex = re.compile(r'(Ha){3,5}')
mo5 = greedyRegex.search('HaHaHaHaHa')
print(mo5.group()) 

nongreedyRegex = re.compile(r'(Ha){3,5}')
mo6 = nongreedyRegex.search('HaHaHaHaHa')
print(mo6.group()) 


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo8 = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo8.group()) 
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))






























