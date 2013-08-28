import csv
import functions
import json
from datetime import timedelta, datetime
from os import listdir
from os.path import isfile, join


stations = []

element = {}
element['id'] = '003003'
element['longitude'] = 122.2353
element['closeDate'] = datetime(1990, 2, 1, 0, 0, 0)
element['name'] = "Broome Airport"

stations.append(element)

element = {}
element['id'] = '004032'
element['longitude'] = 118.6317
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Port Hedland Airport"

stations.append(element)

element = {}
element['id'] = '005007'
element['longitude'] = 114.0967
element['closeDate'] = datetime(1990, 2, 1, 0, 0, 0)
element['name'] = "Learmonth Airport"

stations.append(element)

element = {}
element['id'] = '006011'
element['longitude'] = 113.67
element['closeDate'] = datetime(1990, 2, 1, 0, 0, 0)
element['name'] = "Carnarvon Airport"

stations.append(element)

element = {}
element['id'] = '007045'
element['longitude'] = 118.5372
element['closeDate'] = datetime(1990, 2, 1, 0, 0, 0)
element['name'] = "Meekatharra Airport"

stations.append(element)

element = {}
element['id'] = '008051'
element['longitude'] = 114.6975
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Geraldton Airport Comp"

stations.append(element)

element = {}
element['id'] = '008315'
element['longitude'] = 114.6989
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)  #Not found
element['name'] = "Geraldton Airport"

stations.append(element)

element = {}
element['id'] = '009021'
element['longitude'] = 115.9764
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Perth Airport"

stations.append(element)

element = {}
element['id'] = '009053'
element['longitude'] = 116.0189
element['closeDate'] = datetime(1975, 1, 1, 0, 0, 0)
element['name'] = "Pearce Raaf"

stations.append(element)

element = {}
element['id'] = '009741'
element['longitude'] = 117.8022
element['closeDate'] = datetime(1988, 10, 1, 0, 0, 0)
element['name'] = "Albany Airport Comparison"

stations.append(element)

element = {}
element['id'] = '009789'
element['longitude'] = 121.8925
element['closeDate'] = datetime(1990, 2, 1, 0, 0, 0)
element['name'] = "Esperance"

stations.append(element)

element = {}
element['id'] = '012038'
element['longitude'] = 121.4533
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Kalgoorlie-Boulder Airport"

stations.append(element)

element = {}
element['id'] = '014015'
element['longitude'] = 130.8925
element['closeDate'] = datetime(1989, 12, 1, 0, 0, 0)
element['name'] = "Darwin Airport"

stations.append(element)

element = {}
element['id'] = '015135'
element['longitude'] = 134.1833
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)  #Not found
element['name'] = "Tennant Creek Airport"

stations.append(element)

element = {}
element['id'] = '015590'
element['longitude'] = 133.889
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Alice Springs Airport"

stations.append(element)

element = {}
element['id'] = '016001'
element['longitude'] = 136.8054
element['closeDate'] = datetime(1988, 7, 1, 0, 0, 0)
element['name'] = "Woomera Aerodrome"

stations.append(element)

element = {}
element['id'] = '023034'
element['longitude'] = 138.5204
element['closeDate'] = datetime(1990, 1, 1, 0, 0, 0)
element['name'] = "Adelaide Airport"

stations.append(element)

element = {}
element['id'] = '026021'
element['longitude'] = 140.7739
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Mt Gambier Aero"

stations.append(element)

element = {}
element['id'] = '031011'
element['longitude'] = 145.7458
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)  #Not found
element['name'] = "Cairns Aero"

stations.append(element)

element = {}
element['id'] = '032040'
element['longitude'] = 146.7661
element['closeDate'] = datetime(1990, 2, 1, 0, 0, 0)
element['name'] = "Townsville Aero"

stations.append(element)

element = {}
element['id'] = '036031'
element['longitude'] = 144.2828
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Longreach Aero"

stations.append(element)

element = {}
element['id'] = '039083'
element['longitude'] = 150.4775
element['closeDate'] = datetime(1988, 10, 1, 0, 0, 0)
element['name'] = "Rockhampton Aero"

stations.append(element)

