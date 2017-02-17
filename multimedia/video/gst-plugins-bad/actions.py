#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "true")
    pisitools.dosed("autogen.sh", "tool_run.*autopoint --force.*")

    pisitools.dosed("ext/modplug/gstmodplug.cc", "stdafx.h", "libmodplug/stdafx.h")
    pisitools.dosed("configure.ac", "AM_CONFIG_HEADER", "AC_CONFIG_HEADERS")

    shelltools.export("NOCONFIGURE", "1")
    shelltools.system("./autogen.sh")

    autotools.configure("--with-package-name='PisiLinux gstreamer-plugins-bad package' \
                         --with-package-origin='http://www.pisilinux.org'")

    # for fix unused dependency
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "RELEASE", "REQUIREMENTS")

