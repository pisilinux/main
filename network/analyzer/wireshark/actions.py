
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_DOCDIR=/usr/share/doc/wireshark \
                          -G Ninja", sourceDir="..")

def build():
    mesontools.build()

def install():
    mesontools.install()
#"ws_diag_control.h","ws_symbol_export.h"
    for f in ["epan/register.h", "build/config.h","file.h", "cfile.h"]:
        pisitools.insinto("/usr/include/wireshark/", f)

    pisitools.insinto("/usr/include/wireshark/epan/", "epan/*.h")
    pisitools.insinto("/usr/include/wireshark/wsutil/", "wsutil/*.h")
    pisitools.insinto("/usr/include/wireshark/wsutil/wmem/", "wsutil/wmem/*.h")
    pisitools.insinto("/usr/include/wireshark/wiretap/", "wiretap/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/crypt/", "epan/crypt/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/ftypes/", "epan/ftypes/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/dfilter/", "epan/dfilter/*.h")
    pisitools.insinto("/usr/include/wireshark/epan/dissectors/", "epan/dissectors/*.h")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README*")
