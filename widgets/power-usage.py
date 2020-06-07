import json

from utils import entity, icon_folder

info = entity("sensor.power_consumption")
state = info["state"].replace("_", " ")
unit = info["attributes"].get("unit_of_measurement", "")
icon = str(
    icon_folder / "fa-flash.png"
)  # from https://github.com/encharm/Font-Awesome-SVG-PNG
info = dict(text=f"{state} {unit}", icon_path=icon)
print(json.dumps(info))
