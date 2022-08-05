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
# fold()


def fold(times, limit):
    while times < limit:
        name = input("What is your name? ")
        if name == "":
            print("Entry is empty ")
            times += 1
            if times == limit:
                print("sorry you have to refresh the page")
            else:
                continue
        else:
            print("Name recorded")
            break
fold(0,3)



