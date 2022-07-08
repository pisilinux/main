#!/usr/bin/python
# -*- coding: utf-8 -*-·
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pythonmodules.configure("--default-graphics=spice --default-hvs qemu,xen,lxc", pyVer="3")
    pythonmodules.compile(pyVer="3")

def install():
    shelltools.system("""touch --no-create %s/usr/share/icons/hicolor >/dev/null 2>&1 || :
                                /usr/bin/update-desktop-database > /dev/null 2>&1 || :""" % get.installDIR())

    shelltools.system("python3 setup.py --no-update-icon-cache --no-compile-schemas install --root=%s --no-compile -O0" % get.installDIR())
    #pythonmodules.install(pyVer="3")
    #pisitools.dodoc("COPYING", "NEWS", "README*", "PKG-INFO")
