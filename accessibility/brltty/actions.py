#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

pisitools.cxxflags.add("-std=gnu++11")

def setup():
    pisitools.flags.add(" -lspeechd")
    shelltools.export("PYTHON","/usr/bin/python3")
    autotools.configure(" \
                --with-tables-directory=/usr/share/brltty \
                --with-screen-driver=lx \
                --enable-gpm \
                --with-espeak \
                --with-install-root='%s'  \
                --with-writable-directory='/run/brltty' \
                --disable-stripping \
                --disable-ocaml-bindings \
                --disable-java-bindings" % get.installDIR())

def build():
    autotools.make(" -j1")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s install" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s install-udev" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s install-polkit" % get.installDIR())
    #pisitools.removeDir("/run")
    pisitools.removeDir("/var")
    pisitools.dodoc("LICENSE*", "README")
	
