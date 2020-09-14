Value DEVICE_ID (\S+)
Value LOCAL_INT (\S+)
Value CAPABILITY (\w+)
Value PORT_ID (\S+)

Start
	^Device.*ID -> INFO

INFO
	^${DEVICE_ID}\s+${LOCAL_INT}\s+\d+\s+${CAPABILITY}\s+${PORT_ID} -> Record



