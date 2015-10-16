#   route_configs.py
#   Description:    ...

get_index = {
    'route': '/',
    'methods':  ['GET'],
    'description': 'Welcome to Bots world'
}

post_posts = {
    'route': '/fedpost',
    'methods':  ['POST'],
    'description': 'Post into federation'
}

post_comment = {
    'route': '/fedcomment',
    'methods':  ['POST'],
    'description': 'Post into federation'
}

get_post = {
	'route': '/post',
    'methods':  ['GET'],
    'description': 'get federation'	
}