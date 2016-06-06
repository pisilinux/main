#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "nose-%s" % get.srcVERSION()

examples = "%s/%s/" % (get.docDIR(), get.srcNAME())

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

def setup():
    shelltools.system("sed -i -e 's:man/man1:share/man/man1:g' setup.py")

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    
    pisitools.rename("/usr/bin/nosetests", "nosetests3")
    pisitools.removeDir("/usr/share/man")

    pisitools.dohtml("doc/*")

    shelltools.chmod("examples/*", 0644)
    pisitools.insinto(examples, "examples/*")
