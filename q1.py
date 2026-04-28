#q1
%pip install seaborn
import numpy as np
 import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data={"student_id":[10,np.nan,20,103,24,59,7,217,88],
      "student_name":["sanvi","anuj","sakshi","arun","tarun","tanya","dhoni","virat","sanvi"],
      "age":[18,20,np.nan,20,18,19,21,20,18],
      "height(cm)":[160,160,162,np.nan,168,170,170,180,200],
      "weight(kg)":[35,70,50,np.nan,80,75,60,52,1],
      "semester":[1,1,2,3,2,4,6,2,7],
      "gender":["F",np.nan,"F","M","M","F","M","M","F"],
      "city":["dehradun","ranchi","patna","banaras","mumbai","delhi","amritsar","kolkata","dehradun"]}
df=pd.DataFrame(data)
print(df)
# i. Shape of dataset
print("Shape of dataset:", df.shape)
# ii. Column names
print("Column names:", df.columns)
# iii. Null values count
print("Null values:\n", df.isnull().sum())
# iv. Unique names
print("Unique student names:", df["student_name"].unique())
# v. Line Graphs
plt.figure()
plt.plot(df["height(cm)"], df["weight(kg)"], marker='o')
plt.xlabel("height(cm)")
plt.ylabel("weight(kg)")
plt.title("height(cm) vs weight(kg)")
plt.show()
plt.figure()
plt.plot(df["height(cm)"], df["age"], marker='o')
plt.xlabel("height(cm)")
plt.ylabel("age")
plt.title("height(cm) vs age")
plt.show()
plt.figure()
plt.plot(df["weight(kg)"], df["age"], marker='o')
plt.xlabel("weight(kg)")
plt.ylabel("age")
plt.title("weight(kg) vs age")
plt.show()
# vi. Scatterplot (Height Outliers)
plt.figure()
plt.scatter(range(len(df)), df["height(cm)"])
plt.title("Scatter Plot for Height")
plt.xlabel("Index")
plt.ylabel("height(cm)")
plt.show()
# vii. Boxplot (Outliers in all columns)
plt.figure()
sns.boxplot(data=df.select_dtypes(include=np.number))
plt.title("Boxplot for all numerical columns")
plt.show()
# viii. Remove Outliers (Height - IQR Method)
Q1 = df["height(cm)"].quantile(0.25)
Q3 = df["height(cm)"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_no_height_outliers = df[(df["height(cm)"] >= lower_bound) & (df["height(cm)"] <= upper_bound)]

print("Dataset after removing height outliers (IQR):\n", df_no_height_outliers)

df["weight(kg)"] = df["weight(kg)"].fillna(df["weight(kg)"].mean())

# Step 2: Calculate Z-score
std_w = df["weight(kg)"].std()
z_scores = (df["weight(kg)"] - mean_w) / std_w

# Step 3: Remove Outliers
df = df[np.abs(z_scores) < 3].reset_index(drop=True)
print(df)
