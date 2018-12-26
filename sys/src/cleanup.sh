#!/bin/bash

logPath="/opt/sys/log"
screenshotPath="/opt/sys/shots"

cd $logPath

logFileToRemove=`ls | grep "keys*"`
rm $logFileToRemove
touch keys.log

cd $screenshotPath

rm *.png