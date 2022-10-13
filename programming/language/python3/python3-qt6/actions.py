#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():   
    shelltools.system("sip-build \
                        --confirm-license \
                        --no-make \
                        --qt-shared \
                        --qmake=/usr/bin/qmake6-qt6 \
                        --api-dir /usr/share/qt6/qsci/api/python3.9 \
                        --pep484-pyi")
    shelltools.system("find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib||g;s|-Wl,-rpath,.* ||g'")

def build():
    autotools.make("-C build")

def install():
    autotools.rawInstall("-C build pyuic6 DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("-C build pylupdate6 DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("-C build DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})

    
    pisitools.dodoc("NEWS", "README","LICENSE*")
