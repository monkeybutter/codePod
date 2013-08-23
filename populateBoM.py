import os
import sys        
import psycopg2
import csv         

# Connect to an existing database
conn = psycopg2.connect("dbname='solar_isd' user='solar' host='localhost' password='dummy'")

# Open a cursor to perform database operations
cur = conn.cursor()

# Delete previous table
cur.execute("DROP TABLE test;")

# Create a new table
cur.execute("CREATE TABLE bom (id serial PRIMARY KEY, stationCode int, cdate timestamp, f00 double precision, f01 double precision, f02 double precision, f03 double precision, f04 double precision, f05 double precision, f06 double precision, f07 double precision, f08 double precision, f09 double precision, f10 double precision, f11 double precision, f12 double precision, f13 double precision, f14 double precision, f15 double precision, f16 double precision, f17 double precision, f18 double precision, f19 double precision, f20 double precision, f21 double precision, f22 double precision, f23 double precision, f24 double precision, f25 double precision, f26 double precision, f27 double precision, f28 double precision, f29 double precision)");

stations = ['3003','5007', '8051', '12038', '14015', '15135', '15590', '23034', '26021', '31011', '39083', '72150', '76031', '86282', '91148', '200284']
#stations = ['3003']

for station in stations:
    print station
    path = "%s%s%s" % ("/mnt/cmar-scratch/roz016/BoM Solar Data/", station, "/1-min/")

    os.chdir(path)
    for files in os.listdir("."):
        if files.endswith(".csv"):
            filePath = "%s%s" % (path, files)
            f = open(filePath, 'rb')    # opens the csv file
            try:
                reader = csv.reader(f)  # creates the reader object
                next(reader)            # skip header row
                for row in reader:      # iterates the rows of the file in orders
                   # Populate table
                   cur.execute("INSERT INTO bom (stationCode, cdate, f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (station, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],))
            finally:
                   conn.commit()
                   f.close()            # closing
