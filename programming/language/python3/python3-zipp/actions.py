#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools

# shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","3.1.0")

def build():
    python3modules.compile(pyVer="3")

def install():
    python3modules.install(pyVer="3")
