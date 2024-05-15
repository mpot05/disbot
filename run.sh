#!/usr/bin/env bash

# runs the bot, routinely checking for updates from git.
# a bit of a janky script sure, but its pretty convenient i guess.

PYTHON_CMD="python3.10"
MAIN_PY="disbot.py"

UPDATE_INTERVAL=30

REFRESH_CMD="git pull"

PID=0

function clean_up() {
    if [$PID -ne 0]
    then
        kill $PID
    fi

    exit 0
}

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

    # kill process if it was succesfully instantiated
    if [$PID -ne 0]
    then
        kill $PID
    fi

    # reset process id
    PID=0

    # run the refresh command (in this instance, git pull)
    $REFRESH_CMD
done
