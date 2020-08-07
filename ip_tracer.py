import os 
import urllib2
import json

while True:
    ip = input("Enter Your Target Ip Address >> ")
    url = "http://ip-api.com/json"
    response = urllib2.urlopen(url + str(ip))
    data = response.read()
    values = json.loads(data)
    print("IP: " + values['query'])
    print("Contiinent >> " + values['continent'])
    print("Country >> " + values['country'])
    print("Region >> " + values['regionName'])
    print("City >> " + values['city'])
    print("Zip >> " + values['zip'])
    print("Latitude >> " + values['lat'])
    print("Longitude >> " + values['lon'])
    print("ISP >> " + values['isp'])
    