element = {}
element['id'] = '040223'
element['longitude'] = 153.1142
element['closeDate'] = datetime(1990, 1, 1, 0, 0, 0)
element['name'] = "Brisbane Aero"

stations.append(element)

element = {}
element['id'] = '048027'
element['longitude'] = 145.8294
element['closeDate'] = datetime(1988, 10, 1, 0, 0, 0)  #Not found
element['name'] = "Cobar MO"

stations.append(element)

element = {}
element['id'] = '066037'
element['longitude'] = 151.1731
element['closeDate'] = datetime(1990, 1, 1, 0, 0, 0)
element['name'] = "Sydney Airport AMO"

stations.append(element)

element = {}
element['id'] = '070014'
element['longitude'] = 149.2014
element['closeDate'] = datetime(1990, 1, 1, 0, 0, 0)
element['name'] = "Canberra Airport Comparison"

stations.append(element)

element = {}
element['id'] = '072150'
element['longitude'] = 147.4575
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Wagga Wagga AMO"

stations.append(element)

element = {}
element['id'] = '076031'
element['longitude'] = 142.0867
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Mildura Airport"

stations.append(element)

element = {}
element['id'] = '086071'
element['longitude'] = 144.9700
element['closeDate'] = datetime(1976, 11, 1, 0, 0, 0)
element['name'] = "Melbourne Regional Office"

stations.append(element)

element = {}
element['id'] = '086282'
element['longitude'] = 144.8321
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)  #Not found
element['name'] = "Melbourne Airport"

stations.append(element)

element = {}
element['id'] = '087031'
element['longitude'] = 144.7566
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Laverton RAAF"

stations.append(element)

element = {}
element['id'] = '091148'
element['longitude'] = 144.6892
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0) #Not found
element['name'] = "Cape Grim Radiation"

stations.append(element)

element = {}
element['id'] = '094008'
element['longitude'] = 147.5033
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0)
element['name'] = "Hobart Airport"

stations.append(element)

element = {}
element['id'] = '200284'
element['longitude'] = 96.8344
element['closeDate'] = datetime(1989, 11, 1, 0, 0, 0) #Not found
element['name'] = "Cocos Island Airport"

stations.append(element)

element = {}
element['id'] = '300001'
element['longitude'] = 62.8753
element['closeDate'] = datetime(1978, 1, 1, 0, 0, 0)
element['name'] = "Mawson"

stations.append(element)

element = {}
element['id'] = '300004'
element['longitude'] = 158.9369
element['closeDate'] = datetime(1988, 2, 1, 0, 0, 0)
element['name'] = "Macquarie Island"

stations.append(element)

element = {}
element['id'] = '300006'
element['longitude'] = 110.5333
element['closeDate'] = datetime(1977, 11, 1, 0, 0, 0)
element['name'] = "Casey (The Tunnel)"

stations.append(element)

for station in stations:
	print station['name']
	sourceDNIPath = "/Users/SmartWombat/Dropbox/SolarData/DNI/DC02D_Data_" + station['id'] + ".txt"
	sourceGHIPath = "/Users/SmartWombat/Dropbox/SolarData/GHI/DC02D_Data_" + station['id'] + ".txt"
	sourceDiffusePath = "/Users/SmartWombat/Dropbox/SolarData/Diffuse/DC02D_Data_" + station['id'] + ".txt"
	destPath = "/Users/SmartWombat/Dropbox/SolarData/Phase1/DC02D_Data_" + station['id'] + "_UTC.csv"

	DNI = open(sourceDNIPath, 'rb') # opens the csv file
	GHI = open(sourceGHIPath, 'rb') # opens the csv file
	Diffuse = open(sourceDiffusePath, 'rb') # opens the csv file
	Dest = open(destPath, 'wb')

	try:
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
				if (counterDate < station['closeDate']):
					#old station Mean Solar Time
					UTCDate = functions.getUTCfromMean(counterDate, station['longitude'])

				else:
					#new station True Solar Time
					UTCDate = functions.getUTCfromTrue(counterDate, station['longitude'])

				row.append(UTCDate.strftime("%Y-%m-%dT%H:%M:%S"))

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


	except:
		print "This is an error message!"