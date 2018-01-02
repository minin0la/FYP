import json
from dataIO import fileIO

settings = fileIO("data/settings.json", "load")

print(settings[0])