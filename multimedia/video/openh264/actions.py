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
    autotools.make("PREFIX=/usr")

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr install-shared" % get.installDIR())
    pisitools.dobin("h264dec")
    pisitools.dobin("h264enc")
    pisitools.remove("/usr/lib/libopenh264.a")

    pisitools.dodoc("LICENSE", "README*")
