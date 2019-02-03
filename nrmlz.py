#CVS NORMALIZER TOOL | GARRETT GRUBE | 1/31/19 | Truss Work Sample | nrmlz.py
#This script contains the functions that "normalize" the data in each row of the .csv file

import pytz, copy
from datetime import *

def normalize(r):						#divide and conquer the row! 			
	nTime = normTime(r[0]);				#call the appropriate normalizing function for each entry type
	nAddress = normAddress(r[1]);
	nZIP = normZIP(r[2]);
	nName = normName(r[3]);
	nFooDur = normFooDur(r[4]);
	nBarDur = normBarDur(r[5]);
	nTotalDur = normTotDur(nFooDur,nBarDur);
	nNotes = normNotes(r[7]);
	return [nTime, nAddress, nZIP, nName, nFooDur, nBarDur, nTotalDur, nNotes]

def normTime(time):	
	nTime = copy.deepcopy(time)
	try:
		dt = datetime.strptime(nTime, "%d/%m/%y %I:%M:%S %p")				#parse time into datetime object
		dt = pytz.timezone('US/Pacific').localize(dt)						#localize it to Pacific time
		dt = dt.astimezone(pytz.timezone('US/Eastern'))						#REQ_2 | convert time stamp to Eastern time				
		nTime = dt.isoformat()												#REQ_1 | timestamp column should be formatted in ISO-8601 format										
	except:
		return time
	else:
		return nTime						

def normAddress(address):
	nAddress = address             	#REQ_5.1 | Address should be passed through as is
	return nAddress

def normZIP(ZIP):
	zeros = 5 - len(ZIP)
	while zeros != 0:
		ZIP = '0' + str(ZIP)		#REQ_3 | ZIPs should be 5 digits - add leading zeros if needed 
		zeros-=1
	#print(ZIP)
	return str(ZIP)

def normName(name):
	nName = name.upper() 			#REQ_4 | convert names to all uppercase
	return nName

def normFooDur(fooDur):
	st = sliceTime(fooDur)			
	nFooDur = toFloatSeconds(st)   	#REQ_6 | convert HH:MM:SS.MS to floating point seconds format
	return nFooDur

def normBarDur(barDur):
	st = sliceTime(barDur)			
	nBarDur = toFloatSeconds(st)		#REQ_6 | convert HH:MM:SS.MS to floating point seconds format
	return nBarDur

def normTotDur(nFooDur, nBarDur):
	nTotDur = float(nFooDur + nBarDur) 	#REQ_7 | replace value of total duration as sum of foodur and bardur
	return nTotDur

def normNotes(notes):
	nNotes = notes 						#REQ_8 | do not perform any transformations on notes
	return nNotes

def sliceTime(time):				#helper function - slice out the individual components of the HH:MM:SS.MS time string
	indx = [i for i, ltr in enumerate(time) if ltr == ':']  #finds location of all ':' in time string
	hrs = time[0:indx[0]]
	mins = time[(indx[0]+1):indx[1]]
	secs = time[(indx[1]+1):time.find('.')]
	msec = time[(time.find('.')+1):]
	slicedTime = [hrs, mins, secs, msec]
	return slicedTime

def toFloatSeconds(slTime):						#helper function to normDur functions		
	totalSeconds = 0;							#running total of seconds
	totalSeconds+= float(slTime[0])*60*60 		#convert hours to seconds and add to total
	totalSeconds+= float(slTime[1])*60			#convert mins to seconds and add to total
	totalSeconds+= float(slTime[2])				#add seconds to total
	totalSeconds+= float(float(slTime[3])/1000)	#convert ms to seconds and add to total
	return float(totalSeconds)					#return total as a float value