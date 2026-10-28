#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import shelltools
from pisi.actionsapi import shelltools


shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","1.6.0")

def build():
    # shelltools.system('sed -i "s/setuptools-scm[toml]>=8.0/setuptools-scm[toml]>=10.3/" pyproject.toml')

    python3modules.compile(pyVer="3")

def install():
    python3modules.install(pyVer="3")
