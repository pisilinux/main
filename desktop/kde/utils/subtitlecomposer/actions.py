#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde6
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    shelltools.system("export PKG_CONFIG_PATH='/usr/lib/ffmpeg4.4/pkgconfig'")
    kde6.configure("DKDE_INSTALL_USE_QT_SYS_PATHS=ON -DQT_MAJOR_VERSION=6")

def build():
    kde6.make()

def install():
    kde6.install()

    pisitools.domo("po/tr.po", "tr", "subtitlecomposer.mo")

    pisitools.dodoc("LICENSES/*", "LICENSE", "README.*")
