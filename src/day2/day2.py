inputTestPart1="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

resultTestPart1=["Safe", "Unsafe", "Unsafe", "Unsafe", "Unsafe", "Safe"]
resultTestPart2=["Safe", "Unsafe", "Unsafe", "Safe", "Safe", "Safe"]


def part1(data):
	safeCounter = 0
	rows = data.strip().split("\n")
	results = []

	for row in rows:
		row = row.split(" ")
		print(row)
		isSafe = checker(row)
		if isSafe:
			results.append("Safe")
			safeCounter += 1
		else:
			results.append("Unsafe")

	print(safeCounter)
	return results



def testPart1():
	results = part1(inputTestPart1)
	for i, res in enumerate(resultTestPart1):
		if i >= len(results) or res != results[i]:
			print("error with index " + str(i))
			print(inputTestPart1.split("\n")[i])
			return
	print("all good")

def checker(row):
	sign = 0
	
	for i in range(len(row) - 1):
		differ = int(row[i]) - int(row[i+1])
		if sign == 0 and differ > 0:
			sign = 1
		if sign == 0 and differ < 0:
			sign = -1
		if differ > sign and sign == -1:
			return False
		
		if differ < sign and sign == 1:
			return False
		
		if differ == 0:
			return False
		if abs(differ) > 3:
			return False
		
	return True

# def part2(data):
# 	safeCounter = 0
# 	rows = data.split("\n")
# 	results = []

# 	for row in rows:
# 		row = row.split()
# 		lock = 0
# 		sign = 0
# 		tolerance = 0

		

# 		# print(row)
# 		for i, value in enumerate(row):
# 			if tolerance == 1 and lock == 0:
# 				lock = 1
# 				continue

# 			if tolerance > 1:
# 				results.append("Unsafe")
# 				break

# 			if i == len(row) - 1:
# 				safeCounter += 1
# 				results.append("Safe")
# 				break

# 			# tolerance = checker(value, row[i+1], sign)
# 			# if tolerance == 1 and i != 0:
# 			# 	tolerance += checker(row[i-1], row[i+1], sign)
# 			# 	continue

# 			if i == len(row) - 1:
# 				safeCounter += 1
# 				results.append("Safe")

# 	print(safeCounter)
# 	return results

# def testPart2():
# 	results = part2(inputTestPart1)
# 	for i, res in enumerate(resultTestPart2):
# 		if i >= len(results) or res != results[i]:
# 			print("error with index " + str(i))
# 			print(inputTestPart1.split("\n")[i])
# 			return
# 	print("all good")

testPart1()
part1(open("input-day-2.txt", "r").read())
# 598
# testPart2()
# part2(open("input-day-2.txt", "r").read())
