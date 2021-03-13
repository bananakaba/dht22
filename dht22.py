import serial
import time
import csv

ser = serial.Serial('/dev/ttyUSB0')
ser.reset_input_buffer()

while True:
	try:
		ser_bytes = ser.readline()
		decoded_Humidity = ser_bytes[0:5].decode("utf-8")
		decoded_Temperature = ser_bytes[5:10].decode("utf-8")
		print("Humidity: ", decoded_Humidity, "%")
		print("Temperature: ", decoded_Temperature, "°C")

		t = time.localtime()
		day = time.strftime("%d_%m_%y", t)
		current_time = time.strftime("%H:%M:%S Uhr UTC", t)
		csv_file = str(f"dht22_{day}.csv")
		with open(csv_file, "a") as f:
			writer = csv.writer(f,delimiter=",")
			writer.writerow([current_time,decoded_Humidity,decoded_Temperature])

	except:
		print("Keyboard Interrupt")
		break
