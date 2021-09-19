from time import sleep
from get import snmpConsult

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

comName = input('Nombre de la comunidad: ')
hosts = []
print('A continuacion indique al menos un host a monitorizar')
warning = ''

while 1:
	host = input(f'Direccion IP del host{warning}: ')

	if host == None or host == '':
		print('No se ingreso un host')
		continue

	if host == 'n':
		break

	hosts.append(host)

	warning = ' (Si no desea otro host escriba n)'

#print(hosts)
while 1:
	for host in hosts:
		info = [snmpConsult(comName, host, oid) for oid in OIDs]
		print(':'.join([str(e) for e in info]))
	sleep(1)