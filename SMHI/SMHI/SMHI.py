import urllib.request
import json

# hämta rapport
smhiRapport = urllib.request.urlopen("http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/57.69/lon/11.96/data.json")

#gör om till listobjekt
str_response = smhiRapport.readall().decode('utf-8')
j_obj2 = json.loads(str_response)


#iterera genom lista, skriv varje rad

counter = 1
for i in range(1, len(j_obj2['timeseries'])):

    if '22:00' in str(j_obj2['timeseries'][i]['validTime']):

        print (str(j_obj2['timeseries'][i]['validTime']) + " så blåser det max " + str(j_obj2['timeseries'][i]['gust']))


#age = raw_input("hur gammal")
    
