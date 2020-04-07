#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import autotools
from pisi.actionsapi import qt5
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir="qt-creator-opensource-src-%s" % get.srcVERSION()
def setup():
    pisitools.dosed("qtcreator.pri", "libexec/qtcreator", "lib/qtcreator")
    pisitools.dosed("src/tools/tools.pro", "libexec", "lib")

    shelltools.system("qmake LLVM_INSTALL_DIR=/usr QBS_INSTALL_DIR=/usr \
                             CONFIG+=release QMAKE_CFLAGS_ISYSTEM=-I \
                             DEFINES+=QBS_ENABLE_PROJECT_FILE_UPDATES \
                             QTC_PREFIX=/usr qtcreator.pro")


def build():
    qt5.make()
def install():
    qt5.install()
