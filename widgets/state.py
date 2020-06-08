import argparse
import json

from utils import entity, icon_folder

parser = argparse.ArgumentParser()
parser.add_argument("--entity_id", action="store", required=True)
parser.add_argument("--icon", action="store")
args = parser.parse_args()

info = entity(args.entity_id)
state = info["state"].replace("_", " ")
unit = info.get("attributes", {}).get("unit_of_measurement", "")
info = dict(text=f"{state} {unit}")
if args.icon:
    # download icons from https://github.com/encharm/Font-Awesome-SVG-PNG
    # and place them in `../icons/`
    info["icon_path"] = str(icon_folder / args.icon)
print(json.dumps(info))
