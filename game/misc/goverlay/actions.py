#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("cp -a /usr/lib/lazarus %s/lazarus-build" % get.workDIR())

    lazarus_dir = "%s/lazarus-build" % get.workDIR()

    autotools.make(
        'LAZBUILDOPTS="--ws=qt6 --lazarusdir=%s"' % lazarus_dir
    )

def check():
    autotools.make("tests")

def install():
    autotools.rawInstall(
        "DESTDIR=%s prefix=/usr libexecdir=/lib" % get.installDIR()
    )

    pisitools.dosym("/usr/lib/pascube", "/usr/bin/pascube")

    pisitools.dodoc("LICENSE")