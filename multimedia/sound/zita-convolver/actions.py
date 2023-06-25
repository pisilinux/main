#!/usr/bin/python
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


WorkDir = "zita-convolver-%s" % get.srcVERSION()

def setup():
    shelltools.system("sed -e '/native/d; s/ldconfig/& -N $(DESTDIR)\/$(LIBDIR)/' -i source/Makefile")
    # autotools.configure()

def build():
    autotools.make("-C source")

#def check():
    #autotools.make("check")

def install():
    autotools.rawInstall("-C source DESTDIR=%s PREFIX=/usr LIBDIR=/usr/lib" % get.installDIR())
    pisitools.dodoc("COPYING", "README")
