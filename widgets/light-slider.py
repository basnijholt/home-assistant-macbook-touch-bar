# --Slider widget--
# This is a "Custom Apple Script Slider Widget" type.
# In the widget config add (*fix paths yourself*)
#
# return do shell script ("/Users/basnijholt/miniconda3/bin/python /Users/basnijholt/Downloads/home-assistant-macbook-touch-bar/widgets/light-slider.py --state")
#
# and in the "Action Configuration" add
#
# on bttWidgetSliderMoved(sliderValue)
# 	set cmd to "/Users/basnijholt/miniconda3/bin/python /Users/basnijholt/Downloads/home-assistant-macbook-touch-bar/widgets/light-slider.py --set " & sliderValue
# 	do shell script cmd
# end bttWidgetSliderMoved
#
import argparse

from utils import entity, service

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--state", action="store_true")
group.add_argument("--set", action="store")
args = parser.parse_args()

domain = "light"
entity_id = "light.living_room_lights"

if args.state:
    state = entity(entity_id)
    brightness = 0 if state["state"] == "off" else state["attributes"]["brightness"]
    print(brightness / 255)
else:  # setting the state
    brightness = round(255 * float(args.set.replace(",", ".")))
    response = service(domain, "turn_on", entity_id, brightness=brightness)
    print(f"Setting brightness={brightness}")
