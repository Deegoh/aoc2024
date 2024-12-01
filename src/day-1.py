# https://adventofcode.com/2024/day/1
def sortInput():
	input = open("input-day-1.txt", "r").read()
	rows = input.strip().split('\n')
	list0 = []
	list1 = []

	for row in rows:
		data = row.split()
		if data:
			list0.append(data[0])
			list1.append(data[1])
		
	return (list0, list1)

def day1part1():
	list0, list1 = sortInput()
	list0.sort()
	list1.sort()
	amount = 0
	for index, value in enumerate(list0):
		count = abs(int(list0[index]) - int(list1[index]))
		amount += count
	print("amount of all: " + str(amount))

def day1part2():
	list0, list1 = sortInput()
	amount = 0
	for value in list0:
		# print(list1.count(value))
		count = int(value) * int(list1.count(value))
		# print(count)
		amount += count
	print("amount of all: " + str(amount))

day1part1()
day1part2()