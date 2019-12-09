#!/bin/bash
city=$1

getweather() {
wget -q https://yandex.ru/pogoda/$city -O $city
temprt=$(sed 's~temp">~QQQ~g' $city | sed 's~<~GGG~g' | sed 's~^.*QQQ~ ~' | sed 's~GGG.*$~ ~')
echo Current temperature in $city is $temprt
rm $city
}

if [[ -z "$city" ]]; then
    echo "Please specify a city"
else
    getweather
fi
