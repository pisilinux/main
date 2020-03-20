#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools, shelltools
from pisi.actionsapi import pisitools


def setup():
    cmaketools.configure('-B build')


def build():
    shelltools.cd('build')
    cmaketools.make()


def check():
    shelltools.cd('build')
    shelltools.system('./tests')


def install():
    shelltools.cd('build')
    cmaketools.install()

    pisitools.dodoc('../COPYING')
    pisitools.insinto('/usr/bin', 'sl')
