import requests

# get readme.txt file
r = requests.get("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt")
readme = r.text


# get inventory and stations files
r = requests.get("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-inventory.txt")
inventory_txt = r.text
r = requests.get("https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt")
stations_txt = r.text

# save both the inventory and stations files to disk, in case we need them
with open("inventory.txt", "w") as inventory_file:
    inventory_file.write(inventory_txt)
with open("stations.txt", "w") as stations_file:
    stations_file.write(stations_txt)

# print(inventory_txt[:137])

# parse to named tuples

# use namedtuple to create a custom inventory class
from collections import namedtuple

Inventory = namedtuple(
    "Inventory", ["station", "latitude", "longitude", "element", "start", "end"]
)

# parse inventory lines and convert specific values to floats and ints

inventory = [
    Inventory(
        x[0:11],
        float(x[12:20]),
        float(x[21:30]),
        x[31:35],
        int(x[36:40]),
        int(x[41:45]),
    )
    for x in inventory_txt.split("\n")
    if x.startswith("US")
]

for line in inventory[:5]:
    print(line)
