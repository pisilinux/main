#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import python3modules
from pisi.actionsapi import get
import os


del(os.environ["JOBS"])

shelltools.export("PYTHON", "/usr/bin/python3")
shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())

def setup():
    shelltools.system("./waf configure \
                           --enable-fftw3 \
                           --disable-tests \
                           --libdir=/usr/lib \
                           --prefix=/usr")

def build():
    shelltools.system("./waf build -v")
    shelltools.export("CFLAGS", "-Wno-incompatible-pointer-types")
    python3modules.compile()

def install():
    python3modules.install()
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*")
