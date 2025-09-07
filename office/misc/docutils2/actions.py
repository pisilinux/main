#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="docutils-%s" % get.srcVERSION()

def build():
    pythonmodules.compile()
    
def install():
    pythonmodules.install()

    #Remove .py extensions from scripts in /usr/bin
    for f in shelltools.ls("%s/usr/bin" % get.installDIR()):
        pisitools.domove("/usr/bin/%s" % f, "/usr/bin", f.replace(".py", ""))

    for bin in shelltools.ls("%s/usr/bin" % get.installDIR()):
        pisitools.rename("/usr/bin/%s" % bin, "%s_2" % bin)
    
    
    #Remove .py extensions from scripts in /usr/bin
    for f in shelltools.ls("%s/usr/bin" % get.installDIR()):
        pisitools.domove("/usr/bin/%s" % f, "/usr/bin", f.replace(".py", ""))
    else:
        pisitools.dosym("/usr/bin/rst2man", "/usr/bin/rst2man.py")
        
    # for bin in shelltools.ls("%s/usr/bin" % get.installDIR()):
        # pisitools.rename("/usr/bin/%s" % bin, "%s_3" % bin)
    
    # shelltools.cd("../../build_python/%s" % WorkDir)
    # pythonmodules.install()
    
    

    #Remove .py extensions from scripts in /usr/bin
    # for f in shelltools.ls("%s/usr/bin" % get.installDIR()):
        # pisitools.domove("/usr/bin/%s" % f, "/usr/bin", f.replace(".py", ""))
