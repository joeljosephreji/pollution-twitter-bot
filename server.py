import serial
import time
import requests
import json

import tweepy

fileReference = open('auth_info.json');
authInformation = json.load(fileReference);

auth = tweepy.OAuthHandler(authInformation["consumer_key"], authInformation["consumer_key_secret"])
auth.set_access_token(authInformation["access_token"], authInformation["access_token_secret"])

api = tweepy.API(auth)

firebase_url = 'https://pollution-bot.firebaseio.com/temperature'
#Connect to Serial Port for communication
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)
#Setup a loop to send Temperature values at fixed intervals
#in seconds
data = ''
while 1:
#	while ser.inWaiting()>0:
	line = ser.readline().strip()
	value = line.decode('ascii') 
	if value != 'a':
		data = data + value
	if value == 'a':
		print ('Got:', data)
		record = {'data':data}
		#result = requests.post(firebase_url, data=json.dumps(record))
		api.update_status("Pollution update guis CO2 level:"+data)
		print("Data posted\n")
		data = ''

