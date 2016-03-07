#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

NoStrip = ["/usr/bin", "/usr/lib", "/usr/qt5/qsci/api"]
conf = {"bindir": "/usr/bin",
        "installdir": get.installDIR(),
        "site-packages": "/usr/lib/python3.4/site-packages"}
def install():
   pythonmodules.run("install.py -z \
                                  -b %(bindir)s \
                                  -i %(installdir)s \
                                  -d %(site-packages)s \
                                  -c" % conf, pyVer = "3")
   pythonmodules.fixCompiledPy()  
