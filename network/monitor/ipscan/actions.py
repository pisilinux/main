#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir="."
def install():
    pisitools.insinto("/usr/share/java", "%s/ipscan-linux64-3.8.2.jar" % get.workDIR())
