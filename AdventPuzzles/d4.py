import os
import re

inputs = open(os.getcwd() + '/inputs/test/d4.txt', 'r') 
# inputs = open(os.getcwd() + '/inputs/myInputs/d4.txt', 'r') 
lines = inputs.readlines()


def isValid(ps):
	return (
			ps.find('byr:') > -1 and 
		 	ps.find('iyr:') > -1 and
		 	ps.find('eyr:') > -1 and
		 	ps.find('hgt:') > -1 and
		 	ps.find('hcl:') > -1 and
		 	ps.find('ecl:') > -1 and
			ps.find('pid:') > -1
	)

def isValidP2(splitArr):
	print(splitArr)
 	dict = makeDict(splitArr)

	return True

def makeDict(arr):
	for item
	return {}

passport, tempPass, valids = {}, '', 0
for index, line in enumerate(lines):
	if line == '\n':
		# Part 2
		splitArray = re.split('; |, |:| ', tempPass.strip())
		if  isValid(tempPass) and isValidP2(splitArray):
			valids += 1
		tempPass = ''

		# Part 1
		# if isValid(tempPass):
		# 	valids += 1
		# tempPass = ''
	else:
		tempPass += line.strip('\n')+ ' '

# print(passport)
if isValid(tempPass):
	valids += 1	
# print(valids)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.






# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)



