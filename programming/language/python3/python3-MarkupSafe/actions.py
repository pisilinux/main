#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("PYTHONDONTWRITEBYTECODE", "1")

WorkDir = "markupsafe-%s" % get.srcVERSION()

def build():
    python3modules.compile(pyVer="3")

# def check():
    # python3modules.compile("test", pyVer="3")

def install():
    python3modules.install(pyVer="3")

