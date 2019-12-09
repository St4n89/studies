#!/bin/bash
yr=$1

listfriday() {
for m in {1..12}
  do
    l=31
    case $m in
      2)
      l=28
      ;;
      4|6|9|11)
      l=30
    esac
    for (( d=1; d <= $l; d++ ))
      do
        wd=$(date -d "$yr-$m-$d" +%A)
        wn=$(date -d "$yr-$m-$d" +%d)
        wm=$(( 10#$wn % 2 ))
        if [[ "$wd" == "Friday" && $wm == 1 ]]; then
          echo $yr-$m-$wn is an odd $wd
        fi
      done
  done
}

if [[ -z "$yr" ]]; then
    echo "Please specify year for odd friday count"
else
    listfriday
fi
