#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("python2", "/usr/bin/python2.7")

def setup():
    shelltools.system("sed -i 's|python2-config|python2.7-config|g' configure")
    autotools.configure("--without-gtk-doc \
                         --without-nvdimm \
                         --without-dm")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.domove("/gi/overrides/BlockDev.py", "/usr/lib/python2.7/site-packages/gi/overrides")
    pisitools.removeDir("/gi")

    pisitools.dodoc("LICENSE")
