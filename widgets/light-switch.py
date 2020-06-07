import argparse
import json

from utils import entity, icon_folder, service

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--state", action="store_true")
group.add_argument("--toggle", action="store_true")
args = parser.parse_args()

domain = "light"
entity_id = "light.living_room_lights"

if args.state:
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
elif args.toggle:
    response = service(domain, "toggle", entity_id)
    print("Toggling")
