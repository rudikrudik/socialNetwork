#!/bin/bash
while read -r line;
do
  IFS=","
  set -- "$line"
  declare -a PARAMS="( $1 )"
  first_name="${PARAMS[0]}"
  last_name="${PARAMS[1]}"
  data=$2
  city=$3

  psql -U admin -d api -c "INSERT INTO(first_name, last_name, birthday, city) VALUES($first_name, $last_name, $data, $city)"
done < users.txt
