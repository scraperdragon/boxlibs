import json
import datetime

"""Allows easy stting of the box's json file:

import boxjson
print boxjson.boxjson['status_message']

or

from boxjson import boxjson
print boxjson['status_message']

(but you use the message() function)
"""

jsonfile='/home/scraperwiki.json'

def getjson():
    str_data=open(jsonfile,'r').read()
    return json.loads(str_data)  

def savejson(data):
    str_data=json.dumps(data)
    fh=open(jsonfile, 'w')
    fh.write(str_data)
    fh.close()

def message(msg=None, timestamp=True):
    if timestamp:
        time=datetime.datetime.now().isoformat()[:16]
    else:
        time=''
    if msg:
        boxjson()['status_message']=str(time)+' '+str(msg)
    else:
        return boxjson()['status_message']

class boxjson():
    def __init__(self, *args):
        if len(args)>0:
            jsonfile=args[0]

    def __str__(self):
        return str(getjson())
    
    def parse(self, *args):
        if len(args)==1:
            return getjson()[args[0]]
        elif len(args)==2:
            newjson=getjson()
            newjson[args[0]]=args[1]
            savejson(newjson)
        else:
            return getjson()

    def __getattr__(self, *args, **kwargs):
        return self.parse

boxjson = boxjson()
