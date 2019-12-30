#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    #pisitools.dohtml("docs/build/*")
    #pisitools.insinto("/usr/share/doc/%s/src/" % get.srcNAME(),"docs/src/*")
    pisitools.insinto("/usr/share/man/man1", "doc/pygmentize.1", "pygmentize.1")
    
