import json

from utils import service

response = service("input_boolean", "toggle", "input_boolean.sleep_mode")
print("Toggling")
