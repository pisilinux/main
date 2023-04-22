#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt
#
# TODO: ADD GDATA AND GNOME ONLINE ACCOUNTS SUPPORT

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # pisitools.dosed("CMakeLists.txt", "webkit2gtk-4.1", "webkit2gtk-5.0")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr   \
                          -DSYSCONF_INSTALL_DIR=/etc    \
                          -DENABLE_VALA_BINDINGS=ON     \
                          -DENABLE_INSTALLED_TESTS=ON   \
                          -DENABLE_GOOGLE=OFF           \
                          -DENABLE_GOOGLE_AUTH=OFF      \
                          -DWITH_OPENLDAP=OFF           \
                          -DWITH_KRB5=ON                \
                          -DENABLE_INTROSPECTION=ON     \
                          -DENABLE_CANBERRA=ON          \
                          -DENABLE_WEATHER=ON           \
                          -DENABLE_GTK=ON               \
                          -DENABLE_GTK_DOC=OFF          \
                          -DENABLE_OAUTH2=ON            \
                          -DENABLE_GOA=OFF              \
                          -DENABLE_OAUTH2_WEBKITGTK=ON \
                          -DWITH_SYSTEMDUSERUNITDIR=NO")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "ChangeLog", "HACKING", "MAINTAINERS", "NEWS", "README")

