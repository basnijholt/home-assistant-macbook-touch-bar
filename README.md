# home-assistant-macbook-touch-bar
Displaying Home Assistant sensors in the Macbook Pro's touch bar using BTT

To install a widget on your touch bar

1. open BetterTouchTool
2. select Touch Bar (⌘1)
3. click on (+) sign
4. at "Select Trigger" → "Touch Bar Widgets" → "Shell Script / Task Widget"
5. at "Launch Path" leave `/bin/bash` and at "Parameters" leave `-c`
6. at "Script" add `FULL_PYTHON_PATH PATH_TO_WIDGET OPTIONAL_ARGUMENT`, for the full Python path, use `which python`, e.g., `/Users/basnijholt/miniconda3/bin/python /Users/basnijholt/Downloads/home-assistant-macbook-touch-bar/living-room-lights.py state`

If the widget has an action associated with it, continue

7. at "Assigned Action(s)" click on "Click here & select action ►" → "Controlling Other Applications" → "Execute Shell Script / Task"
8. repeat step 5. and 6.
6. pass the right argument to the script
