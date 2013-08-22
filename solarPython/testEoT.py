from datetime import timedelta, datetime
import math, calendar


for i in range(12):

	datetimeX = datetime(2012, i+1, 1)

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

	print datetimeX.strftime("%Y-%m-%dT%H:%M:%S")
	print EoT