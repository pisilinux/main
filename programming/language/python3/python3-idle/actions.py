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
    #shelltools.unlinkDir("Modules/zlib")
    shelltools.unlinkDir("Modules/_ctypes/darwin")
    #shelltools.unlinkDir("Modules/_ctypes/libffi")
    #shelltools.unlinkDir("Modules/_ctypes/libffi_msvc")
    shelltools.unlinkDir("Modules/_ctypes/libffi_osx")
    #shelltools.unlinkDir("Modules/_decimal/libmpdec")

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
    
    shelltools.mkdir("%s/usr" % get.installDIR())
    
    pisitools.domove("/temp/lib/python3*/tkinter", "/usr/lib/python3*/tkinter")
    pisitools.domove("/temp/lib/python3*/lib-dynload/_tkinter.cpython-38m-x86_64-linux-gnu.so", "/usr/lib/python3*/lib-dynload/_tkinter.cpython-38m-x86_64-linux-gnu.so")
    pisitools.domove("/temp/lib/python3.8/turtledemo", "/usr/lib/python3.8/turtledemo")
    pisitools.domove("/temp/bin/idle3", "/usr/bin/idle3")
    pisitools.domove("/temp/lib/python*/idlelib", "/usr/lib/python*/idlelib")
    
    pisitools.removeDir("/temp")
    #pisitools.remove("/usr/bin/2to3")
    #pisitools.dodoc("LICENSE", "README.*")
