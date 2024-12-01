import requests
import os

def getInputData(day):
	url = "https://adventofcode.com/2024/day/" + str(day) + "/input"
	cookies = {'session': os.environ.get('COOKIE_DATA')}
	folder = "./day" + str(day)
	path = folder + "/input-day-" + str(day) + ".txt"

	if os.path.exists(folder) is False:
		os.makedirs(folder)
		print("folder created")

	if os.path.exists(path):
		print("file already exists")
		return

	req = requests.get(url, cookies=cookies)
	print("input get from day " + str(day))
	file = open(path, "w")
	file.write(str(req.text))
	file.close()
	print("file created")

# python -i getInputData.py 