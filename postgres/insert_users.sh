#!/bin/bash
while read -r line;
do
  IFS=","
  set -- $line
  declare -a PARAMS="( $1 )"
  first_name="${PARAMS[1]}"
  last_name="${PARAMS[0]}"
  data=$2
  city=$3

  psql -U admin -d api -c "INSERT INTO users (first_name, last_name, birthday, city, password, login) VALUES('$first_name', '$last_name', '$data', '$city', '$first_name', '$last_name')"
done < users.txt
