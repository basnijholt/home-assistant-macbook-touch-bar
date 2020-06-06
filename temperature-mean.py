import json

from utils import entity, this_folder

state = entity("sensor.temperature_mean")["state"]
icon = str(
    this_folder / "fa-thermometer-0.png"
)  # from https://github.com/encharm/Font-Awesome-SVG-PNG
info = dict(text=f"{state} °C", icon_path=icon)
print(json.dumps(info))
