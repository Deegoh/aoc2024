inputTestPart="""7 6 4 2 1
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



def testPart(input, resultTest, part = 1):
	result = None
	if part == 1:
		results = part1(input)
	else:
		results = part2(input)
	for i, res in enumerate(resultTest):
		if i >= len(results) or res != results[i]:
			print("error with index " + str(i))
			print(input.split("\n")[i])
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

def checker2(row, tolerence):
	sign = 0
	
	for i in range(len(row) - 1):
		
		differ = int(row[i]) - int(row[i+1])
		if sign == 0 and differ > 0:
			sign = 1
		if sign == 0 and differ < 0:
			sign = -1
		if differ > sign and sign == -1:
			row.remove(row[i])
			return checker2(row, tolerence + 1)
		
		if differ < sign and sign == 1:
			row.remove(row[i])
			return checker2(row, tolerence + 1)
		
		if abs(differ) > 3 or abs(differ) < 1:
			row.remove(row[i])
			return checker2(row, tolerence + 1)
		
	return tolerence

def part2(data):
	safeCounter = 0
	rows = data.strip().split("\n")
	results = []

	for row in rows:
		print(row, row[0:], row[0+1:])
		row = row.split(" ")
		tolerence = 0
		
		if checker2(row, tolerence) <= 1:
			results.append("Safe")
			safeCounter += 1
		else:
			results.append("Unsafe")

	print(safeCounter)
	return results

# testPart(inputTestPart, resultTestPart1)
# part1(open("input-day-2.txt", "r").read())
# 598
testPart(inputTestPart, resultTestPart2, 2)
# 622 to low
# 634
part2(open("input-day-2.txt", "r").read())


# def is_safe(row):
#     inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
#     if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
#         return True
#     return False

# with open("input-day-2.txt", "r") as file:
#     lines = [line.strip() for line in file if line.strip()]
# data = [[int(y) for y in x.split()] for x in lines]

# safe_count = sum([is_safe(row) for row in data])
# print(safe_count)

# safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
# print(safe_count)
