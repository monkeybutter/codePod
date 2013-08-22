import csv
import functions
import json
from datetime import timedelta, datetime
from os import listdir
from os.path import isfile, join


stations = []

element = {}
element['id'] = '015590'
element['longitude'] = 133.889
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Alice Springs Airport"

stations.append(element)

element = {}
element['id'] = '008051'
element['longitude'] = 114.6975
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Geraldton Airport"

stations.append(element)

element = {}
element['id'] = '076031'
element['longitude'] = 142.0867
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Mildura Airport"

stations.append(element)

element = {}
element['id'] = '026021'
element['longitude'] = 140.7739
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Mt Gambier"

stations.append(element)

element = {}
element['id'] = '039083'
element['longitude'] = 150.4775
element['closeDate'] = datetime(1988, 10, 1, 0, 0, 0)
element['name'] = "Rockhampton Airport"

stations.append(element)

element = {}
element['id'] = '072150'
element['longitude'] = 147.4575
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Wagga Wagga"

stations.append(element)

for station in stations:
	print station['name']
	sourceDNIPath = "/Users/SmartWombat/Dropbox/SolarData/DNI/DC02D_Data_" + station['id'] + ".txt"
	sourceGHIPath = "/Users/SmartWombat/Dropbox/SolarData/GHI/DC02D_Data_" + station['id'] + ".txt"
	sourceDiffusePath = "/Users/SmartWombat/Dropbox/SolarData/Diffuse/DC02D_Data_" + station['id'] + ".txt"
	destPath = "/Users/SmartWombat/Dropbox/SolarData/Phase0/DC02D_Data_" + station['id'] + ".csv"

	DNI = open(sourceDNIPath, 'rb') # opens the csv file
	GHI = open(sourceGHIPath, 'rb') # opens the csv file
	Diffuse = open(sourceDiffusePath, 'rb') # opens the csv file
	Dest = open(destPath, 'wb')

	#try:
	DNIReader = csv.reader(DNI)  # creates the reader object
	GHIReader = csv.reader(GHI)  # creates the reader object
	DiffReader = csv.reader(Diffuse)  # creates the reader object
	DestWriter = csv.writer(Dest)

	DestWriter.writerow(["ISODate UTC", "DNI solar exposure half-hourly", "DNI Uncertainty", "GHI solar exposure half-hourly", "GHI Uncertainty", "Diffuse solar exposure half-hourly", "Diffuse Uncertainty"])

	DNIlist = list(DNIReader)
	GHIlist = list(GHIReader)
	Difflist = list(DiffReader)

	DNI_i = 1
	GHI_i = 1
	Diff_i = 1

	while (DNI_i<len(DNIlist) or GHI_i<len(DNIlist) or Diff_i<len(DNIlist)):

		dates = []
		dates.append(datetime(int(DNIlist[DNI_i][2]), int(DNIlist[DNI_i][3]), int(DNIlist[DNI_i][4])))
		dates.append(datetime(int(GHIlist[GHI_i][2]), int(GHIlist[GHI_i][3]), int(GHIlist[GHI_i][4])))
		dates.append(datetime(int(Difflist[Diff_i][2]), int(Difflist[Diff_i][3]), int(Difflist[Diff_i][4])))

		oldest = min(dates)
		counterDate = oldest

		for i in range(48):

			row = []
			row.append(counterDate.strftime("%Y-%m-%dT%H:%M:%S"))

			if (dates[0] == oldest):

				if (DNIlist[DNI_i][(2*i)+5].strip() != ""):
					if (DNIlist[DNI_i][(2*i)+6].strip() != ""):
						#print "1.1"
						row.append(str(float(DNIlist[DNI_i][(2*i)+5].strip())))
						row.append(str(float(DNIlist[DNI_i][(2*i)+6].strip())))
					else:
						#print "1.2"
						row.append(str(float(DNIlist[DNI_i][(2*i)+5].strip())))
						row.append("NaN")
				else:
					if (DNIlist[DNI_i][(2*i)+6].strip() != ""):
						#print "1.3"
						row.append("NaN")
						row.append(str(float(DNIlist[DNI_i][(2*i)+6].strip())))
					else:
						#print "1.4"
						row.append("NaN")
						row.append("NaN")

			else:
				#print "No DNI"
				row.append("NaN")
				row.append("NaN")


			if (dates[1] == oldest):

				if (GHIlist[GHI_i][(2*i)+5].strip() != ""):

					if (GHIlist[GHI_i][(2*i)+6].strip() != ""):
						#print "2.1"
						row.append(str(float(GHIlist[GHI_i][(2*i)+5].strip())))
						row.append(str(float(GHIlist[GHI_i][(2*i)+6].strip())))
					else:
						#print "2.2"
						row.append(str(float(GHIlist[GHI_i][(2*i)+5].strip())))
						row.append("NaN")
				else:
					if (GHIlist[GHI_i][(2*i)+6].strip() != ""):
						#print "2.3"
						row.append("NaN")
						row.append(str(float(GHIlist[GHI_i][(2*i)+6].strip())))
					else:
						#print "2.4"
						row.append("NaN")
						row.append("NaN")

			else:
				#print "No GHI"
				row.append("NaN")
				row.append("NaN")


			if (dates[2] == oldest):

				if (Difflist[Diff_i][(2*i)+5].strip() != ""):
					if (Difflist[Diff_i][(2*i)+6].strip() != ""):
						#print "3.1"
						row.append(str(float(Difflist[Diff_i][(2*i)+5].strip())))
						row.append(str(float(Difflist[Diff_i][(2*i)+6].strip())))
					else:
						#print "3.2"
						row.append(str(float(Difflist[Diff_i][(2*i)+5].strip())))
						row.append("NaN")
				else:
					if (Difflist[Diff_i][(2*i)+6].strip() != ""):
						#print "3.3"
						row.append("NaN")
						row.append(str(float(Difflist[Diff_i][(2*i)+6].strip())))
					else:
						#print "3.4"
						row.append("NaN")
						row.append("NaN")

			else:
				#print "No Diff"
				row.append("NaN")
				row.append("NaN")

			counterDate = counterDate + timedelta(minutes=30)
			DestWriter.writerow(row)


		if (dates[0] == oldest):
			DNI_i =  DNI_i + 1

		if (dates[1] == oldest):
			GHI_i =  GHI_i + 1

		if (dates[2] == oldest):
			Diff_i =  Diff_i + 1


	#except:
		#print "This is an error message!"