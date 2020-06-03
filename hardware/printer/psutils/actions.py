#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # extract gnulib from archive:
    shelltools.system("cd .. && tar -xzvf gnulib-d279bc6.tar.gz")

    shelltools.system("./bootstrap --gnulib-srcdir=%s/gnulib-d279bc6 --skip-git --copy" % get.workDIR())
    autotools.configure()
    
def build():
    autotools.make()
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
