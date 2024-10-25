import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
titanic = sns.load_dataset('titanic')

# Display the first 5 rows of the data
print('First 5 rows of the dataset: ')

print(titanic.head())

# Display general information about the number of rows and columns
print('Information about the dataset: ')
print(titanic.info())

#describe the dataset
print('\n Description of the dataset: ')
print(titanic.describe())

#Description of the categorical data
print('\n Description of the categorical data: ')
print(titanic.describe(include=['object']))

#count null values
print('\n Count of null values: ')
print(titanic.isnull().sum())

#Histogram of the age column
plt.figure
sns.histplot(titanic['age'], bins=30, kde=True)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

#bar plot of the survived by class column
plt.figure(figsize=(6, 6))
sns.countplot(x='class',hue='survived',data=titanic)
plt.title('Survived by Class')
plt.xlabel('Class')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])
plt.show()

#heatmap of the correlation between the number variables
plt.figure(figsize=(10, 8))
sns.heatmap(titanic.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()