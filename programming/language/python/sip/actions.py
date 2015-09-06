#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(),  get.srcVERSION())
py2dir = get.curPYTHON()

def setup():
    pythonmodules.run('configure.py \
                    -b /usr/bin \
                    -d /usr/lib/%s/site-packages \
                    -e /usr/include/%s \
                    CFLAGS+="%s" CXXFLAGS+="%s"' % (py2dir, py2dir, get.CFLAGS(), get.CXXFLAGS()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.remove("/usr/bin/sip")
    pisitools.dodoc("LICENSE*", "NEWS", "README")
