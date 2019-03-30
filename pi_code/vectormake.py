import csv
from datetime import datetime

time = []
magX = []
magY = []
magZ = []

with open("ThinSat_MagField_Vector.csv", 'r') as csvfile:
	magreader = csv.reader(csvfile)
	next(magreader)
	prevrow = next(magreader)
	for row in magreader:
		# print(prevrow)
		time.append(datetime.fromisoformat(prevrow[0]))
		magX.append(float(prevrow[1]))
		magY.append(float(prevrow[2]))
		magZ.append(float(prevrow[3]))
		prevrow = row