# Author: Meher Kalra
# Date: 21 Feb 2022
# Purpose: Lab-3 - sorting information to produce output files

# comparing names, populations, and latitude; writing into new files
# that sort by those categories

from city import *
from quicksort import *

# Purpose: comparing cities to be sorted alphabetically
def compare_names(city1, city2):
    return city1.name.lower() <= city2.name.lower()

# Purpose: comparing cities in order of decreasing population
def compare_population(city1, city2):
    return city1.population >= city2.population

# Purpose: comparing cities to put in order of increasing latitudes
def compare_latitudes(city1, city2):
    return city1.latitude <= city2.latitude

# Comparing names, populations, and latitudes of world cities and sorting them into new files
file = open("world_cities.txt", "r")
new_list = []

for line in file:
    line = line.strip()
    line = line.split(",")
    new_list.append(City(line[0], line[1], line[2], int(line[3]), float(line[4]), float(line[5])))

file.close()

# Writing list in alphabetical order
sort(new_list, compare_names)
cities_alpha = open("cities_alpha.txt", "w")
for line in new_list:
    cities_alpha.write(str(line) + "\n")
cities_alpha.close()

# Writing list in decreasing order of population
sort(new_list, compare_population)
cities_population = open("cities_population.txt", "w")
for line in new_list:
    cities_population.write(str(line) + "\n")
cities_population.close()

# Writing list in latitudes from south to north
sort(new_list, compare_latitudes)
cities_latitude = open("cities_latitude.txt", "w")
for line in new_list:
    cities_latitude.write(str(line) + "\n")
cities_latitude.close()


