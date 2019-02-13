
import pandas
data = pandas.read_csv('dataset_Facebook.csv',sep=';')

print ('среднее число Page total likes ',data['Page total likes'].mean()) 
print ('среднее число Page total likes для Type=Photo ',(data[data['Type']=='Photo'])['Page total likes'].mean())
print ('среднее число Page total likes для Type=Status ',(data[data['Type']=='Status'])['Page total likes'].mean())
print ('среднее число Page total likes для Type=Link ',(data[data['Type']=='Link'])['Page total likes'].mean())
print ('среднее число Page total likes для Type=Video ',(data[data['Type']=='Video'])['Page total likes'].mean())

print ('максимальное число Page total likes ',data['Page total likes'].max()) 
print ('максимальное число Page total likes для Type=Photo ',(data[data['Type']=='Photo'])['Page total likes'].max())
print ('максимальное число Page total likes для Type=Status ',(data[data['Type']=='Status'])['Page total likes'].max())
print ('максимальное число Page total likes для Type=Link ',(data[data['Type']=='Link'])['Page total likes'].max())
print ('максимальное число Page total likes для Type=Video ',(data[data['Type']=='Video'])['Page total likes'].max())

print ('минимальное число Page total likes ',data['Page total likes'].min()) 
print ('минимальное число Page total likes для Type=Photo ',(data[data['Type']=='Photo'])['Page total likes'].min())
print ('минимальное число Page total likes для Type=Status ',(data[data['Type']=='Status'])['Page total likes'].min())
print ('минимальное число Page total likes для Type=Link ',(data[data['Type']=='Link'])['Page total likes'].min())
print ('минимальное число Page total likes для Type=Video ',(data[data['Type']=='Video'])['Page total likes'].min())

print ('медиана Page total likes ',data['Page total likes'].median()) 
print ('медиана Page total likes для Type=Photo ',(data[data['Type']=='Photo'])['Page total likes'].median())
print ('медиана Page total likes для Type=Status ',(data[data['Type']=='Status'])['Page total likes'].median())
print ('медиана Page total likes для Type=Link ',(data[data['Type']=='Link'])['Page total likes'].median())
print ('медиана Page total likes для Type=Video ',(data[data['Type']=='Video'])['Page total likes'].median())

print ('мода Page total likes ',data['Page total likes'].moda()) 
print ('мода Page total likes для Type=Photo ',(data[data['Type']=='Photo'])['Page total likes'].moda())
print ('мода Page total likes для Type=Status ',(data[data['Type']=='Status'])['Page total likes'].moda())
print ('мода Page total likes для Type=Link ',(data[data['Type']=='Link'])['Page total likes'].moda())
print ('мода Page total likes для Type=Video ',(data[data['Type']=='Video'])['Page total likes'].moda())