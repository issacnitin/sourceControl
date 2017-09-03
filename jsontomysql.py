import json
import urllib2
import MySQLdb

conn = MySQLdb.connect(host="localhost",
                    user="root",
                    passwd="root",
                    db="sourceControl")

x = conn.cursor()
with open("../../2015-01-01-0d42d3c3.json") as f:
    for line in f:
        jsonVal = json.loads(line)
        masterTable = {}
        actorTable = {}
        for key in (jsonVal):
            masterTable[key] = jsonVal[key]
        jsonVal = json.loads(masterTable['actor'])
        for key in jsonVal:
            print(key)
            actorTable[key] = jsonVal[key]
        x.execute("INSERT INTO sourceControl(id, type, actorid, repoid, payloadid) VALUES(%s, %s, %s, %s, %s)" % (dictionary['id'], dictionary['type'], dictionary['actor'], dictionary['repo'], dictionary['payload']))
