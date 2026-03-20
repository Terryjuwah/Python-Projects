name = input('Enter your Full Name: ')
age = input('Enter your Age: ')
city = input('Enter your city: ')
hubby = input('Enter your Favourite Hubby: ')
job = input('Enter your Dream Job: ')

print('=' * 30)
print(' ' * 6 + 'PERSONAL INFO CARD' + ' ' * 6)
print('=' * 30) 
print('Name: ' + name)
print('Age: ' + age)
print('City: ' + city) 
print('Favourite Hubby: ' + hubby )  
print('Dream Job: ' + job)


print(' ' * 30)
print(' ' * 30)

print('=' * 30)
print(' ' * 11 + 'FUN FACT' + ' ' * 11)
print('=' * 30)

print('Name Length: '+ str(len(name)))
print('Age Length: '+ str(len(age)))
print('City Length: ' + str(len(city)))
print('Hubby length: ' + str(len(hubby)))
print('Job length: ' + str(len(job)))
ageD = int(age) * 2
print('Age Doubled: ' + str(ageD))
print('Your Hubby is: ' +  hubby * 3)
