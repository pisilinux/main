#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    options = "--disable-aload --without-debug"

    #if get.buildTYPE() == "emul32":
    #    options += " --disable-python"
    #    shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    #autotools.autoreconf("-fi")
    pisitools.cflags.add("-Wno-address-of-packed-member -Wno-unused-result")
    autotools.configure(options)
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    # rpath fix
    #pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    #pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()
    autotools.make("doc")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #if get.buildTYPE() == "emul32": return

    pisitools.dodoc("COPYING", "MEMORY-LEAK", "NOTES")
    pisitools.dohtml("doc/doxygen/html/*")