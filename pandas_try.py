import pandas as pd

# data_1 = ["Sadiq","Murtala","Ibrahim","Musa","Khalid","Ahamad","Muhammad","Khadija","Garba","Yusuf"]
# data_2 = [18,47,13,16,24,33,24,27,22,19]
# c_data = { "Name" : data_1, "Age": data_2}
#
# Pandas = pd.DataFrame(c_data, index=[1,2,3,4,5,6,7,8,9,10])
# csv = Pandas.to_csv("csv_file.csv")
# print(Pandas)
# print(csv)
read = pd.read_csv("csv_file.csv")
print(read.to_string())





