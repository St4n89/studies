#!/usr/bin/env python
#coding=UTF8

import sys
import requests
import re

def checkinput():
    if len(sys.argv) > 1:
        run = 1
        return run
    else:
        print "Please specify a city!"
        run = 0
        return run

def getweather(run):
    if run == 1:
        city = sys.argv[1]
        html = (requests.get('https://yandex.ru/pogoda/' + city)).text
        temprt = (re.search('[+-][0-9]*[°]', html)).group(0)
        print ('Current temperature in ' + city + ' is ' + temprt)
    else:
        exit()

getweather(checkinput())
