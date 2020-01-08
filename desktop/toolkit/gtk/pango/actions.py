#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools


def setup():
	if get.buildTYPE()=="emul32":
		pisitools.dosed("pango/modules.c", "(pango\.modules)", r"\1-32")
    
    # autotools.autoreconf("-fiv")
    
    #autotools.configure("--disable-static \
                         #--sysconfdir=/etc \
                         #--disable-gtk-doc \
                         #--%sable-introspection" % ("dis" if get.buildTYPE()=="emul32" else "en"))
	
	options = "-Dgtk_doc=false \
			"
	
	if get.buildTYPE()=="emul32" :
		options += "-Dintrospection=false \
		            --bindir=/usr/bin32"
	else:
		options += "-Dintrospection=true"

    #pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")
    
	mesontools.configure(options)

def build():
    mesontools.build()

def install():
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    mesontools.install()
    
    #if get.buildTYPE()=="emul32":
        ##shelltools.move("pango/.libs/pango-querymodules", "pango/.libs/pango-querymodules-32")
        ##pisitools.dobin("pango/.libs/pango-querymodules-32")
        #return

    pisitools.dodir("/etc/pango")
    shelltools.touch(get.installDIR() +"/etc/pango/pango.modules")
    
    if get.buildTYPE()=="emul32" :
       pisitools.removeDir("/usr/bin32")

    pisitools.dodoc("README.md", "NEWS")
