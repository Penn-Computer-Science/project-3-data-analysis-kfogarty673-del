import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

names = [
    "Elijah Foster",
    "Kyle Marsh",
    "Kyan Fogarty",
    "Spongebob Squarepants",
    "Tuff dude",
    "Flight Reacts",
    "Gumball Waterson",
    "Jian Jumao-as",
    "Alexis Luebke",
    "Logan Wood",
    "Mya Dickson",
    "Dayvon Daquan Bennett",
    "Roman Williams",
    "Liam Neeson",
    "Noah Centineo",
    "Olivia Rodrigo",
    "Emma Chamberlain",
    "Ariana Grande",
    "Taylor Swift",
    "Josh Allen",
    "Dak Prescott"
]


sports_scale = [
    7,
    8,
    7,
    1,
    3,
    7,
    7,
    1,
    1,
    1,
    6,
    10,
    8,
    9,
    1,
    1,
    1,
    1,
    1,
    10,
    1
]

sports_played = [
    "No",
    "No",
    "No",
    "No",
    "No",
    "No",
    "No",
    "No",
    "Yes",
    "No",
    "No",
    "Yes",
    "Yes",
    "Yes",
    "No",
    "No",
    "No",
    "No",
    "No",
    "Yes",
    "No"
]

school_scale = [
    9,
    9,
    8,
    8,
    8,
    7,
    7,
    7,
    6,
    5,
    5,
    1,
    8,
    4,
    4,
    3,
    2,
    2,
    2,
    1,
    1,
]

GPA = [
    4.1389,
    3.76,
    4.075,
    4.1,
    3.8,
    4,
    4,
    3.6,
    3.4,
    4.2,
    0.01,
    3.8,
    0.162,
    3.67,
    3.5,
    4.0,
    3.9,
    3.8,
    3.9,
    3.6,
    2.0
]

favorite_number = [
    3.14,
    68,
    67,
    67,
    5,
    32,
    7,
    67,
    6,
    67,
    512,
    64,
    42,
    21,
    73,
    13,
    7,
    67,
    22,
    19,
    4
]

data = {
    "Names": names,
    "Sports watched 1-10": sports_scale,
    "School sport played": sports_played,
    "School enjoyment 1-10": school_scale,
    "GPA": GPA,
    "Favorite number": favorite_number
}

survey_data = pd.DataFrame(data)
survey_data.to_csv("survey_data.csv", index=False)
df = pd.read_csv("survey_data.csv")

sports_to_GPA = round(df.groupby("School sport played")["GPA"].mean(), 2)

print(df.describe())

print(sports_to_GPA)

print("-_"*20)
print("Top 3 Students By Gpa") #top 3 students
print(survey_data.sort_values(by='GPA', ascending = False).head(3))

plt.bar(df["School sport played"], df["GPA"])
plt.xlabel("Sports Played")
plt.ylabel("GPA")
plt.show()

plt.hist(df["GPA"], bins=40, edgecolor='black')
plt.xlabel('GPA')
plt.ylabel('Frequency')
plt.show()

plt.scatter(df["Favorite number"], df["GPA"], color='blue')
plt.xlabel('Favorite Number')
plt.ylabel('GPA')
plt.show()