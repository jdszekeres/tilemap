import os
import base64
import glob
from PIL import Image
from io import BytesIO
import subprocess

def tile(lat, lon, zoom=10, width=10, height=5, type="y"):
    os.environ["GOMATI_LATITUDE"] = str(lat)
    os.environ["GOMATI_LONGITUDE"] = str(lon)
    os.environ["GOMATI_ZOOM"] = str(zoom)
    os.environ["GOMATI_WIDTH"] = str(width)
    os.environ["GOMATI_HEIGHT"] = str(height)
    os.environ["GOMATI_TYPE"] = str(type)
    my_env = os.environ.copy()
    if type == "t":
        subprocess.call(["./gomati.terrain.sh"], env=my_env)
    else:
        subprocess.call(["./gomati.sh"," -q"], env=my_env)
    print(os.listdir(), glob.glob("*.jpg"))
    image = Image.open(glob.glob("*.jpg")[0])
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    img_base64 = bytes("data:image/jpeg;base64,", encoding='utf-8') + img_str
    os.system("rm %s; rm -rf gomati-tiles" % glob.glob("*.jpg")[0])
    return img_base64.decode("utf-8")
if __name__ == "__main__":
    tile(32.991527, -117.250062, zoom=20)