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

#WorkDir="PyQt5_gpl-%s" % get.srcVERSION()

def setup():
    shelltools.system("sip-build \
                        --confirm-license \
                        --no-make \
                        --qt-shared \
                        --qmake=/usr/bin/qmake \
                        --api-dir /usr/share/qt5/qsci/api/python3.11 \
                        --pep484-pyi")
    shelltools.system("find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib||g;s|-Wl,-rpath,.* ||g'")

def build():
    autotools.make("-C build")

def install():
    #shelltools.cd("%s/PyQt5_gpl-%s" % (get.workDIR(),get.srcVERSION()))
    autotools.rawInstall("-C build pyrcc DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("-C build pylupdate DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})
    autotools.rawInstall("-C build DESTDIR=%(DESTDIR)s INSTALL_ROOT=%(DESTDIR)s" % {'DESTDIR':get.installDIR()})

    
    #pisitools.dohtml("doc/html/*")
    pisitools.dodoc("NEWS", "LICENSE*")
