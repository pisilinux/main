#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.flags.add("-fwrapv")

    pisitools.dosed("Lib/cgi.py","^#.* /usr/local/bin/python","#!/usr/bin/python")

    shelltools.unlinkDir("Modules/expat")
    shelltools.unlinkDir("Modules/_ctypes/darwin")
    shelltools.unlinkDir("Modules/_ctypes/libffi_osx")

    autotools.rawConfigure("\
                            --prefix=/temp \
                            --enable-shared \
                            --with-threads \
                            --with-computed-gotos \
                            --enable-ipv6 \
                            --with-system-expat \
                            --with-dbmliborder=gdbm:ndbm \
                            --with-system-ffi \
                            --with-system-libmpdec \
                            --enable-loadable-sqlite-extensions \
                            --without-ensurepip")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    shelltools.makedirs("%s/usr" % get.installDIR())
    folders = ("tkinter", "turtledemo", "idlelib")
    for i in folders:
    	pisitools.domove("/temp/lib/python3.9/%s" % i, "/usr/lib/python3.9")
    pisitools.domove("/temp/lib/python3.9/lib-dynload/_tkinter.cpython-39-x86_64-linux-gnu.so", "/usr/lib/python3.9/lib-dynload")
    pisitools.domove("/temp/bin/idle3*", "/usr/bin/")
    
    shelltools.system("sed -i 's/temp/usr/g' %s/usr/bin/idle3.9" % get.installDIR())
    
    pisitools.removeDir("/temp")
