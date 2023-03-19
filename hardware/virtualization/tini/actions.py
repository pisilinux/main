#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools, pisitools

def setup():
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    pisitools.dobin("tini")
    pisitools.dobin("tini-static")

    # symlink docker-init (nice integration with docker)
    pisitools.dosym("/usr/bin/tini-static", "/usr/bin/docker-init")

    pisitools.dodoc("LICENSE", "README*", "VERSION")
