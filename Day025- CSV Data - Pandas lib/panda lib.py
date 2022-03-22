# with open("weather_data.csv") as file:
#     data=file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_files:
#     data=csv.reader(data_files)
#     temperature=[]
#     for row in data:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
data=pandas.read_csv("weather_data.csv")
# print(data)
# print(data['temp'])
# temp_list=data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list)/len(temp_list))
#
# print(data["temp"].mean())
#
# print(data["temp"].max())

# to get data in column
# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# monday_temp=int(monday.temp)
# monday_temp_F=(monday_temp*(9/5)+32)
# print(monday_temp_F)

# Create a dataFrame
data_dict={
    "student":["johny","Jack","angel"],
    "score":[33,34,35]
}

datas=pandas.DataFrame(data_dict)
datas.to_csv("new_data.csv")