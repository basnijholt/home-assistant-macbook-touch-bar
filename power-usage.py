import json

from utils import entity, this_folder

state = entity("sensor.power_consumption")["state"].replace("_", " ")
icon = str(
    this_folder / "fa-flash.png"
)  # from https://github.com/encharm/Font-Awesome-SVG-PNG
info = dict(text=f"{state} kWh", icon_path=icon)
print(json.dumps(info))
