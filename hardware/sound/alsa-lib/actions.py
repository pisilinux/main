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
    shelltools.export("CFLAGS", "%s -flto-partition=none" % get.CFLAGS())
    options = "--disable-aload"

    if get.buildTYPE() == "emul32":
        options += " --disable-python \
                     --libdir=/usr/lib32"
                     
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.autoreconf("-fiv")

    autotools.configure(options)
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

    # rpath fix
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.insinto("/usr/share/alsa", "alsa-ucm-conf-1.2.7.1/ucm2")
        pisitools.insinto("/usr/share/doc/alsa-ucm-conf", "alsa-ucm-conf-1.2.7.1/LICENSE")

        pisitools.insinto("/usr/share/alsa", "alsa-topology-conf-1.2.5.1/topology")
        pisitools.insinto("/usr/share/doc/alsa-topology-conf", "alsa-topology-conf-1.2.5.1/LICENSE")
        return

    pisitools.dodoc("ChangeLog", "TODO", "COPYING", "doc/*.txt")
