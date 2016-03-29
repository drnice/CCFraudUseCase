#!/usr/bin/python
#version 0.2 output all in a single line
#version 0.3 converted to json format
#version 0.4 added time to the transaction
#version 0.5 format as GeoJSON (http://geojson.org/geojson-spec.html) for use with mapping APIs

#added parameters to pass to the python script
#pass filename of name_cc completed
#pass filename of zipcod completed
#how many transactions to create in one script execution ***still working on this
#script executions to fraudulent transactions to make ***stil working on this

import os
import random
import sys
import readline
import json
import time
import getopt

def main(argv):
    global filezip
    global filecc
    global num_of_trans
    global num_before_fraud
    try:
        opts, args = getopt.getopt(argv,"h:c:z:i:f:",["cfile=","zfile=","iterations=","fraud="])
    except getopt.GetoptError:
        sys.stdout.write('readrandom0.5.py -c <input_cc_file> -z <input_zip_file> -i <# of transactions> -f <# of transactions before fraud>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            sys.stdout.write('readrandom0.5.py -c <input_cc_file> -z <input_zip_file> -i <# of transactions> -f <# of transactions before fraud>')
            sys.exit()
        elif opt in ("-c", "--cfile"):
            filecc = arg
        elif opt in ("-z", "--zfile"):
            filezip = arg
        elif opt in ("-i", "--interations"):
            num_of_trans = arg
        elif opt in ("-f", "--fraud"):
            num_before_fraud = arg

def get_random_line(file_name):
    total_bytes = os.stat(file_name).st_size
    random_point = random.randint(0, total_bytes)
    file = open(file_name)
    file.seek(random_point)
    file.readline()
    return file.readline()

filezip=''
filecc=''
num_of_trans=''
num_before_fraud=''

if __name__ == "__main__":
    main(sys.argv[1:])

if filecc =='':
    filecc = 'name_cc.csv'
    
if filezip == '':
    filezip = 'zipcode.csv'



linezip=get_random_line(filezip).rstrip('\r\n')
linecc=get_random_line(filecc).rstrip('\r\n')
transaction_comma=linecc+','+linezip
splitstring=transaction_comma.split(',')

transaction={'type':'Feature', 'properties': {'date':int(time.time()), 'fname':splitstring[0], 'lname':splitstring[1], 'cc':splitstring[2], 'zip':splitstring[3], 'city':splitstring[4], 'state':splitstring[5], 'cost':random.randint(1,800)}, 'geometry':{'type':'Point', 'coordinates':[float(splitstring[6]), float(splitstring[7])]}}

sys.stdout.write(json.dumps(transaction))
