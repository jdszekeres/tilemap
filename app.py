from flask import *
import tile
import glob
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", api=open("api.env", "r").read())
@app.route('/<lat>/<lon>/<zoom>/<width>/<height>/<types>')
def download(lat, lon, zoom, width, height, types):
    return "<img src='{}'>".format(tile.tile(lat, lon, zoom, width, height, types))
app.run(debug=True)