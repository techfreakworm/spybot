#!/bin/bash

logPath="/opt/sys/log"

cd $logPath
dateTime=`date '+%F_%T'`
sourceFile="keys.log"
destinationFile="keys_$dateTime.log"

cp $sourceFile $destinationFile
