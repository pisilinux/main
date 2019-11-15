#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "KoboDeluxe-%s" % get.srcVERSION()

def setup():
    autotools.configure('--enable-opengl \
                         --sharedstatedir="/var" \
                         --disable-dependency-tracking')

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("ChangeLog", "README*", "TODO")
