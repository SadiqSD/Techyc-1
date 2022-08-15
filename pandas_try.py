import pandas as pd

# data_1 = ["Sadiq","Murtala","Ibrahim","Musa","Khalid","Ahamad","Muhammad","Khadija","Garba","Yusuf"]
# data_2 = [18,47,13,16,24,33,24,27,22,19]
# c_data = { "Name" : data_1, "Age": data_2}
#
# Pandas = pd.DataFrame(c_data, index=[1,2,3,4,5,6,7,8,9,10])
# csv = Pandas.to_csv("csv_file.csv")
# print(Pandas)
# print(csv)
# read = pd.read_csv("csv_file.csv")
# print(read.to_string())

# def fold():
#     times = 3
#     name = input("what is your name? ")
#     while name != "":
#         times += 1
#         print("Name recorded")
#     else:
#         print("Entry empty")
#
####### OOP


# do one mission at a time soldier
# name = ["Sadiq","Murtala","Isa", "Aminu","Muhammad"]
# age =  [18,47,18,58,19]
# surname = ["Murtala","Muhammad","Aminu","Musa","Abdullahi"]
# data = {"Name" : name,"Surname":surname , "Age" : age}
#
# df = pd.DataFrame(data, index=[1,2,3,4,5])
# print(df)

import sqlite3

connect = sqlite3.connect("Citizen.db")