import urllib.request
import json
import datetime
import pprint
import tkinter

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
tider = ['08:00', '10:00', '12:00', '14:00', '16:00', '18:00']
dag2Temp = []
dag2Neder = []
dag2Snö = []
dag2Moln = []

#iterera genom lista
for i in range(0, len(j_obj2['timeseries'])):

    #om morgondagens datum finns
    if str(dag2.date()) in str(j_obj2['timeseries'][i]['validTime']):

        #iterera genom tider för morgondagens datum
        for j in range(0, len(tider)):            

            #om 
            if tider[j] in str(j_obj2['timeseries'][i]['validTime']):
                  dag2Temp.append(str(j_obj2['timeseries'][i]['t']))
                  dag2Neder.append(str(j_obj2['timeseries'][i]['pit']))
                  dag2Snö.append(str(j_obj2['timeseries'][i]['pis']))
                  dag2Moln.append(str(j_obj2['timeseries'][i]['tcc']))
                  print(tider[j] + ": " + dag2Temp[j] + " grader. Nederbörd: " + dag2Neder[j] + "mm. Moln: " + dag2Moln[j])

#rita upp display

                    
                
        


    
