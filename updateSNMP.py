from time import sleep
from SNMPdata import MonitorInfo
import os

file = 'hosts.txt'
filesize = 0
monitor = MonitorInfo()

while 1:
	if os.path.exists(file):
		filesize = os.stat(file).st_size
		monitor.readFile(file)
		break
	print('Waiting for hosts file...')
	sleep(1)

#inUnicast  1.3.6.1.2.1.2.2.1.11.1
#ipIn       1.3.6.1.2.1.4.3.0
#icmpECHO   1.3.6.1.2.1.5.21.0
#tcpSegsIn  1.3.6.1.2.1.6.10.0
#udpInDtg   1.3.6.1.2.1.7.1.0
OIDs = ('1.3.6.1.2.1.2.2.1.11.1', 
		'1.3.6.1.2.1.4.3.0',
		'1.3.6.1.2.1.5.21.0',
		'1.3.6.1.2.1.6.10.0',
		'1.3.6.1.2.1.7.1.0')

while 1:
	try:
		if os.stat(file).st_size != filesize:
			monitor.readFile(file)
			filesize = os.stat(file).st_size
	except:
		pass

	for host in monitor.hosts:
		info = [monitor.snmpConsult(host, oid) for oid in OIDs]
		print(':'.join([str(e) for e in info]))
	sleep(1)