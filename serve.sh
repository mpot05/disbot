#!/usr/bin/env bash

# runs the bot, routinely checking for updates from git.
# a bit of a janky script sure, but its pretty convenient i guess.

# python path
PYTHON_CMD="python3.12"

# main python file
MAIN_PY="disbot.py"

# update interval (in seconds, currently set to every 10 minutes)
UPDATE_INTERVAL=1800

# command to run when updating (git pull)
REFRESH_CMD="git pull origin main"

# process id of the python script, gets set in main loop
PID=0

# runs if you ctrl+c the process, exiting python and this script.
function clean_up() {
    echo $PID

    # kill python
    if [[ $PID -ne 0 ]]
    then
        kill $PID
    fi

    # exit script
    exit 0
}

# set clean_up to run when ctrl+c is pressed
trap clean_up SIGINT

# while true
while [ 1 ]
do
    # run the script
    $PYTHON_CMD $MAIN_PY &

    # get the pid of the last run command, aka our script
    PID=$!

    # wait
    sleep $UPDATE_INTERVAL

    # kill the process (if it got set correctly)
    if [[ $PID -ne 0 ]]
    then
        kill $PID
    fi

    # reset process id
    PID=0

    # run the refresh command (in this instance, git pull)
    $REFRESH_CMD
done
