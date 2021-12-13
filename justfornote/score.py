import requests
from datetime import datetime

time = datetime.now()
timeString = str(time)
UserName = 'Apple1'
score = 10000

dictToSend = {'UserName': UserName, 'GameTime':timeString, 'GameScore': score}

res = requests.post('http://127.0.0.1:5000/score', json=dictToSend)