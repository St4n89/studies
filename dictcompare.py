#!/usr/bin/env python
import sys
import os.path

dict1 = {}
dict2 = {}

def checkinput():
    if len(sys.argv) > 1:
        run = 1
        return run
    else:
        print "Please specify dictionary files!"
        run = 0
        return run

def dictionarize(file,dictionary):
    with file as input:
        for line in input:
            key,value = line.split(":")
            dictionary[key] = value.strip()

def dictcompare(dic1,dic2):
    different = "Different: "
    similar = "Similar: "
    d = 0
    s = 0
    list = set(dic1.keys()+dic2.keys())
    for key in list:
        if not key in dic1:
            diff = key + ":" + dic2.get(key)
            different = different + diff + " "
            d+=1
        else:
            if not key in dic2:
                diff = key + ":" + dic1.get(key)
                different = different + diff + " "
                d+=1
            else:
                if dic1.get(key) != dic2.get(key):
                    diff = key + ":" + dic1.get(key)
                    different = different + diff + " "
                    diff = key + ":" + dic2.get(key)
                    different = different + diff + " "
                    d+=1
                else:
                    sim = key + ":" + dic2.get(key)
                    similar = similar + sim + " "
                    s+=1

    if s == 0:
        similar = "Similar: None"

    if d == 0:
        different = "Different: None"

    print (str(similar))
    print (str(different))

def execute(run):
    if run == 1:
        file1 = open(sys.argv[1])
        file2 = open(sys.argv[2])
        dictionarize(file1,dict1)
        dictionarize(file2,dict2)
        dictcompare(dict1,dict2)
    else:
        exit()

def main():
    execute(checkinput())

main()
