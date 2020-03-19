#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    #package name change
    pisitools.dosed("mate-system-monitor.desktop.in*", "_Name=MATE System Monitor", "_Name=System Monitor")
    
    pisitools.dosed("configure", "GLIB_REQUIRED=2.56.0", "GLIB_REQUIRED=2.54.3")
    pisitools.dosed("src/load-graph.cpp", "G_FORMAT_SIZE_BITS", "G_FORMAT_SIZE_IEC_UNITS")

    autotools.configure("--disable-static \
                         --libexecdir=/usr/lib \
                         --disable-scrollkeeper")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")
