from random import random
from turtle import title
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import median
import random
df=pd.read_csv(r"C:\Big data project material\Car_sales2.csv")
df.shape
df.head(10)
df=df.drop(['EngineV'], axis = 1)
df.head()
df.isnull().sum()
df=df.fillna(df['Price'].mean(skipna=True))
df[df['Mileage']==0] 
df['Mileage']=df['Mileage'].mask(df.Mileage==0,df['Mileage'].mean(skipna=True))

df.duplicated().sum()
df.drop_duplicates(keep='first',inplace=True)

df = df[df['Mileage']>100] 
df = df[df['Mileage']<400]


dfa=df.Brand.value_counts()
dfa
d=set(df["Brand"])
a=df.groupby('Brand').size()
explode=[]
colors=[]
list1=[0.1,0.2,0.3]
list2=["r","g","c","m","y","b"]
for i in range (0,len(d)):
    explode.append(random.choice(list1))

for i in range(0,len(d)):
    colors.append(random.choice(list2))

plt.pie(x=a,labels=d, data=df, autopct="%.2f %%",explode=explode,colors=colors)
plt.show()
fig, ax = plt.subplots(figsize = (12,6))


ind = np.arange(len(dfa))
bars1 = ax.bar(dfa.index, dfa, 
        color=colors,
        label=dfa.index)
ax.set_title("Number of car models realsed till 2016 per brand")
ax.set_ylabel('Number of car models realsed till 2016')


ax.set_xticklabels(dfa.index, rotation=70)
ax.set_xlabel("Car Brands")
plt.show()

sns.distplot(df['Price']).set(title="Price variations")
plt.show()


df.sort_values('Year')

Year1= df['Year'].unique()
Year1.sort()
len(Year1)

median_per_year = []
for i in Year1:
    df0 = df[df['Year']==i]
    a = median(df0['Price'])
    median_per_year.append(a)

len(median_per_year)

sns.lineplot(Year1,median_per_year)
plt.title("Prefered Price range per year")
plt.show()

sns.lineplot(df['Year'],df['Price'])
plt.title("Price range per year")
plt.show()

len(df['Model'].unique())

sns.lineplot(df['Year'],df['Mileage'])
plt.title("Mileage trends since 1970s till 2016")
plt.show()

dfz= df[df['Year']==2016]
dfz['Mileage'].mean()

dfy= df[df['Year']==1990]
dfy['Mileage'].mean()

New_models_per_year = []
New_models_per_model_per_year = []
for i in Year1:
    df1= df[df['Year']==i].groupby("Brand").count()
    
    New_models_per_model_per_year.append(df1)

print(New_models_per_model_per_year)

df1 = df[df['Year']<2000].groupby("Brand")['Year'].count()
df2 = df[df['Year']>=2000].groupby("Brand")['Year'].count()

df1
df2

fig, ax = plt.subplots(figsize = (12,6))


ind = np.arange(len(df1))
carmodels2002before= ax.bar(df1.index, df1, 
        color=colors,
        label=df1.index)
ax.set_title("Number of car models realsed before 2002 per brand")
ax.set_ylabel('Number of car models realsed before 2002')


ax.set_xticklabels(df1.index, rotation=70)
ax.set_xlabel("Car Brands")

fig, ax = plt.subplots(figsize = (12,6))

ind = np.arange(len(df2))
carmodels2002after = ax.bar(df2.index, df2, color=colors,label=df2.index)
ax.set_title("Number of car models realsed after 2002 per brand")
ax.set_ylabel('Number of car models realsed after 2002')


ax.set_xticklabels(df1.index, rotation=70)
ax.set_xlabel("Car Brands")


df1= df[df['Year']==2016]
df2=df1.groupby("Brand")['Price'].mean()
df2




fig, ax = plt.subplots(figsize = (12,6))


ind = np.arange(len(df2))
carprice2016 = ax.bar(df2.index, df2, 
       color=colors, 
        label=df2.index)
ax.set_title("Number of car models ")
ax.set_ylabel('Number of car models')


ax.set_xticklabels(df2.index, rotation=70)
ax.set_xlabel("Car Brands")
plt.title("Avegarge car price per brand in 2016")
plt.show()


df4=df[['Brand','Body']]
df4=df4.groupby('Body')['Brand'].count()
print(df4)


fig, ax = plt.subplots(figsize = (12,6))
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = 	'#696969'
plt.rcParams['axes.labelcolor']= 	'#696969'
plt.rcParams['xtick.color'] = '#696969'
plt.rcParams['ytick.color'] = '#696969'
plt.rcParams['font.size']=12

ind = np.arange(len(df4))

bars1 = ax.bar(df4.index, df4, 
        color=colors,
        label=df4.index)
ax.set_title("Number of car models ")
ax.set_ylabel('Number of car models')


ax.set_xticklabels(df4.index, rotation=70)
ax.set_xlabel("Body type of car")
plt.title("Number of car body types since 1970s") 
plt.show()

sns.scatterplot(x = dfz , y = 'Price', size = 'Mileage' ,  hue= 'Mileage' , data = df).set(title = 'How price effecting the mileage')

plt.show()
X = df4.index
Diesel=[]
Petrol=[]
for i in X:
    dfx=df[df['Body']==i]
    a=dfx.groupby('Engine Type')['Body'].count()
    Diesel.append(a['Diesel'])
    Petrol.append(a['Petrol'])



X_axis = np.arange(len(X))
plt.xticks(X_axis, X)
plt.bar(X_axis - 0.2,Diesel, 0.4, label = 'Diesel')
plt.bar(X_axis + 0.2,Petrol, 0.4, label = 'Petrol')
plt.xlabel("Body type of car")
plt.ylabel("#count")
plt.title("Car engine type distribution")
plt.legend()
plt.show()


ratio1 = df['Price']/df['Mileage']
df['Price/Mileage'] =ratio1
sns.distplot(ratio1)
plt.show()
DP1970= df.groupby('Engine Type')['Price'].count()
plt.bar(DP1970.index,DP1970)
plt.title("Number of car types produced since 1970")
plt.show()
DP2016 = df0.groupby('Engine Type')['Price'].count()
plt.bar(DP2016.index,DP2016)
plt.title("Number of car types produced in 2016")
plt.show()
