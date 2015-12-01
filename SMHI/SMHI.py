import urllib.request
import json
import datetime
import pprint

# hämta rapport
smhiRapport = urllib.request.urlopen("http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/57.69/lon/11.96/data.json")

#gör om till listobjekt
str_response = smhiRapport.read().decode('utf-8')
j_obj2 = json.loads(str_response)

#skapa datumobjekt, dag2 är imorgon
dag2 = datetime.datetime.now() + datetime.timedelta(days=1)
#dag2 += datetime.timedelta(days=1)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(j_obj2['timeseries'][17])

#gör lista av datum och tid
tid = ['08:00', '10:00']
list2 = []

#iterera genom lista, leta efter datum och tid
for i in range(0, len(j_obj2['timeseries'])):

    if str(dag2.date()) in str(j_obj2['timeseries'][i]['validTime']):
        for j in range(0, len(tid)):            
                        


            if tid[j] in str(j_obj2['timeseries'][i]['validTime']):
                  list2.append(str(j_obj2['timeseries'][i]['t']))
                  print("Temp imorgon 08:00 " + str(j_obj2['timeseries'][i]['t']))
                    
                
        


    
