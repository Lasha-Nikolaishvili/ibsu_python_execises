import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# series = pd.Series([1, 2, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1], name="marks")
# marks_dataframe = pd.DataFrame(series)
# print(marks_dataframe.head(2))
# print(marks_dataframe['marks'].mode()[1])
# student_info = {"Name": ["Ana", "Mariam", "Salome", "Giorgi", "Revaz"],
#                 "Subject1": [72, 62, 94, 62, 76],
#                 "Subject2": [88, 90, 84, 64, 71],
#                 "Subject3": [71, 60, 67, 64, 69]}

# student_table = pd.DataFrame(student_info)
# print(student_table.head())
# student_table["average"] = (student_table["Subject1"] + student_table["Subject2"] + student_table["Subject3"]) / 3
# student_table.columns = ["First Name", "Python", "Calculus", "Statistics"]
# student_table.columns.values[0] = "firstname"
# student_table.drop(["average", "Name"], axis="columns", inplace=True)
# print(student_table.head())

# Create a DataFrame
# d = {
#     'Name': ['Alisa', 'Bobby', 'jodha', 'jack', 'raghu', 'Cathrine',
#              'Alisa', 'Bobby', 'kumar', 'Alisa', 'Alex', 'Cathrine'],
#     'Age': [26, 24, 23, 22, 23, 24, 26, 24, 22, 23, 24, 24],
#
#     'Score': [85, 63, 55, 74, 31, 77, 85, 63, 42, 62, 89, 77]}
# person = pd.DataFrame(d)
# person.drop_duplicates("Name",inplace=True)
# print(person.head(12))
# print(person.)

# students_info = {
#     "Name": ["Alex", "Mari", "Solomon", "Nick"],
#     "Calculus": [56, 78, 90, 91]
# }
# student_dataframe = pd.DataFrame(students_info)
# student_dataframe = student_dataframe.assign(Statistics=[90, 98, 45, 53])
# student_dataframe.insert(2, "Algebra", np.array([54, 23, 98, 78]))
# student_dataframe.loc[len(student_dataframe)] = ["Givi", 67, 98, 87]
# print(student_dataframe.head(8))

# student_info = {
#     "Name": ["Michael", "John", "David", "George", "Nick", "Bosho"],
#     "Python": [78, 77, 88, 77, 91, 56],
#     "Calculus": [98, 66, 77, 88, 87, 88],
#     "Statistics": [90, 56, 63, 66, 65, 45]
# }
# student_dataframe = pd.DataFrame(student_info)
# student_dataframe.set_index("Name", inplace=True)
# student_dataframe.sort_values(by=["Python", "Calculus"], ascending=[True, True], inplace=True)
# print(student_dataframe.head())
# print(student_dataframe.mean(axis=1))

d = {
    'Name': ['Alisa', 'Bobby', 'jodha', 'jack', 'raghu', 'Cathrine',
             'Alisa', 'Bobby', 'kumar', 'Alisa', 'Alex', 'Cathrine'],
    'Age': [26, 24, 23, 22, 23, 24, 26, 24, 22, 23, 24, 24],
    'Score': [85, 63, 55, 74, 31, 77, 85, 63, 42, 62, 89, 77]
}

df = pd.DataFrame(d)
# print(df.head())

# print(df.loc[0, :])
# print(df.loc[0, "Age"])
# print(df.loc[0:3, :])
# print(df.loc[0:3, ["Age", "Name"]])
# print(df.loc[df["Name"] == "Alisa"])
# print(df.loc[df["Score"] >= 75])
# print(df.iloc[0:5, [1, 2]])
# df.sort_values(by="Score", ascending=False, inplace=True)
# print(df.iloc[:1, :])
#
# df.sort_values(by="Score", ascending=True, inplace=True)
# print(df.iloc[:1, :])
# print(df.iloc[df["Score"].idxmax()])
# print(df.iloc[df["Score"].idxmin()])
print(df[(df["Score"]>60)&(df["Score"]<70)])
print(df[df["Age"]>10])