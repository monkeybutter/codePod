from pymongo import Connection
import pymongo
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
      collectionName = 'minute5'
   elif (minLapse==15):
      collectionName = 'minute15'
   elif (minLapse==30):
      collectionName = 'minute30'
   elif (minLapse==60):
      collectionName = 'minute60'
   elif (minLapse==180):
      collectionName = 'minute180'
   else:
      return


   connection = Connection()
   db = connection[databaseName]
   #db.drop_collection(collectionName)
   collection = db[originDBName]
   collectionRollUp = db[collectionName]
   #collectionRollUp.create_index([("stationCode", pymongo.ASCENDING), ("date", pymongo.ASCENDING)], unique=True)
   
   #aggResult = collection.aggregate([{"$group": {"_id":"null", "station":{"$addToSet":"$stationCode"}}}])

   #stationList = aggResult['result'][0]['station']
   #stationList = [23034, 15135, 14015, 12038, 15590, 200284, 5007, 3003, 91148, 72150, 8051, 86282, 39083, 76031, 26021, 31011]
   stationList = [86282, 39083, 76031, 26021, 31011]

   for station in stationList:
      #print station
      aggResult = collection.aggregate([{"$match":{"stationCode":station}}, {"$group": {"_id":"null", "from":{"$min":"$date"}, "to":{"$max":"$date"}}}])
      minDate = aggResult['result'][0]['from']
      maxDate = aggResult['result'][0]['to']
   
      startHour = datetime(minDate.year, minDate.month, minDate.day, 0, 0, 0) 
      endHour = datetime(maxDate.year, maxDate.month, maxDate.day, maxDate.hour+1, 0, 0)
 
      mygenerator = datetimeIterator(startHour, endHour, timedelta(minutes=minLapse))

      for endHour in mygenerator:
         startHour = endHour - timedelta(minutes=minLapse)
         bufferHour = startHour + timedelta(minutes=60)
         print station, startHour, endHour
         aggResult = collection.aggregate([{"$match":{"stationCode":station, "date":{"$gt": startHour, "$lte": endHour}}}, {"$group": {"_id":"null", "avgMeanDirectIrradiance":{"$avg":"$data.MeanDirectIrradiance"}, "avgMeanTerrestrialIrradiance":{"$avg":"$data.MeanTerrestrialIrradiance"}, "avgMeanDiffuseIrradiance":{"$avg":"$data.MeanDiffuseIrrandiance"}, "avgMeanGlobalIrrandiance":{"$avg":"$data.MeanGlobalIrrandiance"}, "avgDHI":{"$avg":"$data.MeanDHI"}, "sum144":{"$sum":"$data.144sunshine"},"sum120":{"$sum":"$data.120sunshine"}, "sum96":{"$sum":"$data.96sunshine"}, "sum":{"$sum":1}}}]) 
         #print 'Aggregation done!'

         if (len(aggResult['result'])>0):
            elements = aggResult['result'][0]['sum']
            #print elements
            if (elements > (.75*minLapse)):
               collectionRollUp.insert({"stationCode":station, "date":endHour, "data" :{"MeanDiffuseIrrandiance":aggResult['result'][0]['avgMeanDiffuseIrradiance'], "MeanDirectIrrandiance":aggResult['result'][0]['avgMeanDirectIrradiance'], "MeanTerrestrialIrrandiance":aggResult['result'][0]['avgMeanTerrestrialIrradiance'], "MeanGlobalIrrandiance":aggResult['result'][0]['avgMeanGlobalIrrandiance'], "MeanDHI":aggResult['result'][0]['avgDHI'], "96sunshine":aggResult['result'][0]['sum96'], "120sunshine":aggResult['result'][0]['sum120'], "144sunshine":aggResult['result'][0]['sum144'] }})
               #print 'Insertion done!'
#rollUp(180)
#rollUp(60)
#rollUp(30)
#rollUp(15)
rollUp(5)
