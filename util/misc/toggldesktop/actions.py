#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools, shelltools
from pisi.actionsapi import get


def setup():
    shelltools.makedirs('build')
    shelltools.cd('build')
    parameters = " ".join([
        "-DTOGGL_VERSION:STRING=\"{}\"".format(get.srcVERSION()),
        "-DTOGGL_PRODUCTION_BUILD=ON",
        "-DTOGGL_ALLOW_UPDATE_CHECK=ON",
        "-DUSE_BUNDLED_LIBRARIES=OFF",
    ])
    cmaketools.configure(parameters=parameters, sourceDir='..')


def build():
    shelltools.makedirs('build')
    shelltools.cd('build')
    cmaketools.make()


def install():
    shelltools.makedirs('build')
    shelltools.cd('build')
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
