# Author: Meher Kalra
# Date: 21 Feb 2022
# Purpose: Lab-3 checkpoint

# to define a City class that gives information about a world city
class City:
    # Method1: the init method that takes in instance variables country_code, name, region, population, latitude, longitude
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude

    # Method2: str method returns a string of name, population, latitude and longitude of the city
    def __str__(self):
        x = self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)
        return x

# defining empty list
cities_out = []
file1 = open('world_cities.txt', 'r')
Line = file1.readlines()
# for loop for appending the necessary information from the file to the empty list
for line in Line:
    line.strip()
    words = line.split(",")
    c1 = City(words[0], words[1], words[2], int(words[3]), float(words[4]), float(words[5]))
    cities_out.append(c1)

file2 = open('cities_out.txt', 'w')

for i in range(len(cities_out) - 1):
    file2.writelines(str(cities_out[i]))
    file2.writelines("\n")

file2.writelines(str(cities_out[len(cities_out) - 1]))
file2.close()
