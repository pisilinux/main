#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import python3modules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os


# shelltools.export("SETUPTOOLS_SCM_PRETEND_VERSION","%s" % get.srcVERSION())


def build():
    shelltools.system("rm -f .git_archival.txt")
    shelltools.cd("vcs-versioning")
    os.environ["SETUPTOOLS_SCM_PRETEND_VERSION_FOR_VCS_VERSIONING"] = "2.5.0"
    os.environ["SETUPTOOLS_SCM_PRETEND_VERSION"] = "2.5.0"

    # python3modules.compile()
    # shelltools.system("python3 -m build --wheel --no-isolation")
    shelltools.system(
        "SETUPTOOLS_SCM_PRETEND_VERSION=2.5.0 "
        "SETUPTOOLS_SCM_PRETEND_VERSION_FOR_VCS_VERSIONING=2.5.0 "
        "python3 -m build --wheel --skip-dependency-check --no-isolation"
    )

def install():
    shelltools.cd("vcs-versioning")
    # python3modules.install()
    shelltools.system("python3 -m installer --destdir='%s' dist/*.whl" % get.installDIR())

    pisitools.dodoc("README.md")
