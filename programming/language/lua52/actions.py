#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("sed -i '/#define LUA_ROOT/s:/usr/local/:/usr/:' src/luaconf.h")
    shelltools.system("sed -r -e '/^LUA_(SO|A|T)=/ s/lua/lua5.2/' \
        -e '/^LUAC_T=/ s/luac/luac5.2/'     \
        -i src/Makefile")


    # pisitools.dosed("src/Makefile", "^CFLAGS.*$", "CFLAGS=%s -DLUA_USE_LINUX" % get.CFLAGS())
    # pisitools.dosed("src/Makefile", "^MYLDFLAGS.*$", "MYLDFLAGS=%s" % get.LDFLAGS())
    autotools.make("MYCFLAGS=\"-fPIC\" MYLDFLAGS=\"$LDFLAGS\" linux")

def install():
    options = "TO_BIN=\"lua5.2 luac5.2\" \
               TO_LIB='liblua5.2.so liblua5.2.so.5.2 liblua5.2.so.5.2.4'  \
               INSTALL_DATA=\"cp -d\" \
               INSTALL_TOP=\"%s/usr\"  \
               INSTALL_INC=\"%s/usr/include/lua5.2\" \
               INSTALL_MAN=%s/usr/share/man/man1" % (get.installDIR(),get.installDIR(),get.installDIR())
    autotools.rawInstall(options)

    pisitools.removeDir("/usr/share/lua")
    pisitools.removeDir("/usr/lib/lua")
    
    pisitools.dosym("/usr/lib/liblua5.2.so", "/usr/lib/liblua.so.5.2")
    pisitools.dosym("/usr/lib/liblua5.2.so", "/usr/lib/liblua.so.5.2.4")

    docs = [ "*.html", "*.png", "*.css", "*.gif" ]
    for d in docs:
        pisitools.insinto("/usr/share/doc/lua5.2", "doc/%s" % d)
    pisitools.rename("/usr/share/man/man1/lua.1", "lua.5.2.1")
    pisitools.rename("/usr/share/man/man1/luac.1", "luac.5.2.1")

    pisitools.dosym("/usr/lib/pkgconfig/lua5.2.pc", "/usr/lib/pkgconfig/lua-5.2.pc")
    pisitools.dosym("/usr/lib/pkgconfig/lua5.2.pc", "/usr/lib/pkgconfig/lua52.pc")
