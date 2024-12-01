import requests
import os

def get_input_data(day):
	url = "https://adventofcode.com/2024/day/" + str(day) + "/input"
	cookies = {'session': os.environ.get('COOKIE_DATA')}

	req = requests.get(url, cookies=cookies)
	print("input get from day " + str(day))
	file = open("./input-day-" + str(day) + ".txt", "w")
	file.write(str(req.text))
	file.close()
	print("file created")

# python -i getInputData.py 