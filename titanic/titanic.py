import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_df=pd.read_csv("titanictrain.csv")
titanic_df["Survived"]=titanic_df["Survived"].map({0:"died",1:"survived"})
print (titanic_df.head(5))
titanic_df.drop(["Name","Fare","Ticket","Parch"],axis=1,inplace=True)
titanic_df["Embarked"]=titanic_df["Embarked"].fillna("S")

titanic_df["Pclass"]=titanic_df["Pclass"].map({1:"luxury class",2:"economy class",3:"low class"})
print (titanic_df.head(5))

ax=sns.countplot(x='Pclass',palette='Set1',hue="Survived",data=titanic_df)
ax.set(title="survival rate based on p class",xlabel="class",ylabel="count ")
plt.show()
print(pd.crosstab(titanic_df["Sex"],titanic_df["Survived"]))
ax=sns.countplot(x='Sex',palette='Set2',hue="Survived",data=titanic_df)
plt.show()
#age group create intervals of ages

interval=(0,18,35,60,120)
categ=["child","teens","adults","old"]
titanic_df["age_cat"]=pd.cut(titanic_df["Age"],interval,labels=categ)
ax=sns.countplot(x="age_cat",hue="Survived",data=titanic_df)
plt.show()
print("start")
titanic_df.describe()







