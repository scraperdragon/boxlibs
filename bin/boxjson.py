import json

jsonfile='/home/scraperwiki.json'

def getjson():
    str_data=open(jsonfile,'r').read()
    return json.loads(str_data)  

def savejson(data):
    str_data=json.dumps(data)
    fh=open(jsonfile, 'w')
    fh.write(str_data)
    fh.close()

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

