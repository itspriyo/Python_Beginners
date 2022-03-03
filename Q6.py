import pandas as pd
data = {"Name" :["Toshi","Bhawana","Samridhi"],
        "Age":[16,17,18],
        "Weight":[45,50,48]}
df = pd.DataFrame(data,index=['Row_1',"Row_2","Row_3"])
print(df)
df.drop('Row_1',inplace=True)
print("Updated data frame is ")
print(df)