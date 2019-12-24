#!/usr/bin/env python
import requests
import re
import sqlite3
import datetime
import sys

def checkinput():
    if len(sys.argv) > 2:
        run1 = 1
        return run1
    else:
        print "Please specify the file and text to search!"
        run1 = 0
        return run1

def checkconnection(run):
    if run == 1:
        file = str(sys.argv[1])
        address = 'https://raw.github.com/St4n89/studies/master/'+file
        try:
            response = requests.get(address)
            if str(response) == "<Response [200]>":
                run2 = 1
                return run2,address
            else:
                print ("This file does not exist in your GitHub repo.")
                run2 = 0
                return run2,address

        except requests.ConnectionError as err:
            print "Check your internet connection, GitHub not available!"
            run2 = 0
            return run2,address
    else:
        exit()

def gitcheck(run2,address):
    if run2 == 1:
        word = sys.argv[2]
        gitrequest = (requests.get(address)).text
        match = re.search(word, gitrequest)
        if str(match) == "None":
            result = "Not found"
        else:
            result = "Found"
        gettime = datetime.datetime.now()
        timestamp = str(gettime.year)+"-"+str(gettime.month)+"-"+str(gettime.day)+" "+str(gettime.hour)+":"+str(gettime.minute)+":"+str(gettime.second)
        #print (match)
        #print (result)
        return address,timestamp,word,result
    else:
        exit()

def dbwrite(address,timestamp,word,result):
    dbconnect = sqlite3.connect("database.db")
    cursor = dbconnect.cursor()
    if not address:
        print("No address")
        exit()
    else:
        try:
            cursor.execute("insert into Gitchecks (result, site, file, regex, datetime) values (?, ?, ?, ?, ?)",(result, 'Github', address, word, timestamp))
            dbconnect.commit()
            dbconnect.close()
            print ("Values inserted successfully.")
        except sqlite3.OperationalError as err:
            print ("Gitchecks table does not exist. Creating...")
            cursor.execute("""CREATE TABLE Gitchecks(result text, site text, file text, regex text, datetime text)""")
            print ("Successful. Inserting values...")
            cursor.execute("insert into Gitchecks (result, site, file, regex, datetime) values (?, ?, ?, ?, ?)",(result, 'Github', address, word, timestamp))
            print ("Successful.")
            dbconnect.commit()
            dbconnect.close()

def main():
    input = checkinput()
    connect = checkconnection(input)
    gitconnect = gitcheck(connect[0],connect[1])
    dbwrite(gitconnect[0],gitconnect[1],gitconnect[2],gitconnect[3])

main()
