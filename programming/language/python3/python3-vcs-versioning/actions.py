#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())

def build():
    shelltools.system("rm -f .git_archival.txt")
    shelltools.cd("vcs-versioning")
    python3modules.compile()

def install():
    shelltools.cd("vcs-versioning")
    python3modules.install()

    pisitools.dodoc("README.md")
