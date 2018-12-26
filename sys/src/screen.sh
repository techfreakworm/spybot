#!/bin/bash

export DISPLAY=:1
screenshotPath="/opt/sys/shots"

cd $screenshotPath
dateTime=`date '+%F_%T'`

scrot $dateTime.png
