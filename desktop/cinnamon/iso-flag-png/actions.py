#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file https://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get, pisitools

def install():
    pisitools.insinto("/usr/share", "%s/flags-%s/usr/share/iso-flag-png" % (get.workDIR(),get.srcVERSION()))

    pisitools.dodoc("README*")
