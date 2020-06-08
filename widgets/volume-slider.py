#!/usr/bin/env python3
"""Volume slider widget

This is a "Custom Apple Script Slider Widget" type.
In the widget config add (*fix paths yourself*)
```
return do shell script ("~/miniconda3/bin/python ~/Downloads/home-assistant-macbook-touch-bar/widgets/volume-slider.py --entity_id media_player.kef_lsx --state")
```
and in the "Action Configuration" add
```
on bttWidgetSliderMoved(sliderValue)
	set cmd to "~/miniconda3/bin/python ~/Downloads/home-assistant-macbook-touch-bar/widgets/volume-slider.py --entity_id media_player.kef_lsx --set " & sliderValue
	do shell script cmd
end bttWidgetSliderMoved
```
"""
import argparse

from utils import entity, service

parser = argparse.ArgumentParser()
parser.add_argument("--entity_id", action="store", required=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--state", action="store_true")
group.add_argument("--set", action="store")
args = parser.parse_args()

domain = args.entity_id.split(".")[0]

if args.state:
    state = entity(args.entity_id)
    volume_level = state["attributes"]["volume_level"] if state["state"] == "on" else 0
    print(volume_level)
else:  # setting the state
    volume_level = round(float(args.set.replace(",", ".")), 2)
    response = service(domain, "volume_set", args.entity_id, volume_level=volume_level)
    print(f"Setting volume={volume_level}")
