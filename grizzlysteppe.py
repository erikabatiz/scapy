# Name: Erika Batiz
# Date: October 27, 2017
# Scapy lab  |  grizzlysteppe.py

import csv
from collections import Counter

ips = []

with open ('JAR-16-20296A.csv', 'rb') as f:
    reader = csv.reader(f)
    included_cols = [0, 7]
    for row in reader:
        if (row[1] == "IPV4ADDR"):
            content = list(row[i] for i in included_cols)
            ips.append(content)

for row in ips:
    temp = row[0].replace("[", "")
    row[0] = temp.replace("]", "")
    if "recommended" not in row[1]:
        temp2 = row[1].replace("This IP address is located in ", "")
        temp2 = temp2.replace("the ", "")
        row[1] = temp2.replace(".", "")
    else: 
        row[1] = "Undetermined"

print([item[0] for item in ips])

list1 = [item[1] for item in ips]
counts = Counter(list1)
print("Locations of the IPV4 Addresses:", counts)


