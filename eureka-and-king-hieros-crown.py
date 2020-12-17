# https://www.101computing.net/eureka-and-king-hieros-crown/
import re


def calculate_density(mass, volume):
    object_density = mass/volume
    return object_density


while True:
    try:
        mass = input('Please enter the mass of the metal in kilograms (exclude units)\n')
        mass = float(re.sub(r'[a-z]+', '', mass, re.I))
        if mass != '':
            break
        print('Invalid entry. Please enter a number only with no units\n')
    except Exception as e:
        print(e)
while True:
    try:
        volume = input('Please enter the volume of the metal in m3 (exclude units)\n')
        volume = float(re.sub(r'[a-z]+', '', mass, re.I))
        if volume != '':
            break
        print('Invalid entry. Please enter a number only with no units\n')
    except Exception as e:
        print(e)

density = calculate_density(mass, volume)
print(density)
