import json

from utils import entity, icon_folder

state = entity("person.marcella")["state"].replace("_", " ")
info = dict(text=f"is {state}", icon_path=str(icon_folder / "marcella.jpg"))
print(json.dumps(info))
