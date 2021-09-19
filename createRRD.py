#!/usr/bin/env python

import rrdtool

def create(filename)
    ret = rrdtool.create(filename,
                         "--start",'N',
                         "--step",'60',
                         "DS:inunicast:COUNTER:600:U:U",
                         "DS:inip:COUNTER:600:U:U",
                         "DS:icmpecho:COUNTER:600:U:U",
                         "DS:tcpsegsin:COUNTER:600:U:U",
                         "DS:udpindtgr:COUNTER:600:U:U",
                         "RRA:AVERAGE:0.5:6:5",
                         "RRA:AVERAGE:0.5:1:20")

    if ret:
        print (rrdtool.error())