import json
import sys

from utils import entity, icon_folder, service

which = sys.argv[1]

domain = "light"
entity_id = "light.living_room_lights"

if which == "state":
    state = entity(entity_id)["state"]
    icon = str(
        icon_folder / "fa-lightbulb-o.png"
    )  # from https://github.com/encharm/Font-Awesome-SVG-PNG

    info = dict(
        text=state,
        icon_path=icon,
        background_color="255,255,0,255" if state == "on" else "75,75,75,255",
    )
    print(json.dumps(info))
elif which == "toggle":
    response = service(domain, "toggle", entity_id)
    print("Toggling")
else:
    raise ValueError("Incorrect option")
