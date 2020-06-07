import json

from utils import entity, this_folder

state = entity("light.living_room_lights")["state"]
icon = str(
    this_folder / ".." / "fa-lightbulb-o.png"
)  # from https://github.com/encharm/Font-Awesome-SVG-PNG

info = dict(
    text=state,
    icon_path=icon,
    background_color="255,255,0,255" if state == "on" else "75,75,75,255",
)
print(json.dumps(info))
