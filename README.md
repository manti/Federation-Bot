# Federation-Bot
federation bot


```

* Copy `Bot/configs.py.sample` to `Bot/configs.py`
* Edit `Bot/configs.py` with desired configuration
* Run sudo pip install -r requirements.lock
* Run the application by invoking `main.py`

GET /post
POST /post
Data - {
"title":<post title>,
"raw": "correct url"
}
Header - {
'content-type': 'application/json'
}
```
