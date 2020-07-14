import requests
from config import Config
from os import remove

def upload():
	
	headers = {'Authorization': 'Client-ID %s' % Config.CLIENT_ID}

	info = { 
		'type': 'file',
		'title': 'screenSearch Screenshot',
		'description': 'image uploaded by the screenSearch project'
	}


	image = {'image':open('ss.jpg','rb')}

	response = requests.post("https://api.imgur.com/3/upload",
								json=info,
								headers=headers,
								files=image)

	remove('ss.jpg')
	return response.json()['data']['link']