#!/bin/bash

srcPath="/opt/sys/src"
uploadSourcePath="/opt/sys/toUpload"

cd $uploadSourcePath

cd $srcPath
./logRename.sh
echo "Logs Renamed"
#./screen.sh
echo "Screenshot captured"
./copyToUpload.sh
echo "Copied to upload directory"

photo=`ls $uploadSourcePath| grep "png"`
log=`ls $uploadSourcePath| grep "log"`

echo "variables set are:"
echo $photo
echo $log

python uploadToDrive.py $log $photo

echo "Python script executed"
cd $uploadSourcePath
rm *.png
rm *.txt

echo "files removed"
