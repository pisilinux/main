#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os


def setup():
	shelltools.export("CARGO_HOME", os.path.join(get.workDIR(), ".cargo"))

def build():
	shelltools.system("make")

    
def install():
	shelltools.system("make DESTDIR=%s install" % get.installDIR())
	pisitools.dodoc("LICENSE", "README.md","TODO.md*")
