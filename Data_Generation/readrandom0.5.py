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
    global transaction
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

def writefile(file_trans, num, action):
    f = open(file_trans, action)
    f.write(num+'\n')
    f.close()

def readfile(file_trans, action):
    global num_of_trans
    global num_before_fraud
    loop=0
    f = open(file_trans, action)
    for line in f:
        if loop == 0:
            num_of_trans=line.rstrip('\r\n')
        else:
            num_before_fraud=line.rstrip('\r\n')
        loop=loop+1
    f.close()



filezip=''
filecc=''
num_of_trans=0
num_before_fraud=0
transaction=''
flagfraud=0

if __name__ == "__main__":
    main(sys.argv[1:])

if filecc =='':
    filecc = 'name_cc.csv'
    
if filezip == '':
    filezip = 'zipcode.csv'

if os.path.isfile('numtrans2fraud'):
    readfile('numtrans2fraud', 'r')
    num_of_trans=int(num_of_trans)
    num_before_fraud=int(num_before_fraud)
    num_before_fraud= num_before_fraud - num_of_trans
    if int(num_before_fraud)<=0:
        os.remove('numtrans2fraud')
        flagfraud=3
    else:
        writefile('numtrans2fraud', str(num_of_trans), 'w')
        writefile('numtrans2fraud', str(num_before_fraud), 'a')
elif num_of_trans != 0 and num_before_fraud != 0:
    writefile('numtrans2fraud', num_of_trans, 'w')
    writefile('numtrans2fraud', num_before_fraud, 'a')
    writefile('ccfraud','2','w')
    flagfraud=1

if num_of_trans==0:
    num_of_trans=1
for x in range(0, int(num_of_trans)):
    linezip=get_random_line(filezip).rstrip('\r\n')
    linecc=get_random_line(filecc).rstrip('\r\n')
    if os.path.isfile('ccfraud') and flagfraud == 1:
        writefile('ccfraud',linecc, 'w')
        flagfraud =2
    elif os.path.isfile('ccfraud') and flagfraud == 3:
        f = open('ccfraud', 'r')
        linecc=f.readline().rstrip('\r\n')
        f.close
        os.remove('ccfraud')

    transaction_comma=linecc+','+linezip
    splitstring=transaction_comma.split(',')

    #transaction={x :{'type':'Feature', 'properties': {'date':int(time.time()), 'fname':splitstring[0], 'lname':splitstring[1], 'cc':splitstring[2], 'zip':splitstring[3], 'city':splitstring[4], 'state':splitstring[5], 'cost':random.randint(1,800)}, 'geometry':{'type':'Point', 'coordinates':[float(splitstring[7]), float(splitstring[6])]}}}

    transaction={'type':'Feature', 'properties': {'date':int(time.time()), 'fname':splitstring[0], 'lname':splitstring[1], 'cc':splitstring[2], 'zip':splitstring[3], 'city':splitstring[4], 'state':splitstring[5], 'cost':random.randint(1,800)}, 'geometry':{'type':'Point', 'coordinates':[float(splitstring[7]), float(splitstring[6])]}}


    sys.stdout.write(json.dumps(transaction))
    sys.stdout.write('\n')
