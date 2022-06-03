#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools


def install():
    # Install branding icon
    fldr = ("icons","lang-all")
    for i in fldr:
    	pisitools.insinto("/usr/share/pixmaps/icons", "%s/*" % i)
