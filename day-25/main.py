# with open(f"day-25\weather_data.csv.csv") as data_file:
#             data = data_file.readlines()
#             print(data)

# import csv

# with open(f"day-25\weather_data.csv.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

# data = pandas.read_csv("day-25\weather_data.csv")
# print(type(data))
# # print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data.temp.max())

# print(data[data.temp == (data.temp.max())])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 +32
# print(monday_temp_F)


# create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("day-25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("day-25\\squirrel_count_csv")