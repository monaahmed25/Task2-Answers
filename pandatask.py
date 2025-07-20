import pandas as pd
data=[["Alice",20,"A",85],["Bob",22,"B",78],["Charlie",19,"A",92],["David",21,"C",65],["Eva",20,"B",74]]
students_data=pd.DataFrame(data, columns=["Name","Age","Grade","Marks"])
print(students_data.head(3))
print(students_data[["Name","Marks"]])
print(students_data.loc[students_data["Grade"]=="A"])

