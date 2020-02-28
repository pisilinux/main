#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -lpthread -lbz2")
    pythonmodules.compile()

def install():
    pythonmodules.install()
    
    # manually add man pages
    pisitools.doman("doc/*.1")
    pisitools.doman("doc/*.5")
    pisitools.doman("doc/*.8")
    
    # manually add documentation
    pisitools.dohtml("doc/*.html")
    
    # manually install bash completion script
    pisitools.insinto("/etc/bash_completion.d", "contrib/bash_completion", "mercurial")