#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# def setup():
    # autotools.configure()

def build():
    autotools.make("-C src")

def install():
    autotools.rawInstall("-C src  DESTDIR=%s LIBSUBDIR=lib" % get.installDIR())
    pisitools.remove("/usr/lib/libbpf.a")

    pisitools.dodoc("LICENSE*", "README*")
