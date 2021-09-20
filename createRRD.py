#!/usr/bin/env python
import sys
import rrdtool

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

def graph(filename, var, title, descr, t0 = 'N', tf = 'N'):
    ret = rrdtool.graph(f'rrd/{filename} {var}.png',
                     "--start",t0,
                     "--end",tf,
                     "--vertical-label=Bytes/s",
                     f"--title={title}",
                     f"DEF:{var}=rrd/{filename}.rrd:{var}:AVERAGE",
                     f"LINE3:{var}#0000FF:{descr}")