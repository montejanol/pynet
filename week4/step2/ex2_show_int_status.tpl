Value PORT_NAME (\S+)
Value STATUS (\S+)
Value VLAN (\d+)
Value DUPLEX (\S+)
Value SPEED (\S+)
Value PORT_TYPE (\S+)


Start
	^Port.*Type\s*$$ -> Interface_Status

Interface_Status
	^${PORT_NAME}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${PORT_TYPE} -> Record
