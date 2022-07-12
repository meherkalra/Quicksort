# Author: Meher Kalra
# Date: 21 Feb 2022
# Purpose: Lab-3

from cs1lib import *

# Purpose: to write a function to mark circles for cities on the map
def mark(city):
    disable_stroke()
    set_fill_color(0.8, 0.3, 0.9)
    latitude = 180 - 2*city[0]
    longitude = 360 + 2*city[1]
    draw_circle(longitude, latitude, 3)

input = open("cities_population.txt", "r")
list_cities = []
count = 0

for line in input:
    count = count + 1
    line.strip()
    line = line.split(",")
    list_cities.append([float(line[2]), float(line[3])])
    if count == 50:
        break

input.close()
j = 0

# Purpose: to write a main draw function to add the circles to the image
def main_draw():
    global j
    img = load_image("world.png")
    draw_image(img, 0, 0)

    for i in range(j, len(list_cities)):
        for k in range(0, j):
            mark(list_cities[k])
        j = j + 1
        break

    if j == 50:
        for l in list_cities:
            mark(l)

start_graphics(main_draw, width=720, height=360, framerate=4)


