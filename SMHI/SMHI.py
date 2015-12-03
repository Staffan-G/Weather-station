import urllib.request
import json
import datetime
import pprint
import io
import tkinter as tk
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

dag2Tid = []
dag2Temp = []
dag2Neder = []
dag2Snö = []
dag2Moln = []

dag3Tid = []
dag3Temp = []
dag3Neder = []
dag3Snö = []
dag3Moln = []




#iterera genom lista
for i in range(0, len(j_obj2['timeseries'])):

    #om morgondagens datum finns
    if str(dag2.date()) in str(j_obj2['timeseries'][i]['validTime']):

        #iterera genom tider för morgondagens datum
        for j in range(0, len(tider)):            

            #om tider i datum finns, skriv till listor
            if tider[j] in str(j_obj2['timeseries'][i]['validTime']) and str(dag2.date()) in str(j_obj2['timeseries'][i]['validTime']):
                dag2Tid.append(str(tider[j]))
                dag2Temp.append(str(j_obj2['timeseries'][i]['t']))
                dag2Neder.append(str(j_obj2['timeseries'][i]['pit']))
                dag2Snö.append(str(j_obj2['timeseries'][i]['pis']))
                dag2Moln.append(str(j_obj2['timeseries'][i]['tcc']))
                print(str(dag2.date()) + tider[j] + ": " + dag2Temp[j] + " grader. Nederbörd: " + dag2Neder[j] + "mm. Moln: " + dag2Moln[j])


    
    if str(dag3.date()) in str(j_obj2['timeseries'][i]['validTime']): 
        
        for k in range(0, len(tider)):
            
            if tider[k] in str(j_obj2['timeseries'][i]['validTime']):
                dag2Tid.append(str(tider[j]))
                dag3Temp.append(str(j_obj2['timeseries'][i]['t']))
                dag3Neder.append(str(j_obj2['timeseries'][i]['pit']))
                dag3Snö.append(str(j_obj2['timeseries'][i]['pis']))
                dag3Moln.append(str(j_obj2['timeseries'][i]['tcc']))
                                
                print(str(dag3.date()) + tider[k] + ": " + dag3Temp[-1] + " grader. Nederbörd: " + dag3Neder[-1] + "mm. Moln: " + dag3Moln[-1])


  




class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self, 10,2)
        t.pack(side="top", fill="x")
        t.set(0,0,"Hello, world")
        t.set(0,1,"hej vad det går")

class SimpleTable(tk.Frame):
    def __init__(self, parent, rows = 10, columns = 2):
        # use black background so it "peeks through" to 
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="%s/%s" % (row, column), 
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()   
                
        


    
