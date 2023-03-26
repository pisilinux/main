#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

major = ".".join(get.srcVERSION().split(".")[:2])

def setup():
    # shelltools.system('sed "s/^R= \$V.4/R= \$V.5/" -i Makefile')
    pisitools.dosed("src/Makefile", "^CFLAGS.*$", "CFLAGS=%s -fPIC -DLUA_USE_LINUX -DLUA_COMPAT_5_3 -DLUA_COMPAT_5_2 -DLUA_COMPAT_5_1" % get.CFLAGS())
    pisitools.dosed("src/Makefile", "^MYLDFLAGS.*$", "MYLDFLAGS=%s" % get.LDFLAGS())
    pisitools.dosed("lua.pc", "%VER%", "%s" % major)
    pisitools.dosed("lua.pc", "%REL%", "%s" % get.srcVERSION())

def build():
    autotools.make("linux")

def install():
    autotools.rawInstall("INSTALL_TOP=%s/usr INSTALL_MAN=%s/usr/share/man/ INSTALL_LIB=%s/usr/lib/ TO_LIB='liblua.so liblua.so.%s liblua.so.%s'" % (get.installDIR(), get.installDIR(), get.installDIR(), major, get.srcVERSION()))
    
    pisitools.dosym("/usr/lib/liblua.so.5.4.4", "/usr/lib/liblua.so.5.3")

    #pisitools.insinto("/usr/lib", "src/liblua.so*")
    
    pisitools.insinto("/usr/lib/pkgconfig", "lua.pc")
    pisitools.insinto("/usr/lib/pkgconfig", "lua.pc", "lua5.4.pc")
    
    #free directory
    pisitools.removeDir("usr/lib/lua/")
    pisitools.removeDir("usr/share/lua/")

    pisitools.dohtml("doc")
    pisitools.dodoc("README")
