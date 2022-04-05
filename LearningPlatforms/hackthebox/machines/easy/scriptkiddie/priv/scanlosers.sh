#!/bin/bash

log=log

cat $log | cut -d' ' -f3- | sort -u | while read ip; do
    sh -c "nmap --top-ports 10 -oN test/${ip}.nmap ${ip} 2>&1 >/dev/null" &
done

