#   __init__.py
#   Description:    ...

from flask import Flask

app = Flask('Bot')
app.config.from_object('Bot.configs')

import router
