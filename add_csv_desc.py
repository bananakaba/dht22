import csv

add = ["time", "humidity", "temperature"]

print("Dieses Programm fügt die Beschriftung der CSV durch.")

filename = input("Datum der CSV eingeben 'dd_mm_yy': ")
#with open("dht22/data.csv", "r") as infile:
with open(f"csv/dht22_{filename}.csv", "r") as infile:
    reader = list(csv.reader(infile))
    if reader[0] != add:
        reader.insert(0, add)

#with open("dht22/data.csv", "w", newline="") as outfile:
with open(f"csv/dht22_{filename}.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    for line in reader:
        writer.writerow(line)