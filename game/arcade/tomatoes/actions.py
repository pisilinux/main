#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

ketchup = "/usr/share/tomatoes"
WorkDir="tomatoes-%s" %get.srcVERSION()

def setup():
    pisitools.dosed("makefile", "_pardus_cflags", get.CFLAGS())
    pisitools.dosed("makefile", "_pardus_ldflags", "-lm -lstdc++ %s" % get.LDFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("tomatoes")
    pisitools.insinto("/usr/share/pixmaps", "icon.png", "tomatoes.png")
    
    pisitools.dodir("%s/music" % ketchup)
    pisitools.insinto(ketchup, "tomatoes-1.5/tomatoes.mpk")
    pisitools.insinto("%s/music" % ketchup, "tomatoes-1.5/music/IHaveNoTomatoes.it")

