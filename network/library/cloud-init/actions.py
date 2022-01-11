#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def build():
    pythonmodules.compile(pyVer="3")
    shelltools.system("python3 setup.py build")

def check():
    pass
    #pythonmodules.run("setup.py test", pyVer="3")
    #pythonmodules.run("test/run_all_unittests.py",pyVer="3")
    #pythonmodules.run("test/run_examples_test.py",pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    # unneeded systemd service file
    pisitools.removeDir("/etc/systemd/system/sshd-keygen@.service.d/disable-sshd-keygen-if-cloud-init-active.conf")
    pisitools.removeDir("/lib/systemd/")
    pisitools.dodoc("LICENSE", "README*")
