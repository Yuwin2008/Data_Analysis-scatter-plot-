import csv 
import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')
roll_no = input("Enter your roll no to check your performance: ")
student = df.loc[df["student_id"] == roll_no]
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")

fig.show()
