import csv
import functions
import json, sys
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
	sourcePath = "/Users/SmartWombat/Dropbox/SolarData/Phase1/DC02D_Data_" + station['id'] + "_UTC.csv"
	destPath = "/Users/SmartWombat/Dropbox/SolarData/Phase2/DC02D_Data_" + station['id'] + "_UTC_Interp.csv"

	source = open(sourcePath, 'rb') # opens the csv file
	dest = open(destPath, 'wb') # opens the csv file for writing

	try:
		SourceReader = csv.reader(source)  # creates the reader object
		DestWriter = csv.writer(dest) # creates the writer object

		DestWriter.writerow(["ISODate UTC", "DNI solar exposure half-hourly", "DNI Uncertainty", "GHI solar exposure half-hourly", "GHI Uncertainty", "Diffuse solar exposure half-hourly", "Diffuse Uncertainty"])

		SourceList = list(SourceReader)

		i = 1

		while (i<(len(SourceList)-1)):

			dateA = datetime.strptime(SourceList[i][0], "%Y-%m-%dT%H:%M:%S")
			dateB = datetime.strptime(SourceList[i+1][0], "%Y-%m-%dT%H:%M:%S")

			if dateA.minute < 30:
				interDate = datetime(dateA.year, dateA.month, dateA.day, dateA.hour, 30, 00)

			else:
				interDate = datetime(dateB.year, dateB.month, dateB.day, dateB.hour, 00, 00)

			row = []
			row.append(interDate.strftime("%Y-%m-%dT%H:%M:%S"))

			lapseA = (interDate-dateA).seconds
			lapseB = (dateB-interDate).seconds

			# DHI
			if (SourceList[i][1] != "NaN" and SourceList[i+1][1] != "NaN"):
				#print "DNI"
				row.append("{0:.6f}".format(float(SourceList[i][1]) + ( ( (float(SourceList[i][1]) - float(SourceList[i+1][1])) / ((-1)*(lapseA+lapseB)) ) * lapseA ) ) )

			else:
				#print "No DNI"
				row.append("NaN")

			# DHI uncert
			if ((SourceList[i][2] != "NaN") and (SourceList[i+1][2] != "NaN")):
				#print "DHI uncert"
				row.append("{0:.6f}".format(float(SourceList[i][2]) + ( ( (float(SourceList[i][2]) - float(SourceList[i+1][2])) / ((-1)*(lapseA+lapseB)) ) * lapseA ) ) )

			else:
				#print "No DNI uncert"
				row.append("NaN")

			# GHI
			if ((SourceList[i][3] != "NaN") and (SourceList[i+1][3] != "NaN")):
				#print "GHI"
				row.append("{0:.6f}".format(float(SourceList[i][3]) + ( ( (float(SourceList[i][3]) - float(SourceList[i+1][3])) / ((-1)*(lapseA+lapseB)) ) * lapseA ) ) )

			else:
				#print "No GHI"
				row.append("NaN")

			# GHI uncert
			if ((SourceList[i][4] != "NaN") and (SourceList[i+1][4] != "NaN")):
				#print "GHI uncert"
				row.append("{0:.6f}".format(float(SourceList[i][4]) + ( ( (float(SourceList[i][4]) - float(SourceList[i+1][4])) / ((-1)*(lapseA+lapseB)) ) * lapseA ) ) )

			else:
				#print "No GHI uncert"
				row.append("NaN")

			# Diff
			if ((SourceList[i][5] != "NaN") and (SourceList[i+1][5] != "NaN")):
				#print "Diff"
				row.append("{0:.6f}".format(float(SourceList[i][5]) + ( ( (float(SourceList[i][5]) - float(SourceList[i+1][5])) / ((-1)*(lapseA+lapseB)) ) * lapseA ) ) )

			else:
				#print "No Diff"
				row.append("NaN")

			# Diff uncert
			if ((SourceList[i][6] != "NaN") and (SourceList[i+1][6] != "NaN")):
				#print "Diff uncert"
				row.append("{0:.6f}".format(float(SourceList[i][6]) + ( ( (float(SourceList[i][6]) - float(SourceList[i+1][6])) / ((-1)*(lapseA+lapseB)) ) * lapseA ) ) )

			else:
				#print "No Diff uncer"
				row.append("NaN")

			DestWriter.writerow(row)

			i = i + 1


	except:
		print "This is an error message!", sys.exc_info()[0]