import csv
import pandas as pd
import plotly.express as px

add = ["time", "humidity", "temperature"]                                   # Beschriftung

print("CSV bitte in dht22 abspeichern.")
filename = input("Datum der CSV eingeben 'dd_mm_yy': ")


with open(f"dht22/dht22_{filename}.csv", "r") as infile:                    # Beschriftung hinzufügen falls nicht vorhanden
    reader = list(csv.reader(infile))
    if reader[0] != add:
        reader.insert(0, add)

with open(f"dht22/dht22_{filename}.csv", "w", newline="") as outfile:       # Veränderungen abspeichern
    writer = csv.writer(outfile)
    for line in reader:
        writer.writerow(line)


df = pd.read_csv(f"dht22/dht22_{filename}.csv")
#print(df.head())

fig1 = px.line(df, x = "time", y = "temperature", title="Temperature")
fig1.show()

fig2 = px.line(df, x = "time", y = "humidity", title="Humidity")
fig2.show()