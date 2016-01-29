# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="setuptools-%s" % get.srcVERSION()

def setup():
    shelltools.makedirs("python3")
    shelltools.copytree("../setuptools-%s" % get.srcVERSION(), "%s/python3" % get.workDIR())

def install():
    #pythonmodules.install()
    #pisitools.remove("/usr/lib/%s/site-packages/setuptools/*.exe" % get.curPYTHON())
    shelltools.cd("%s/python3" % get.workDIR())
    pythonmodules.install(pyVer = "3")
    #pisitools.remove("/usr/lib/python3.4/site-packages/setuptools/*.exe")
    pisitools.rename("/usr/bin/easy_install", "py3easy-install")
    #avoid python-setuptools conflict
    pisitools.removeDir("/usr/share")