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
1.1. You can Ambari to install your cluster or download a sanbox for the Hortonworks web site at:
http://hortonworks.com/products/sandbox/#download-install
(this demo worked with HDP 2.4 as well as HDP 2.3)

2. Set up a local web service:
You can set up you web services either on the a server or on your local mac for demo purposes. 

2.1. Installation on CentOS server:
To install apache, open terminal and type in this command:

sudo yum install httpd

2.2. Make configuration changes for your web services:

vi /etc/httpd/conf/httpd.conf

Place the content of the UI folder in the DocumentRoot location to be accessed via the webserver
DocumentRoot "/var/www/html"


2.3. Start apache by running

sudo service httpd start


3. Install Nifi:

To install Nifi on your cluster please follow the steps documented in the Ali's github:

https://github.com/abajwa-hw/ambari-nifi-service


4. Import Nifi XML template schema 

After starting Nifi, navigate to the Nifi UI.
Select the icon marked in with the right red square click it, this 
would allow you to upload an xml template, use Nifi_demo_se.xml
(Browse select and import).
Once the template is loaded you can drag the icon in the red rectangle to the UI view 
which will enable a popup menu that would display "Nifi_demo_se.xml".
After selecting this template you view should display the following Nifi flow.

![Image](../master/Screenshot/Nifi-ui1.jpg?raw=true)

Verify that the placement of the python script is on you server location in the template we have it at:
 /home/nifi/CCFraudUseCase/Data_Generation/
 
 To verify you can click the handle_requests process and click the "Ledger transaction" process, 
 right click the "Retrieve_store_Ledger" and inspect the command Arguments property.
 
 If all is good, you can start the flow by licking on the Green "Play" triangle.
 
 Now you are ready to launch your UI at the Webserver location you set up on step 2, the 
 following display will show up!
 
 ![Image](../master/Screenshot/ScreenUI-Nifi-HDP.png?raw=true)
 
 

