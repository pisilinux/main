
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    # shelltools.makedirs("build")
    # shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_DOCDIR=/usr/share/doc/wireshark \
                          -DUSE_qt6=ON \
                          -DENABLE_LUA=ON \
                          -B build -G Ninja")

def build():
    shelltools.system("ninja -C build")

def install():
    # shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

    #"ws_diag_control.h","ws_symbol_export.h"
    # shelltools.cd("build")
    for f in ["epan/register.h", "build/config.h","file.h", "epan/cfile.h"]:
        pisitools.insinto("/usr/include/wireshark/", f)

    pisitools.insinto("/usr/include/wireshark/epan/", "epan/*.h")
    pisitools.insinto("/usr/include/wireshark/wsutil/", "wsutil/*.h")
    pisitools.insinto("/usr/include/wireshark/wsutil/wmem/", "wsutil/wmem/*.h")
    pisitools.insinto("/usr/include/wireshark/wiretap/", "wiretap/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/crypt/", "epan/crypt/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/ftypes/", "epan/ftypes/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/dfilter/", "epan/dfilter/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/dissectors/", "epan/dissectors/*.h")


    # shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README*")
