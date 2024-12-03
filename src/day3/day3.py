import re

dataTest = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
dataTest2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def part1(data):
	pattern = r'mul\((\d+),(\d+)\)'
	matches = re.findall(pattern, data)

	print("Found matches:")
	result = 0
	for match in matches:
		result = result + int(match[0]) * int(match[1])

	print(result)

def part2(data):
	pattern = r'don\'t\(\)[\s\S]*?(do\(\)|$)'
	matches = re.sub(pattern, "", "do()"+data+"don't()")
	part1(matches)

part1(dataTest)
# 161
part1(open("input-day-3.txt", "r").read())
# 189527826

part2(dataTest2)
# 48
part2(open("input-day-3.txt", "r").read())
# 85151559 to high
# 44922961 to low
# 64568611
# 63013756
