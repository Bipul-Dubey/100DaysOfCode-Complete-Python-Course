import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color=(data["Primary Fur Color"])
gray=0
Cinnamon=0
black=0
for color in fur_color:
    if color=='Gray':
        gray+=1
    if color=='Cinnamon':
        Cinnamon+=1
    if color=='Black':
        black+=1
print(black,gray,Cinnamon)
data_dict={
    "Fur color":["black","red","gray"],
    "score":[black,Cinnamon,gray]
    }
datas=pandas.DataFrame(data_dict)
datas.to_csv("new_squirel_data.csv")

# course solution to count fur color squirrel
# grey_squirrel_count=len(data[data["Primary Fur Color"]=='Gray'])
# red_squirrel_count=len(data[data["Primary Fur Color"]=='Cinnamon'])
# black_squirrel_count=len(data[data["Primary Fur Color"]=='Black'])
# print(grey_squirrel_count,red_squirrel_count,black_squirrel_count)
