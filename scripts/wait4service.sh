#!/bin/bash

HOST=$1
PORT=$2

test $HOST && test $PORT || exit 0

echo "Waiting for ${HOST}:${PORT}"
while [ `echo "" | nc -w 5 --send-only ${HOST} ${PORT} &> /dev/null; echo $?` -ne 0 ]; do
    sleep 1
    echo -n '.'
done
echo SUCCESS

