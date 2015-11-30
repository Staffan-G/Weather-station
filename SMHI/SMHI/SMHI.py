import urllib.request
import json
import datetime
import pprint

# hämta rapport
smhiRapport = urllib.request.urlopen("http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/57.69/lon/11.96/data.json")

#gör om till listobjekt
str_response = smhiRapport.readall().decode('utf-8')
j_obj2 = json.loads(str_response)

#skapa datumobjekt, dag2 är imorgon
dag2 = datetime.datetime.now()
dag2 += datetime.timedelta(days=1)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(j_obj2['timeseries'][17])

#iterera genom lista, leta efter datum och tid
for i in range(1, len(j_obj2['timeseries'])):

    if str(dag2.date()) in str(j_obj2['timeseries'][i]['validTime']):
            
                if '08:00' in str(j_obj2['timeseries'][i]['validTime']):
                    dag20800 = str(j_obj2['timeseries'][i]['t'])
                    print("Temp imorgon 08:00 " + str(j_obj2['timeseries'][i]['t']))

                if '10:00' in str(j_obj2['timeseries'][i]['validTime']):
                    dag21000 = str(j_obj2['timeseries'][i]['t'])
                    print("Temp imorgon 10:00 " + str(j_obj2['timeseries'][i]['t']))
                
        

       

        


    
