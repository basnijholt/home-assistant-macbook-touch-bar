import argparse
import json

from utils import entity, icon_folder, service

parser = argparse.ArgumentParser()
parser.add_argument("--entity_id", action="store", required=True)
parser.add_argument("--icon", action="store")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--state", action="store_true")
group.add_argument("--toggle", action="store_true")
args = parser.parse_args()

if args.state:
    state = entity(args.entity_id)["state"]
    info = dict(
        text=state,
        background_color="255,255,0,255" if state == "on" else "75,75,75,255",
    )
    if args.icon:
        # download icons from https://github.com/encharm/Font-Awesome-SVG-PNG
        # and place them in `../icons/`
        info["icon"] = str(icon_folder / args.icon)

    print(json.dumps(info))
elif args.toggle:
    domain = args.entity_id.split(".")[0]
    response = service(domain, "toggle", args.entity_id)
    print("Toggling")
