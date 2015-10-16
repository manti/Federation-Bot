#   FedPostController.py
#   Description:FedPost Controller

from Bot import app
import flask
import requests
import json
url ='?api_key=' +app.config['API_KEY'] + '&api_username=' + app.config['API_USER_NAME']
def get():
    return "sucess"

def fed_post():
    post_data = flask.request.get_json()
    if 'http' in post_data['raw'] or 'https' in post_data['raw']:
	    response = requests.post(app.config['HOST']+'posts' + url, data=json.dumps(post_data), headers={"content-type":"application/json"})
        return response.json()

def get_fed_post():
	data = requests.get(app.config['HOST'] + 'latest.json' + url)
	return data.json()['topic_list']['topics'][2]
