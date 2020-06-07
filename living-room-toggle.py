import json

from utils import service

response = service("light", "toggle", "light.living_room_lights")
print("Toggling")
