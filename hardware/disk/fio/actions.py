#!/usr/bin/python
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
    shelltools.makedirs("fio-fio-3.36")
    shelltools.cd("fio-fio-3.36")
    shelltools.system("../configure \
        --prefix=/usr \
        --disable-native --enable-gfio")

def build():
    shelltools.cd("fio-fio-3.36")
    autotools.make()

def install():
    shelltools.cd("fio-fio-3.36")
    autotools.install("BINDIR=%(install)s/usr/bin \
                       CONFDIR=%(install)s/etc    \
                       MANDIR=%(install)s/usr/share/man/man1" % { "install": get.installDIR()})
    # pisitools.dodoc("COPYING", "README.rst")
