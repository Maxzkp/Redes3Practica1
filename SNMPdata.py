from pysnmp.hlapi import *

class MonitorInfo:
	def __init__(self, SNMPv = '1', comunity = 'ZKCom', port = '161', hosts = []):
		self.SNMPv = SNMPv
		self.comunity = comunity
		self.port = port
		self.hosts = [host for host in hosts]

	def saveFile(self, filename):
		with open(filename, 'w') as f:
			f.write(f'{self.SNMPv}:{self.comunity}:{self.port}')
			for host in self.hosts:
				f.write(f'\n{host}')

	def readFile(self, filename):
		with open(filename, 'r') as f:
			lines = f.readlines()
			self.SNMPv, self.comunity, self.port = lines[0].split(':')
			if len(lines) > 1:
				self.hosts = [host.strip() for host in lines[1:]]
			else:
				self.hosts = []


	def snmpConsult(self, target, OID):
	    iterator = getCmd(
	        SnmpEngine(),
	        CommunityData(self.comunity, mpModel=(int(self.SNMPv) - 1)),
	        UdpTransportTarget((target, int(self.port))),
	        ContextData(),
	        ObjectType(ObjectIdentity(OID))
	    )

	    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

	    if errorIndication:
	        print(errorIndication)
	        return None

	    elif errorStatus:
	        print('%s at %s' % (errorStatus.prettyPrint(),
	                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
	        return None

	    else:
	        for varBind in varBinds:
	            return varBind[1]
	def addHost(self, host):
		self.hosts.append(host)

	def removeHost(self, host):
		self.hosts.remove(host)
