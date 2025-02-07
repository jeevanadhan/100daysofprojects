# import csv,pandas
# with open("weather_condition.csv") as file:
#     data=pandas.read_csv(file)
#     print(data)
#     temp_list=data["temp"].to_list()
#     print(temp_list)
#     total=0
#     avg=sum(temp_list)/len(temp_list)
#     print(f"average = {round(avg,2)}")
#     max_value=data["temp"].max()
#     print(f"the maximum value is {max_value}")
#     monday=data[data.day == "Monday"]
#     monday_temp=monday.temp[0]
#     far= (monday_temp * 9 / 5) + 32
#     print(f"the fahrenhiet of monday = {far}")
import pandas
from collections import Counter
with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as file:
    data=pandas.read_csv(file)
    gray_count=len(data[data["Primary Fur Color"]=="Gray"])
    cinnamon_count=len(data[data["Primary Fur Color"]=="Gray"])
    black_count=len(data[data["Primary Fur Color"]=="Gray"])
    data_dict={ "fur color":["gray","cinnamon","black"],
                "Count":[gray_count,cinnamon_count,black_count]}
    df=pandas.DataFrame(data_dict)
    df.to_csv("squirrel_color_count.csv")







    # values_count=data_dict.values()
    # print(values_count)