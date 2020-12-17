# https://www.101computing.net/eureka-and-king-hieros-crown/
import re
import csv


def calculate_density(mass, volume):
    # calculates the density of an unknown metal given mass and volume
    object_density = mass/volume
    return object_density


def import_density_values_csv(csv_file):
    # reads a csv into a python list of dictionaries. manipulating 'density_range' to facilitate our solution
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        accepted_density_values_list = []
        for row in reader:
            row['density_range'] = row['density_range'].replace('-',',').split(',')
            accepted_density_values_list.append(row)
    return accepted_density_values_list


def take_density_calc_and_search_for_metals(density, accepted_density_values_list):
    # searches within the list of dicts to find the metal which matches the density
    for dict in accepted_density_values_list:
        #print(dict['density_range'][0])
        #print(dict['density_range'][1])
        if density > float(dict['density_range'][0]) and density < float(dict['density_range'][1]):
            return dict['metal']


while True:
    try:
        mass = input('Please enter the mass of the metal in kilograms (exclude units)\n')
        mass = float(re.sub(r'[a-z]+', '', mass, re.I)) # regex to remove any letters a user puts in incorrectly
        if mass != '':
            break
        print('Invalid entry. Please enter a number only with no units\n')
    except Exception as e:
        print(e)
while True:
    try:
        volume = input('Please enter the volume of the metal in m3 (exclude units)\n')
        volume = float(re.sub(r'[a-z]+', '', volume, re.I)) # regex to remove any letters a user puts in incorrectly
        if volume != '':
            break
        print('Invalid entry. Please enter a number only with no units\n')
    except Exception as e:
        print(e)

density = calculate_density(mass, volume)
density_list_from_csv = import_density_values_csv('metal-density.csv')
final_metal = take_density_calc_and_search_for_metals(density, density_list_from_csv)
print(final_metal)
