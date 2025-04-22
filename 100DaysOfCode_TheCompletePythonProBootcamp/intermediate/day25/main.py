import pandas

# # import csv

# # with open("./weather_data.csv", "r") as weather:
# #     data = csv.reader(weather)
# #     temperatures =[]
    
# #     temperatures_raw = []
# #     for row in data:
# #         temperatures_raw.append(row[1])
        
# #     for i in temperatures_raw[1::]:
# #         temperatures.append(int(i))
        
# #     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data)

# data_dict = data.to_dict()

# data_json = data.to_json

# # print(data_dict)
# # print(data_json)

# temp_list = data["temp"].to_list()

# # to find the average, we need to add all items inside the list and divide 
# # the sum by number of items in the list

# # sum = 0

# # for n in temp_list:
# #     sum += n

# # # or just use sum(temp_list) and don't be cringe


# # t_avg = round((sum / len(temp_list)), 2)

# # print(t_avg)

# # avg = data["temp"].mean()

# # avg = round(avg, 1)

# # print(avg)

# # max = data.temp.max()
 
# # print(data[data.temp == max])

# monday = data[data.day == "Monday"]

# monday_temp = monday.temp

# monday_temp_fhr = (monday_temp * 9/5) + 32

# print(monday_temp_fhr)


# SQUIRRELS

squirrels = pandas.read_csv('2018_Central_Park_Squirrel_Census.csv')

gray = squirrels[squirrels["Primary Fur Color"] == "Gray"]
black = squirrels[squirrels["Primary Fur Color"] == "Black"]
cinnamon = squirrels[squirrels["Primary Fur Color"] == "Cinnamon"]

total_gray =(len(gray))
total_black =(len(black))
total_red =(len(cinnamon))

squirrel_counting = {"Fur Color": ["Gray", "Black", "Red"],
                     "Total COunt": [total_gray, total_black, total_red]}

squirrel_count = pandas.DataFrame(squirrel_counting)
squirrel_count.to_csv("./squirrel_count.csv")