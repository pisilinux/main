#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    mesontools.configure()

def build():
    mesontools.build()

def install():
    mesontools.install()

    #pisitools.domove("/usr/share/doc/%s-1.6/*" % get.srcNAME(), "/usr/share/gtk-doc/html/atkmm")
    #pisitools.removeDir("/usr/share/doc/%s-1.6" % get.srcNAME())
    #pisitools.removeDir("/usr/share/devhelp")

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README*")
