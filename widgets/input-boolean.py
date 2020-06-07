import argparse
import json

from utils import entity, icon_folder, service

parser = argparse.ArgumentParser()
parser.add_argument("--entity_id", action="store", required=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--state", action="store_true")
group.add_argument("--toggle", action="store_true")
args = parser.parse_args()

if args.state:
    state = entity(args.entity_id)["state"]
    icon = str(
        icon_folder / "fa-bed.png"
    )  # from https://github.com/encharm/Font-Awesome-SVG-PNG

    info = dict(
        text=state,
        icon_path=icon,
        background_color="255,255,0,255" if state == "on" else "75,75,75,255",
    )
    print(json.dumps(info))
elif args.toggle:
    response = service("input_boolean", "toggle", args.entity_id)
    print("Toggling")
else:
    raise ValueError("Incorrect option")
