#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("-C tools/bpf/bpftool  ")

def install():
    autotools.rawInstall("-C tools/bpf/bpftool  DESTDIR=%s prefix=/usr" % get.installDIR())

    # pisitools.dodoc("LICENSE*", "README*")
