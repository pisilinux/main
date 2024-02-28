#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools

def setup():
    kde6.configure("-DBUILD_KWALLET_QUERY=OFF")

def build():
    kde6.make()

def install():
    kde6.install()
    pisitools.remove("/usr/share/dbus-1/services/org.kde.kwalletd5.service")
    # pisitools.remove("/usr/share/man/man1/kwallet-query.1")

    pisitools.dodoc("README.md")
