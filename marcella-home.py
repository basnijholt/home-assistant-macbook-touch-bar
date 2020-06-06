import json

from utils import entity, this_folder

state = entity("person.marcella")["state"].replace("_", " ")
info = dict(text=f"is {state}", icon_path=str(this_folder / "marcella.jpg"),)
print(json.dumps(info))
