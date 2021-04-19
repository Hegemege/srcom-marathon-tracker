# Tracker server

Simple Flask server to serve the various trackers via an HTTP API.

## Setup development environment
Install dependencies for the trackers and the flask server

```
# BeautifulSoup4 and requests used by trackers
# See requirements.txt in any of the parsers/trackers
pip install bs4 requests

pip install -r requirements.txt
```

Run local environment on port 8090
```
# Execute from repository root, for proper python packaging
export FLASK_APP=src/server/wsgi.py
flask run -p 8090
```

Trackers in `/obs` should now show some data from localhost:8090
