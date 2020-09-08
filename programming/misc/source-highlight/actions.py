#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--prefix=/usr \
                         --sysconfdir=/etc \
                         --with-bash-completion=/usr/share/bash-completion/completions")
    
    # fix unused direct dependency analysis
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s bash_completiondir=/usr/share/bash-completion/completions" % get.installDIR())
    pisitools.dodoc("COPYING*", "README*")