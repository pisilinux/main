#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("JOBS", get.makeJOBS().replace("-j", ""))

def setup():
    # we are going to compile LV2 with python3 from now on
    # python2 has been deprecated. so fix python interpreter:
    pisitools.dosed("lv2specgen/lv2specgen.py", "python", "python3")
    shelltools.export("CFLAGS", "-Wno-deprecated-declarations")
    shelltools.system("python3 waf configure --prefix=/usr --libdir=/usr/lib/")
    # fix unused dependecy analysis:
    pisitools.dosed("build/c4che/_cache.py", "LINK_CC = \['x86_64-pc-linux-gnu-gcc'\]", "LINK_CC = ['x86_64-pc-linux-gnu-gcc', '-Wl,-O1,--as-needed']")

def build():
    shelltools.system("python3 waf build -v")

def install():
    shelltools.system("DESTDIR=%s python3 waf install" % get.installDIR())

    pisitools.dodoc("COPYING", "README.md")