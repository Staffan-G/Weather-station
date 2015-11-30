import urllib.request
import json
import datetime

# hämta rapport
smhiRapport = urllib.request.urlopen("http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/57.69/lon/11.96/data.json")

#gör om till listobjekt
str_response = smhiRapport.readall().decode('utf-8')
j_obj2 = json.loads(str_response)

#iterera genom lista, skriv varje rad
print(j_obj2)

dag2 = datetime.datetime.now()

dag2 += datetime.timedelta(days=1)


for i in range(1, len(j_obj2['timeseries'])):

    if '08:00' in str(j_obj2['timeseries'][i]['validTime']):
        #print(dag2.date())
        #print(str(j_obj2['timeseries'][i]['validTime']))

        if str(dag2.date()) in str(j_obj2['timeseries'][i]['validTime']):
            
            print("Temp imorgon " + str(j_obj2['timeseries'][i]['t']))

        


    
