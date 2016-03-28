#version 0.2 output all in a single line
#version 0.3 converted to json format
#version 0.4 added time to the transaction
#version 0.5 format as GeoJSON (http://geojson.org/geojson-spec.html) for use with mapping APIs
import os
import random
import sys
import readline
import json
import time
 
def get_random_line(file_name):
    total_bytes = os.stat(file_name).st_size
    random_point = random.randint(0, total_bytes)
    file = open(file_name)
    file.seek(random_point)
    file.readline()
    return file.readline()

linezip=get_random_line(file_name='zipcode.csv').rstrip('\r\n')
linecc=get_random_line(file_name='name_cc.csv').rstrip('\r\n')
transaction_comma=linecc+','+linezip
splitstring=transaction_comma.split(',')

transaction={'type':'Feature', 'properties': {'date':int(time.time()), 'fname':splitstring[0], 'lname':splitstring[1], 'cc':splitstring[2], 'zip':splitstring[3], 'city':splitstring[4], 'state':splitstring[5], 'cost':random.randint(1,800)}, 'geometry':{'type':'Point', 'coordinates':[float(splitstring[6]), float(splitstring[7])]}}

sys.stdout.write(json.dumps(transaction))
