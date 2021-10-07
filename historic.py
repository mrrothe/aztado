
def historic_data():
    date=1
    d=t.getHistoric(1,date)
    temps=d['measuredData']['insideTemperature']['dataPoints']
    tempArray={}
    for temp in temps:
        print(temp['timestamp'])
        azloganalytics.sendtoAzure(("timestamp",temp['timestamp']),("temp",temp['value']['celsius']))
    #    tempArray[temp['timestamp']]=(temp['value']['celsius'])
    #heating=d['stripes']['dataIntervals'] #['dataPoints']
    #heatArray={}
    #for hear in heating:
    #    heatArray[heat['timestamp']]=(temp['value']['celsius'])

    #print(tempArray[6])
    #tadoData=t.getState(1)
    #for k,v in tadoData.items():
    #    print(k + " = " + str(v))

    #for day in range(2,24):
    #    date="2021-01-" + str(day)
    #    print(date)
    #    submitData(date)