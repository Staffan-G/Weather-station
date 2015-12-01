﻿import urllib.request
import json
import datetime
import pprint
import io
import tkinter
from tkinter import *
from tkinter import ttk

# hämta rapport
smhiRapport = urllib.request.urlopen("http://opendata-download-metfcst.smhi.se/api/category/pmp1.5g/version/1/geopoint/lat/57.69/lon/11.96/data.json")


#gör om till listobjekt
str_response = smhiRapport.read().decode('utf-8')
j_obj2 = json.loads(str_response)

#skapa datumobjekt, dag2 är imorgon
dag2 = datetime.datetime.now() + datetime.timedelta(days=1)
dag3 = datetime.datetime.now() + datetime.timedelta(days=2)
dag4 = datetime.datetime.now() + datetime.timedelta(days=3)
#dag2 += datetime.timedelta(days=1)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(j_obj2['timeseries'][17])

#gör lista av datum och tid
tider = ['07:00', '09:00', '11:00', '13:00', '15:00', '18:00']

dag2Temp = []
dag2Neder = []
dag2Snö = []
dag2Moln = []

dag3Temp = []
dag3Neder = []
dag3Snö = []
dag3Moln = []

dag4Temp = []
dag4Neder = []
dag4Snö = []
dag4Moln = []



#iterera genom lista
for i in range(0, len(j_obj2['timeseries'])):

    #om morgondagens datum finns
    if str(dag2.date()) in str(j_obj2['timeseries'][i]['validTime']):

        #iterera genom tider för morgondagens datum
        for j in range(0, len(tider)):            

            #om tider i datum finns, skriv till listor
            if tider[j] in str(j_obj2['timeseries'][i]['validTime']) and str(dag2.date()) in str(j_obj2['timeseries'][i]['validTime']):
                  dag2Temp.append(str(j_obj2['timeseries'][i]['t']))
                  dag2Neder.append(str(j_obj2['timeseries'][i]['pit']))
                  dag2Snö.append(str(j_obj2['timeseries'][i]['pis']))
                  dag2Moln.append(str(j_obj2['timeseries'][i]['tcc']))
                  print(str(dag2.date()) + tider[j] + ": " + dag2Temp[j] + " grader. Nederbörd: " + dag2Neder[j] + "mm. Moln: " + dag2Moln[j])


    
    if str(dag3.date()) in str(j_obj2['timeseries'][i]['validTime']): 
        
        for k in range(0, len(tider)):
            
            if tider[k] in str(j_obj2['timeseries'][i]['validTime']):

                dag3Temp.append(str(j_obj2['timeseries'][i]['t']))
                dag3Neder.append(str(j_obj2['timeseries'][i]['pit']))
                dag3Snö.append(str(j_obj2['timeseries'][i]['pis']))
                dag3Moln.append(str(j_obj2['timeseries'][i]['tcc']))
                                
                print(str(dag3.date()) + tider[k] + ": " + dag3Temp[-1] + " grader. Nederbörd: " + dag3Neder[-1] + "mm. Moln: " + dag3Moln[-1])


  

#rita upp display

root = Tk()
content = ttk.Frame(root)

#lägg innehållet här

dag28 = str(dag2.hour()) + ": Regn: " + dag2Neder[0]

 
dag2Datum = ttk.Label(content, text=str(dag2.date()))
pos1 = ttk.Label(content, text=dag28)


    

#sätter ut ett grid
content.grid(column=0, row=0)

#placerar namelb på plats 0,0
dag2Datum.grid(column=0, row=0)
pos1.grid(column=0, row=2, sticky=(W))


root.mainloop()

                    
                
        


    
