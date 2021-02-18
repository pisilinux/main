#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
        #autotools.autoreconf("-vfi")
    options = "--disable-static \
               --disable-rpath \
              "
              
    if get.buildTYPE() == "emul32":
        options += "--disable-qv4l2"
        
        
    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")


def build():
	if get.buildTYPE() == "emul32":
		autotools.make("-C lib")
	else:
		autotools.make()

def install():
	if get.buildTYPE() == "emul32":
		autotools.make("MAKEFLAGS='-j1' -C lib DESTDIR=%s install" % get.installDIR())
		pisitools.removeDir("/emul32")
	else:
		autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	
    
    #if get.buildTYPE() == "emul32": return

	pisitools.dodoc("ChangeLog", "COPYING*", "README*", "TODO")
	pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "contrib")

