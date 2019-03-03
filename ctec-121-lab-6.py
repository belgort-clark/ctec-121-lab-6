# CTEC 121 - Clark College
# Getting Data from a Website Using an API
# by Bruce Elgort
# August 20, 2017
# Lab No. 6

'''
IMPORTANT - You will first need to install the 'requests' Python library

See the video on Canvas how to do this on Windows and OS X

JSON - Learn about JSON >>> http://www.json.org/

Answer each of the questions below within the code as comments

Question No. 1 - What does the request library do?

''' 

import urllib.request
# Question No. 2 - What does the JSON library do?
import json

def readIdeaJamData():
    # Question No. 3 - Place the URL below into your web browser. What do you see?
    url = "http://ideajam.net/ideajam/p/ij.nsf/jsonGetWhatsHot"
    # Question No. 4 - Now go to this URL >> https://codebeautify.org/jsonviewer
    # Click on "Load URL" and paste in the URL from Question No. 3. What do you see?
    print("Reading website data...")
    # Question No. 5 - What does the statement below do?
    response = urllib.request.urlopen(url)
    data = response.read()
    data = data.decode("UTF-8")
    data = json.loads(str(data))
    print("Converting JSON to Python object...")
    print("Displaying data...")
    # Question No. 6 - What is being iterated through here?
    for i in data['result']:
        print("Created By:",i['createdby'])
        print("Idea:",i['idea'])
        print("IdeaSpace:",i['ideaspace'])
        print("Tag(s):",end="")
        # Question No. 7 - What is being iterated through here?
        for j in i['tags']:
            print(j,end= " ")
        print("Body:",i['body'])
        print("IdeaID:",i['ideaid'])
        print("URL:",i['ideaurl'])
        print("Votes:",i['votes'])
        print("Status:",i['status'])
        print("Linked Idea(s):",end="")
        for j in i['linkedideaid']:
            print(j,end=" ")
        print("Additional Long Text:",i['additionallongtext'])
        print("Data Created:",i['datecreated'])
        print("Implementation Manager:",i['implementationManager'])
        print("Implementation Plan:",i['implementationPlan'])
        print("\n")
        print("Comments:")
        for j in i['comments']:
            print(j['createdby'])
            print(j['comment'])
            print(j['datecreated'])
            print("\n")
        print("\n")
        print("Program Complete")


readIdeaJamData()
