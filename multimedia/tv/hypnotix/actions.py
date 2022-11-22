#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #autotools.configure()
    #undefined symbol: mpv_detach_destroy
    pisitools.dosed("usr/lib/hypnotix/mpv.py", "mpv_detach_destroy", "mpv_destroy")
    
def build():
    autotools.make()

def install():
    pisitools.insinto("/usr", "usr/*")
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")
