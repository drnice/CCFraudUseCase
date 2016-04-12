# CCFraudUseCase

The CCFraudUseCase Demo demonstrate the capabilities within a modern data architecture to integrate Hortonworks Hadoop technologies to quickly 
supplement new insights into existing organic environment that need to quickly add additional functionality handling new data sources.

We demonstrate the ability to stream content using Apache Nifi - we use JSON object in this case generate to simulate CC transaction.
Within the Nifi data flow we demonstrate the ability to route the stream based on specific key within the stream payload.

Nifi would allow us also to spin up web instances that respond to a specific URL. We demonstrate the capability to interact in Real time 
with such instances to deploy a real time Web UI that shows a map with our simulated CC transaction events.

The Nifi flow also writes our content into our HDP cluster at a specific HDFS directory, which is setup to allow us immidiate query capability on 
the ingested content. 
 

# Data Generation tool
Data generation using python scripte along with two data files (name_cc.csv and zipcode.csv).

all files below need to reside in the same directory - for now.

Execute command as follows:

python readrandom0.5.py

output looks like the following of the above python script

{
  "geometry": {
    "type": "Point",
    "coordinates": [
      42.980323,
      -77.42022
    ]
  },
  "type": "Feature",
  "properties": {
    "lname": "Sexton",
    "cc": "5377 2269 9354 2898",
    "state": "NY",
    "cost": 23,
    "zip": "14564",
    "fname": "Daria",
    "city": "Victor",
    "date": 1459173501
  }
}

# installation steps

1. Install an HDP cluster 
1.1 You can Ambari to install your cluster or download a sanbox for the Hortonworks web site at:
http://hortonworks.com/products/sandbox/#download-install
(this demo worked with HDP 2.4 as well as HDP 2.3)

2. Set up a local web service:
