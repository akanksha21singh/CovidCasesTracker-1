from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from covid import Covid
import numpy as np
from tkinter import *
root = Tk()
root.geometry("350x350")
root.title("Get Covid-19 Data Country wise")



def showdata():
    #country_names = []
    #country_names = input("Enter country names with comma: ").split(',')
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    root.update()
    countries = data.get()
    country_names = countries.strip()
    country_names = country_names.replace(" ",",")
    country_names = country_names.split(",")


    for x in country_names:
        cases.append(covid.get_status_by_country_name(x))
        root.update()
    
    for y in cases:
        confirmed.append(y["confirmed"]/100000)
        active.append(y["active"]/100000)
        deaths.append(y["deaths"]/100000)
        recovered.append(y["recovered"]/100000)
    
    casesVal = len(country_names)
    val = np.arange(casesVal)
    width = 0.2

    bar1 = plt.bar(val, confirmed, width, color= 'y')

    bar2 = plt.bar(val+width, active, width, color='b')

    bar3 = plt.bar(val+width*2, deaths, width, color= 'r')

    bar4 = plt.bar(val+width*3, recovered, width, color= 'g')


    plt.title('Current Covid Cases')
    plt.xlabel('Country Name')
    plt.ylabel('Cases(in millions)')
    plt.xticks(val+width,country_names)
    plt.legend((bar1,bar2,bar3,bar4),("confirmed","active","deaths","recovered"))
    plt.show()
Label(root, text="Enter countries\n for which you wish to get\n covid-19 data (Except USA)", font = "Console 15 bold").pack()
Label(root, text="Enter country name:").pack()
data = StringVar()
data.set("Separate country names using comma or space(not both)")
entry = Entry(root,textvariable=data,width=50).pack()
Button(root, text="Get Data", command = showdata).pack()
root.mainloop()
