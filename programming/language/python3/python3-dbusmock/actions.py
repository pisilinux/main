#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools




shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","0.37.1")

def build():
    python3modules.compile(pyVer = '3')

def install():
    python3modules.install(pyVer = '3')

