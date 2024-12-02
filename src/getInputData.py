import requests
import os

def getInputData(day):
	url = "https://adventofcode.com/2024/day/" + str(day) + "/input"
	cookies = {'session': os.environ.get('COOKIE_DATA')}
	folder = "./day" + str(day) + "/"
	file =  "input-day-" + str(day) + ".txt"
	path = folder + file

	if os.path.exists(folder) is False:
		os.makedirs(folder)
		os.chown(folder, 1000, 1000) 
		os.chmod(folder, 0o755)
		print("folder created")

	if os.path.exists(path):
		print("file already exists")
		return

	req = requests.get(url, cookies=cookies)
	print("input get from day " + str(day))
	print(path)
	fd = open(path, "w")
	fd.write(str(req.text))
	fd.close()
	os.chown(path, 1000, 1000) 
	os.chmod(path, 0o755)
	print("file created")

# python -i getInputData.py 