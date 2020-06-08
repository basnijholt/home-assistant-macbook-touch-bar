#!/usr/bin/env bash
. ~/.bash_profile
cd `dirname $0`
python state.py --icon fa-flash.png --entity_id sensor.power_consumption
