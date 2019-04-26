## Useful links
- JetBrains Pycharm: https://www.jetbrains.com/pycharm/download/
- Python: https://www.python.org/
- Flask: http://flask.pocoo.org/
- Leaflet: https://leafletjs.com/

## Quick guide to present geographic data on web

- Download this project: https://github.com/lada-olc/simple-map/archive/master.zip
- Unzip the project
- Open Windows cmd in the project root folder
- [Optional] Activate your virtual environment
- Install Flask with `pip install Flask` to your Python
- Run these commands:
```
set FLASK_APP=simple-map.py
set FLASK_DEBUG=1
flask run
```
- Open http://localhost:5000 in your browser
- You should see a simple webpage with a map and some points in it
- Explore the `simple-map.py` file to see how the points are obtained from database
- Explore the `templates/simple-map.html` file to see how the points are added to the map
- **Edit and extend according to your needs :-)**
