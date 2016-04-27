#!/bin/bash

# Make a change to reference your path in the PATH_TO_SCRIPT_LOCATION

export PATH_TO_SCRIPT_LOCATION=/home/nifi/CCFraudUseCase/Data_Generation/
#export PATH_TO_SCRIPT_LOCATION=/Users/eorgad/Demo

OUTPUT="$(python $PATH_TO_SCRIPT_LOCATION/readrandom0.5.py -i 10  -f 2)"

# Make this jar active to see the distance calculation on fraud transactions
#OUTPUT="$(java -jar $PATH_TO_SCRIPT_LOCATION/CCFraudUseCase/CCFraudUseCase-master/Data_Generation/parseJsonObjects.jar)"

echo "${OUTPUT}"
