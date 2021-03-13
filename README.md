# DHT22 - Raspberry PI and Arduino Nano

DHT22 is connected to Arduino Nano. Arduino is connected over USB with Raspberry Pi 3b+ running Raspberry Pi OS.

## Requirements

- Python (No Python2 supported)
- pyserial (pip3 install pyserial)
- pandas (pip3 install pandas)
- plotly (pip3 install pandas)

The rest should be included in python by default.

## Arduino Nano

### dht.ino

Standard DHT lib from Arduino IDE is used. It sends data to Serial with baud 9600.

## Raspberry Pi

### dht22.py

It's listening to the serial connection (in my case '/dev/ttyUSB0') and decoding incoming data.
It creates a csv for each day with the time, humidity and temperature for each measerument in it.

## csv_plot.py

Can run on any device using python. CSV file is needed. Adds the description for the csv in first row and plots them with plotly.
Plotted graphs are shown in Browser Tabs for humidity and temperature.

## add_csv_desc.py

Just for adding firt row to csv. Sample csv is included for testing. Use 01_01_01 as date.

## Future

Pythonscript for combining csv sheets for better controlling.
