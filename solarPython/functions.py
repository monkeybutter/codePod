from datetime import timedelta, datetime
import math, calendar, datetime

def getMeanSolar(datetimeUTC, lon):
    return datetimeUTC + timedelta(hours=lon / 15)

def getUTCfromMean(datetimeMean, lon):
	return datetimeMean - timedelta(hours=lon / 15)

def getTrueSolar(datetimeUTC, lon):

	if calendar.isleap(datetimeUTC.year):
    	# Leap year, 366 days
		lMonth = [0,31,60,91,121,152,182,213,244,274,305,335,366]
	else:
	    # Normal year, 365 days
	    lMonth = [0,31,59,90,120,151,181,212,243,273,304,334,365]

	DoY = lMonth[datetimeUTC.month-1] + datetimeUTC.day

	EoT = (((5.0323-(430.847*math.cos((((2*math.pi)*DoY)/366.0)+4.8718)))\
	                + (12.5024*(math.cos(2*((((2*math.pi)*DoY)/366.0)+4.8718))))\
	                + (18.25*(math.cos(3*((((2*math.pi)*DoY)/366.0)+4.8718))))\
	                - (100.976*(math.sin((((2*math.pi)*DoY)/366.0)+4.8718))))\
	                + (595.275*(math.sin(2*((((2*math.pi)*DoY)/366.0)+4.8718))))\
	                + (3.6858*(math.sin(3*((((2*math.pi)*DoY)/366.0)+4.871))))\
	                - (12.47*(math.sin(4*((((2*math.pi)*DoY)/366.0)+4.8718)))))\
	                / 60.0

	return getMeanSolar(datetimeUTC + timedelta(minutes=EoT), lon) 


def getUTCfromTrue(datetimeTrue, lon):
	datetimeX = datetimeTrue - timedelta(hours=lon / 15)

	if calendar.isleap(datetimeX.year):
    	# Leap year, 366 days
		lMonth = [0,31,60,91,121,152,182,213,244,274,305,335,366]
	else:
	    # Normal year, 365 days
	    lMonth = [0,31,59,90,120,151,181,212,243,273,304,334,365]

	DoY = lMonth[datetimeX.month-1] + datetimeX.day

	EoT = (((5.0323-(430.847*math.cos((((2*math.pi)*DoY)/366.0)+4.8718)))\
	                + (12.5024*(math.cos(2*((((2*math.pi)*DoY)/366.0)+4.8718))))\
	                + (18.25*(math.cos(3*((((2*math.pi)*DoY)/366.0)+4.8718))))\
	                - (100.976*(math.sin((((2*math.pi)*DoY)/366.0)+4.8718))))\
	                + (595.275*(math.sin(2*((((2*math.pi)*DoY)/366.0)+4.8718))))\
	                + (3.6858*(math.sin(3*((((2*math.pi)*DoY)/366.0)+4.871))))\
	                - (12.47*(math.sin(4*((((2*math.pi)*DoY)/366.0)+4.8718)))))\
	                / 60.0

	return datetimeX - timedelta(minutes=EoT)