# based on the primary fur colors (Grey, black, cinnamon), how many are there of each?
# build a small data frame with the data

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_gray_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
squirrel_cinnamon_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
squirrel_black_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# squirrel_color_data = squirrel_data["Primary Fur Color"].value_counts()
print(squirrel_gray_data)
print(squirrel_cinnamon_data)
print(squirrel_black_data)

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Population": [2473, 392, 103]
}


squirrel_df = pandas.DataFrame(squirrel_dict)

print(squirrel_df)

squirrel_color_csv = squirrel_df.to_csv("squirrel_color_data.csv")

