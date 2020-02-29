import pylab
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
data_train = pd.read_csv("./data_merged.csv",delimiter=',')


# Plot Cab type distribution
pylab.rcParams['figure.figsize'] = (8.0, 8.0)
type_distribution = data_train["cab_type"].value_counts()
plt.pie(type_distribution,radius=None,labels=["Uber", "Lyft"],colors=["#ffc0cb","#26d3f6"],explode = (0.05,0.1),
        labeldistance = 1.1,autopct = '%1.1f%%',shadow = True,startangle = 90,pctdistance = 0.6)
plt.title('Cab type distribution')
plt.show()

# Plot Cab name distribution
pylab.rcParams['figure.figsize'] = (15.0, 8.0)
name_distribution = data_train["name"].value_counts()
sns.barplot(name_distribution.index, name_distribution.values/1000,color="g")
plt.ylabel('Nums of routes in thousands')
plt.xlabel("Cab_name")
plt.title('Cab name distribution')
plt.show()

# Plot Distance distribution
distance_distribution = data_train["distance"]
dist_range=list(range(0,9,1))
distance_distribution=pd.cut(distance_distribution,dist_range,right=True)
distance_distribution = distance_distribution.value_counts()
sns.barplot(distance_distribution.index, distance_distribution.values/1000,color="g")
plt.ylabel('Nums of routes in thousands')
plt.xlabel("Distance")
plt.title('Distance distribution')
plt.show()

# Plot Weekday distribution
weekday_distribution = data_train["weekday"].value_counts()
order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sns.barplot(order, weekday_distribution.values/1000,color="g")
plt.ylabel('Nums of routes in thousands')
plt.xlabel("Weekday")
plt.title('Weekday distribution')
plt.show()

# Plot price distribution
price_distribution = data_train["price"]
price_range=list(range(0,70,5))
price_distribution=pd.cut(price_distribution,price_range,right=True)
price_distribution = price_distribution.value_counts()
sns.barplot(price_distribution.index, price_distribution.values/1000,color="g")
plt.ylabel('Nums of routes in thousands')
plt.xlabel("Price")
plt.title('Price distribution')
plt.show()

# Plot surge_multiplier vs distance
sns.scatterplot(x=data_train["distance"],y=data_train["surge_multiplier"],data=data_train,hue=data_train["cab_type"])
plt.title('surge_multiplier vs distance')
