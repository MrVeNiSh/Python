import json
from urllib.request import urlopen

def display(obj, s_params, s_date, e_date):
    print("Selected Parameters: " + ", ".join(s_params))
    print("Time Range: {} to {}".format(s_date, e_date))
    
    print("\nStation ID: " + obj["stations"][0]["stationID"])
    print("Data Table:")
    header = ["TIME"] + s_params
    print(" ".join(header))

    for entry in obj["stations"][0]["data"]:
        entry_date = entry["DATETIMEDATA"]
        if s_date <= entry_date <= e_date:
            row = [entry_date]
            for param in s_params:
                row.append(entry[param])
            print(" ".join(map(str, row)))

obj = json.load(urlopen('http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN&type=hr&sdate=2023-10-01&edate=2023-11-06&stime=00&etime=16'))

available_params = obj["stations"][0]["params"]

print("Available Parameters: " + ", ".join(available_params))
param_input = input("Enter the parameters you want to display (comma-separated): ").split(',')

s_params = [param.strip().upper() for param in param_input if param.strip().upper() in map(str.upper, available_params)]

s_date = input("Enter the start date and time (YYYY-MM-DD HH:MM): ")
e_date = input("Enter the end date and time (YYYY-MM-DD HH:MM): ")

if s_params:
    display(obj, s_params, s_date, e_date)
else:
    print("Invalid parameters selected or no parameters selected.")