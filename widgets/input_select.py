#!/usr/bin/env python3
# input_select button widget
#
# Tested with an `input_select`.
# Examples:
# /Users/basnijholt/miniconda3/bin/python ~/Downloads/home-assistant-macbook-touch-bar/widgets/input_select.py --icon fa-bed.png --entity_id input_select.sleep_mode
# /Users/basnijholt/miniconda3/bin/python ~/Downloads/home-assistant-macbook-touch-bar/widgets/input_select.py --entity_id input_select.sleep_mode --icon fa-bed.png --select_next

import argparse
import json

from utils import entity, icon_folder, service

parser = argparse.ArgumentParser()
parser.add_argument("--entity_id", action="store", required=True)
parser.add_argument("--icon", action="store")
parser.add_argument("--select_next", action="store_true")
parser.add_argument(
    "--text",
    action="store",
    help="Optionally overwrite the text to display (instead of the state).",
)
args = parser.parse_args()

if args.select_next:
    domain = args.entity_id.split(".")[0]
    response = service(domain, "select_next", args.entity_id)

state = entity(args.entity_id)["state"]
info = dict(
    text=state if args.text is None else args.text,
    background_color="75,75,75,255",
)
if args.icon:
    # download icons from https://github.com/encharm/Font-Awesome-SVG-PNG
    # and place them in `../icons/`
    info["icon_path"] = str(icon_folder / args.icon)

print(json.dumps(info))
