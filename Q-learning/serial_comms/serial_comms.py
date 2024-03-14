import serial
import csv
import time

# Establish serial connection with the Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change '/dev/ttyACM0' to the appropriate port and 9600 to the baud rate used in your Arduino

# Open a CSV file to save the sensor data
csv_file = open('sensor_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp', 'Sensor1', 'Sensor2', 'Sensor3', 'Sensor4', 'Sensor5'])  # Header row

try:
    while True:
        # Read a line of data from the serial port
        line = ser.readline().decode().strip()
        # Split the line into timestamp and distance values for each sensor
        timestamp = time.time()  # Current timestamp
        distances = [float(val) for val in line.split(',')]  # Convert distance strings to floats
        # Write the data to the CSV file
        csv_writer.writerow([timestamp] + distances)
        # Print the data for verification (optional)
        print(f'Timestamp: {timestamp}, Distances: {distances}')	
        # Wait for a short duration to avoid overloading the serial buffer
        time.sleep(0.1)

except KeyboardInterrupt:
    # Close the serial connection and CSV file when the program is interrupted
    ser.close()
    csv_file.close()

