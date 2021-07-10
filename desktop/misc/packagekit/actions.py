#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    #shelltools.system("sed -i 's@self.filesdb@# self.filesdb@g' backends/pisi/pisiBackend.py")

    autotools.configure("--enable-pisi \
               --with-default-backend=pisi \
               --disable-dummy \
               --disable-bash-completion \
               --disable-man-pages \
               --disable-static \
               --disable-systemd \
               --disable-offline-update")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "MAINTAINERS", "COPYING", "README", "NEWS")
