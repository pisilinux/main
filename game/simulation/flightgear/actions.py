#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True
Version = get.srcVERSION()


def install():
    pisitools.dodir ("/opt/flightgear")
    pisitools.doexe("flightgear-%s-linux-amd64.AppImage" % Version, "/opt/flightgear")
    pisitools.dosym("/opt/flightgear/flightgear-%s-linux-amd64.AppImage" % Version, "/usr/bin/fgfs")
 