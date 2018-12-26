#!/bin/bash

#1. install logkeys and magick
#2. make /opt/sys
#3. make /opt/sys/log
#4. make /opt/sys/shots
#5. make /opt/sys/src
#6. make all directories read/write/execute ready
#7. copy scripts from src/ to /opt/sys/src
#8. make all scripts be able to execute
#9. copy logkeys to /etc/init.d/
#10. Add contrad job for bootstrap.sh to run every 15 minutes daily
# add to user crontab --
  */15 *   *   *   *    export DISPLAY=:1 && scrot  ~/tempCache.png
# add to systemwide crontab --
*/15  *    * * *   root    cd /opt/sys/src/  && ./bootstrap.sh > joblog.txt 2>&1
#turn off beep sounds
