#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools


def setup():
    parameters = ' '.join([
                 '-B build',
                 '-DGSL_TEST=OFF',
                 '-DCMAKE_BUILD_TYPE=Release'
                 '-DCMAKE_EXE_LINKER_FLAGS="%s"' % get.LDFLAGS(),
                 ])
    cmaketools.configure(parameters)

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.install()

    pisitools.dodoc("../LICENSE", "../README*")