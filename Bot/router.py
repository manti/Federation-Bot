#   router.py
#   Description:    ...

import json
from flask import Flask, Response, request
from Bot import app
import route_configs
from Bot.Controllers import FedPostController
import json

#   Index page
@app.route(
    route_configs.get_index['route'],
    methods=route_configs.get_index['methods']
)
# @authenticate
def get_index():
    return Response('Welcome to bots world!')


# Post to federation
@app.route(
    route_configs.post_posts['route'],
    methods=route_configs.post_posts['methods']
)
def post_posts():
    return Response(
        json.dumps
        (
            {
                'response': FedPostController.fed_post()
            }
        ),
        mimetype='application/json',
        status=200
    )


# Get to federation
@app.route(
    route_configs.get_post['route'],
    methods=route_configs.get_post['methods']
)
def get_post():
    return Response(
        json.dumps
        (
            {
                'response': FedPostController.get_fed_post()
            }
        ),
        mimetype='application/json',
        status=200
    )