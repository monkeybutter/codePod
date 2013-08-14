from pymongo import Connection
import pymongo, psycopg2
from psycopg2 import extras
from datetime import datetime, timedelta
 
def datetimeIterator(from_date=None, to_date=None, delta=timedelta(minutes=60)):
   from_date = from_date or datetime.now()
   while to_date is None or from_date <= to_date:
      yield from_date
      from_date = from_date + delta
      return
	 
def rollUp(minLapse=60):
   databaseName = 'solar-isd'
   originDBName = 'minute'

   if (minLapse==5):
      collectionName = '5minute'
   elif (minLapse==15):
      collectionName = '15minute'
   elif (minLapse==60):
      collectionName = '60minute'
   else:
      return

   # Connect to an existing database
   conn = psycopg2.connect("dbname='solar_isd' user='solar' host='localhost' password='dummy'")
   # Open a cursor to perform database operations
   cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

   # Open MongoDB Connection
   connection = Connection()
   db = connection[databaseName]
   db.drop_collection(collectionName)
   collectionRollUp = db[collectionName]
   collection = db[originDBName]
   collectionRollUp.create_index([("stationCode", pymongo.ASCENDING), ("date", pymongo.ASCENDING)], unique=True)
   
   #print 'avant'	   
   #aggResult = collection.aggregate([{"$group": {"_id":"null", "station":{"$addToSet":"$stationCode"}}}])   
   #print 'apres'	   

   #stationList = aggResult['result'][0]['station']
   #print stationList
   stationList = [23034, 15135, 14015, 12038, 15590, 200284, 5007, 3003, 91148, 72150, 8051, 86282, 39083, 76031, 26021, 31011]

   for station in stationList:
      print station
         
      aggResult = collection.aggregate([{"$match":{"stationCode":station}}, {"$group": {"_id":"null", "from":{"$min":"$date"}, "to":{"$max":"$date"}}}])
      minDate = aggResult['result'][0]['from']
      maxDate = aggResult['result'][0]['to']

      startHour = datetime(minDate.year, minDate.month, minDate.day, minDate.hour, 0, 0) 
      endHour = datetime(maxDate.year, maxDate.month, maxDate.day, maxDate.hour, 0, 0)

      mygenerator = datetimeIterator(startHour, endHour, timedelta(minutes=minLapse))

      for endHour in mygenerator:
         startHour = endHour - timedelta(minutes=minLapse)
         print station, startHour, endHour
         cur.execute("SELECT count(*) FROM bom WHERE cdate > DATE '2005-01-01' AND cdate < DATE '2005-01-30';")
         # retrieve the records from the database
         records = cur.fetchall()
         print records

rollUp(5)
