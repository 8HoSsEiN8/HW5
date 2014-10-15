

def addCheckSum(buff):
	
	#print "Original Command:\t", buff

	cSum = 0x00
	for i in range(2, len(buff)):
		cSum = cSum + (buff[i] & 0xFF)

	cSum = ~cSum
	buff.append(cSum & 0xFF)
	#print "Command with Checksum:\t", buff
	return buff

def setVelocity(ID, direction, RPM):
		
	speed = ( (1022 * RPM) - 909 ) / 113
	speed = speed & 0x03FF	# Maximum speed is 1023
	
	if (direction == 1):	# CW Direction Turn
		speed = speed | 0x0400
	if (RPM == 0):
		speed = 0
			
	buff = [255, 255]
	buff.append(ID)				# ID
	buff.append(4)				# Length
	buff.append(0x20)			# Instruction	
	buff.append(speed & 0xFF)	# Moving Speed(L)
	buff.append(speed >> 8)		# Moving Speed(H)
	
	buff = addCheckSum(buff)
	return buff

def setAngleLimit(ID, CWlimit, CCWlimit):
	buff = [255, 255]
	buff.append(ID)				# ID
	buff.append(6)				# Length
	buff.append(6)				# Instruction	
	buff.append(CWlimit & 0xFF)	# CW Angle Limit(L)
	buff.append(CWlimit >> 8)	# CW Angle Limit(H)	
	buff.append(CCWlimit & 0xFF)# CCW Angle Limit(L)
	buff.append(CCWlimit >> 8)	# CCW Angle Limit(H)
	
	buff = addCheckSum(buff)
	return buff
