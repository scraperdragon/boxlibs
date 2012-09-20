#!/usr/bin/env python
import os
import json

try:
    f = open('/home/scraperwiki.json')
except IOError:
    # f = open('scraperwiki.json')
    print 'This must be run on the box, and the box must have a valid scraperwiki.json file.'

config_text = f.read()

try:
    config = json.loads(config_text)
except ValueError:
    print 'Malformed scraperwiki.json file'

try:
    token = config['publish_token']
except:
    print 'No publish_token is set in scraperwiki.json.'

print 'http://box.scraperwiki.com/' + os.environ['USER'] + '/' + token + '/http/overview/'
