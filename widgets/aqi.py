#!/usr/bin/env python3
# AQI widget
#
# Uses an AQI sensor value to display the numeric AQI (or text if passed in)
# Also colors the widget to represent status (e.g. Yellow = moderate)
# RGB Colors from https://www.weather.gov/phi/air_quality
# Tested using the AirVisual Cloud API:
# https://www.home-assistant.io/integrations/airvisual/
# Example entity used:
# sensor.u_s_air_quality_index

import argparse
import json

from utils import entity, icon_folder, service

parser = argparse.ArgumentParser()
parser.add_argument("--entity_id", action="store", required=True)
parser.add_argument("--icon", action="store")
parser.add_argument(
    "--text",
    action="store",
    help="Optionally overwrite the text to display (instead of the state).",
)
args = parser.parse_args()

state = entity(args.entity_id)["state"]

aqi = int(state)
if aqi <= 50:
    background_color = "0,228,0,255"
elif aqi <= 100:
    background_color = "255,255,0,255"
elif aqi <= 150:
    background_color = "255,126,0,255"
elif aqi <= 200:
    background_color = "255,0,0,255"
elif aqi <= 300:
    background_color = "153,0,76,255"
else:
    background_color = "76,0,38,255"

info = dict(
    text=state if args.text is None else args.text,
    background_color=background_color,
)
if args.icon:
    # download icons from https://github.com/encharm/Font-Awesome-SVG-PNG
    # and place them in `../icons/`
    info["icon_path"] = str(icon_folder / args.icon)

print(json.dumps(info))