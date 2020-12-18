import csv
import re


def import_csv_data_to_list_of_dicts(csvfile):
	list_of_dicts_of_csv_data = []
	with open(csvfile, 'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			list_of_dicts_of_csv_data.append(row)
	return list_of_dicts_of_csv_data


def calculate_yearly_commute_in_km(list_of_dictionaries_data):
	for item in list_of_dictionaries_data:
		if item['Description'] == 'Distance between Oxford and London':
			commute_distance = float(re.sub(r'[a-z]+', '', item['Value'], re.I))
		if item['Description'] == 'Number of working days per week':
			work_days_per_week = float(re.sub(r'[a-z]+', '', item['Value'], re.I))
		if item['Description'] == 'Number of weeks in a year':
			work_weeks_per_year = float(re.sub(r'[a-z]+', '', item['Value'], re.I))
		if item['Description'] == 'Number of km in 1 mile':
			km_in_one_mi = float(re.sub(r'[a-z]+', '', item['Value'], re.I))
		if item['Description'] == 'Distance between planet Earth and the Moon':
			distance_from_earth_to_moon = float(re.sub(r'[a-z]+', '', item['Value'], re.I).replace(',',''))
	yearly_commute_distance_mi = (commute_distance*2)*work_days_per_week*work_weeks_per_year
	yearly_commute_distance_km = yearly_commute_distance_mi*km_in_one_mi
	years_to_the_moon = distance_from_earth_to_moon/yearly_commute_distance_km
	return years_to_the_moon


csv_data = import_csv_data_to_list_of_dicts('puzzle-data.csv')
final_answer = calculate_yearly_commute_in_km(csv_data)
print(final_answer)
