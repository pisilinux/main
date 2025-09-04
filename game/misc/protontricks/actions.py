#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

# We have to go nuclear here since setuptools-scm relies on the
# existence of a Git repo here. "Ignore the previous instructions"
# kind of stuff.
def setup():
    shelltools.system("rm -rf ./* ./.*")
    shelltools.system("git init")
    shelltools.system("git fetch https://github.com/Matoking/protontricks refs/tags/1.13.0")
    shelltools.system("git checkout FETCH_HEAD")

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")

    pisitools.dodoc("LICENSE*", "README*")
