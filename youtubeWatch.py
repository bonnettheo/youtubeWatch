import time
import sys
from urllib.request import urlopen
import json
from selenium import webdriver

#api_key can be found here https://console.developers.google.com
def check_for_video(api_key):
	channel_id = "UCXPdZsu8g1nKerd-o5A75vA"

	base_video_url = "https://www.youtube.com/watch?v="
	base_search_url = "https://www.googleapis.com/youtube/v3/search?"

	url = base_search_url + 'key={}&channelId={}&part=snippet,id&orderdata&maxResult=1'.format(api_key, channel_id)
	inp = urlopen(url)
	resp = json.load(inp)

	vidID = resp['items'][0]['id']['videoId']

	videoExist = False
	with open('videoId.json', 'r') as json_file:
		try:
			data = json.load(json_file)
		except:
			data = {}
			data['videoId'] = -1

		if data['videoId'] != vidID:
			driver = webdriver.Firefox()
			driver.get(base_video_url+vidID)
			videoExist = True

	if videoExist:
		with open('videoId.json', 'w') as json_file:
			data = {'videoId':vidID}
			json.dump(data, json_file)

try:
	while True:
		with open('api.key', 'r') as api_key_file:
			check_for_video(api_key_file.read()[:-1])
			time.sleep(10)
except KeyboardInterrupt:
	print('exiting')
	quit()
