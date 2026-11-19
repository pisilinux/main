#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
zzz
def setup():

    shelltools.makedirs("build")
    shelltools.cd("build")
    # shelltools.system('export CFLAGS="$CFLAGS -fcommon"')
    # shelltools.system('export LDFLAGS="$LDFLAGS -Wl,--export-dynamic"')
    cmaketools.configure("-DCMAKE_BUILD_TYPE='Debug' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -DCMAKE_INSTALL_LIBDIR='lib' \
        -DHARDINFO_GTK3='ON' \
        -Wno-dev  \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
        -DHARDINFO_DEBUG='$(usex debug 1 0)'", sourceDir="..")

def build():
    cmaketools.make("-C build")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # shelltools.chmod(get.installDIR() + "/usr/lib/hardinfo/modules/*.so")

    pisitools.dodoc("../LICENSE")

