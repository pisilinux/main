#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="po4a-%s" % get.srcVERSION()

def setup():
    shelltools.system("export LC_ALL=en_US.UTF-8")
    perlmodules.configure()

def build():
    perlmodules.make()

# def check():
    # perlmodules.make("test")

def install():
    perlmodules.install()

    pisitools.dodoc("README*", "COPYING")
