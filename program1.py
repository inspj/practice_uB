import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv')
data = data.dropna(subset = ['Age'])


#Calculating the average age of all people present on the boat
avg_age = round(sum(data['Age']/data['Age'].count()), 2)
print(avg_age)


#Calculating correlation between the Age of people and Death
print("Correlation between age and death is: ", data['Age'].corr(data['Survived']))

#plt.hist(data['Age'])
#plt.show()
