# !/usr/bin/env bash
# -------------------------------------------------------------
# Script_name: Orchestrator
# Description: Create a log file with 1000 log lines
# Version: 0.1
# Author: Henrique Verissimo
# Date: 14/12/2025
# License: GNU/GPL v3.0
# -------------------------------------------------------------
# Use: absolute_path/orchestrator.sh or ./orchestrator.sh
# -------------------------------------------------------------
# Script:

[[ -f access_log.txt ]] && echo 'Error: The file "access_log.txt" already exists!' && exit 1
[[ ! -f analyzer.py ]] && echo 'Error: The "./analyzer.py" file was not found!' && exit 1

for item in $(seq 1 1000); do
    min=1577836800
    max=1735689599
    timestamp=$(( min + RANDOM % (max - min + 1) ))

    random_number=$(($RANDOM % 100 + 1))
    printf -v random_number "%03d" $random_number
    userid="user_$random_number"

    options_status_code=("200" "404" "500")
    status_code=${options_status_code[$RANDOM % ${#options_status_code[@]}]}

    response_time="$(( 50 + RANDOM % 4951 ))ms"

    echo "$timestamp $userid $status_code $response_time" >> access_log.txt
done

cat access_log.txt | grep " 200 " > successful_accesses.txt

python3 analyzer.py ./successful_accesses.txt

rm -f access_log.txt successful_accesses.txt
exit 0