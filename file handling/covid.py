import csv
import pycountry_convert as pc

def country_to_continent(country_name):
    
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Example
# country_name = 'Australia'
# print(country_to_continent(country_name))


with open('file handling/covid_worldwide.csv', 'r', encoding='UTF-8') as file:
    data = csv.DictReader(file, delimiter=',')

    highest_deaths = 0
    highest_deaths_country = ''

    number_of_tests = 0

    confirmed_cases = 0

    continents = {
        'Asia' : 0,
        'Africa' : 0,
        'Europe' : 0,
        'North America' : 0,
        'South America' : 0,
        'Oceania' : 0
    }

    cfr = {}

    for row in data:
        if row['Total Deaths'] != '':
            deaths = int(row['Total Deaths'].replace(',', ''))
            if deaths > highest_deaths:
                highest_deaths = deaths
                highest_deaths_country = row['Country']
        
        if row['Total Test'] != '':
            number_of_tests += int(row['Total Test'].replace(',', ''))

        if row['Total Cases'] != '':
            total_cases = int(row['Total Cases'].replace(',', ''))              
            
            confirmed_cases += total_cases

            cfr[row['Country']] = round(deaths / total_cases  * 100, 2)
        
        try:
            continent = country_to_continent(row['Country'].lstrip())
            continents[continent] += int(row['Total Test'].replace(',', ''))
        except:
            continue

    print(continents)

with open('file handling/covid_ans.txt', 'w') as file:
    
    # answer 1
    file.write(f'1.\nHighest number of deaths: {highest_deaths_country}\n')
    
    # answer 2
    file.write(f'2.\nCumulative number of tests: {number_of_tests}\n')
    
    # answer 3
    file.write(f'3.\n')
    for continent in continents:
        file.write(f'{continent} : {continents[continent]}\n')

    # answer 4
    file.write(f'4.\nCumulative number of confirmed cases: {confirmed_cases}\n')
    
    # answer 5
    file.write(f'5.\n')
    for row in cfr:
        file.write(f'{row} : {cfr.get(row)}%\n')

    # answer 6
    ans_6 = sorted(cfr.items(), key=lambda x:x[1])
    file.write(f'6.\n')
    for row in ans_6:
        file.write(f'{row[0]} : {row[1]}%\n')