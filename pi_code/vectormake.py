import csv
from datetime import datetime


class HelmholtzCage:
	def __init__(self, magfield, L, d):
		self.magfield = magfield
		# set length of side of coil
		self.L = L
		# set distance between coils 
		self.d = d
		self.currentX = []
		self.currentY = []
		self.currentZ = []

		# CHANGE TO ACTUAL FORMULA LATER PLZ
		# DON'T FORGET THAT B IS IN mGAUSS
		getcurr = lambda B : B/30

		for mag in self.magfield.magX:
			self.currentX.append(getcurr(mag))

		for mag in self.magfield.magY:
			self.currentY.append(getcurr(mag))

		for mag in self.magfield.magZ:
			self.currentZ.append(getcurr(mag))


class MagField:
	def __init__(self, fname):
		self.time = []
		# magfield intensity is stored in mGauss!!!
		# therefore, the csv file is expected to be in mGauss as well!!
		self.magX = []
		self.magY = []
		self.magZ = []

		# populate the vectors with csv information
		with open(fname, 'r') as csvfile:
			magreader = csv.reader(csvfile)
			next(magreader)  # skip the first row
			prevrow = next(magreader)  # use this to skip the last row
			for row in magreader:
				dtitem = prevrow[0]  # YYYY-MM-DDTHH:MM:SS.ss
				self.time.append(
					datetime(
						int(dtitem[:4]),  # YYYY
						int(dtitem[5:7]),  # MM
						int(dtitem[8:10]),  # DD
						int(dtitem[11:13]),  # HH
						int(dtitem[14:16]),  # mm
						int(dtitem[17:19])  # ss
					)
				)
				self.magX.append(float(prevrow[1]))
				self.magY.append(float(prevrow[2]))
				self.magZ.append(float(prevrow[3]))
				prevrow = row
