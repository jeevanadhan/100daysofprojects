import csv,pandas
with open("weather_condition.csv") as file:
    data=pandas.read_csv(file)
    temp_list=data["temp"].to_list()
    print(temp_list)
    total=0
    avg=sum(temp_list)/len(temp_list)
    print(f"average = {round(avg,2)}")
    max_value=data["temp"].max()
    print(f"the maximum value is {max_value}")
    monday=data[data.day == "Monday"]
    monday_temp=monday.temp[0]
    far= (monday_temp * 9 / 5) + 32
    print(f"the fahrenhiet of monday = {far}")