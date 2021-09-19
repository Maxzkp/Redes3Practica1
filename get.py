"""
SNMPv1
++++++

Send SNMP GET request using the following options:

  * with SNMPv1, community 'public'
  * over IPv4/UDP
  * to an Agent at demo.snmplabs.com:161
  * for two instances of SNMPv2-MIB::sysDescr.0 MIB object,

Functionally similar to:

| $ snmpget -v1 -c ZKCom localhost 1.3.6.1.2.1.1.1.0

"""#
from pysnmp.hlapi import *
def snmpConsult(comunity, target, OID):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunity, mpModel=0),
        UdpTransportTarget((target, 161)),
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
            return varBind[1]#' = '.join([x.prettyPrint() for x in varBind])


#inUnicast  1.3.6.1.2.1.2.2.1.11.1
#ipIn       1.3.6.1.2.1.4.3.0
#icmpECHO   1.3.6.1.2.1.5.21.0
#tcpSegsIn  1.3.6.1.2.1.6.10.0
#udpInDtg   1.3.6.1.2.1.7.1.0

if __name__ == '__main__':
    print(snmpConsult('ZKCom', '192.168.1.81', '1.3.6.1.2.1.1.1.0'))
    print(snmpConsult('ZKCom', '192.168.1.81', '1.3.6.1.2.1.1.4.0'))