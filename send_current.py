from PyTado.interface import Tado
import azloganalytics
import datetime
import os

tadoUsername=os.environ.get("tadoUsername")
tadoPass=os.environ.get("tadoPass")
azID=os.environ.get("azID")
azSecret=os.environ.get("azSecret")

t = Tado(tadoUsername, tadoPass)
la = azloganalytics.LogAnalytics(azID,azSecret,'pytado')

def current_data(zone):
    currentData = t.getClimate(zone=zone)
    return [{"temp":currentData['temperature'],"humidity":currentData['humidity']}]

sendData=current_data(1)
print(sendData)
la.sendtoAzure(sendData)