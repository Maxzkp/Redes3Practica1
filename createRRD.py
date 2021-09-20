#!/usr/bin/env python
import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 600

def create(filename):
    ret = rrdtool.create(f'rrd/{filename}.rrd',
                         "--start",'N',
                         "--step",'60',
                         "DS:inunicast:COUNTER:600:U:U",
                         "DS:inip:COUNTER:600:U:U",
                         "DS:icmpecho:COUNTER:600:U:U",
                         "DS:tcpsegsin:COUNTER:600:U:U",
                         "DS:udpindtgr:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:6:5",
                         "RRA:AVERAGE:0.5:1:30")

    if ret:
        print (rrdtool.error())

def graph(filename, var, title, descr):
    ret = rrdtool.graph(f'rrd/{filename} {var}.png',
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Bytes/s",
                     f"--title={title}",
                     f"DEF:{var}=rrd/{filename}.rrd:{var}:AVERAGE",
                     f"LINE3:{var}#0000FF:{descr}")